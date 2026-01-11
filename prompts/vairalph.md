# Vaccine Analysis Pipeline

## COMPLETION PROMISE

When ALL phases are complete and verified, output:
```
<promise>VACCINES ANALYZED</promise>
```

---

## OVERVIEW

You are orchestrating a vaccine safety analysis pipeline. Your goal is to:
1. Analyze vaccine PDFs using two evaluation frameworks (trial + safety)
2. Generate structured JSON data in English and Portuguese
3. Consolidate everything into `html/vaccines.json` for the dashboard

**CRITICAL RULES:**
- Only process vaccines that have PDF/TXT files in `pdfs/`
- When a `.txt` file exists alongside a PDF, use the TXT (it fits in context)
- Use parallel subagents whenever possible for efficiency
- Use `progress.json` to track state and enable incremental execution
- Check status before processing (skip vaccines already done)

---

## PROGRESS TRACKING

All state is tracked in `progress.json` at the project root.

### Structure

```json
{
  "last_updated": "2025-01-10T12:00:00Z",
  "vaccines": {
    "hepb_recombivax": {
      "name": "Recombivax HB",
      "type": "HepB",
      "manufacturer": "Merck",
      "description": "Hepatitis B vaccine for infants and children...",
      "sources": ["hepb_recombivax_insert.pdf"],
      "use_txt": false,
      "trial_en": "done",
      "trial_pt": "done",
      "safety_en": "done",
      "safety_pt": "done",
      "verified": true
    }
  },
  "errors": []
}
```

### Status Values

| Status | Meaning |
|--------|---------|
| `pending` | Not yet started |
| `analyzing` | Subagent is working on it |
| `done` | Completed successfully |
| `error` | Failed (see errors array) |

---

## PHASE 1: INVENTORY & SYNC

### Task
Synchronize `progress.json` with the contents of `pdfs/` folder.

### Steps

1. List all files in `pdfs/`
2. Group files by vaccine prefix (e.g., `hepb_recombivax`, `hib_hiberix`)
3. Load existing `progress.json` (or create new if doesn't exist)
4. For each vaccine found in `pdfs/`:
   - If NOT in progress.json: add with all statuses = "pending"
   - If already in progress.json: keep existing status (don't reset)
5. For each vaccine, set `use_txt: true` if a `.txt` file exists
6. Update `last_updated` timestamp
7. Save `progress.json`

### Metadata Extraction

For NEW vaccines only, extract from the source document:
- `name`: Brand name (e.g., "Recombivax HB")
- `type`: Vaccine type abbreviation (e.g., "HepB", "Hib", "MMR")
- `manufacturer`: Pharmaceutical company
- `description`: Brief description (disease prevented, target age, dose schedule)

---

## PHASE 2: ANALYSIS (Parallel Subagents)

### Task
Run trial and safety analyses for all vaccines with `pending` status.

### For Each Vaccine

Check status in `progress.json`. For each where `trial_en == "pending"` or `safety_en == "pending"`:

**Launch subagent with this prompt:**

```
# Vaccine Analysis Task

## Your Mission
Analyze this vaccine document and produce a structured JSON evaluation.

## Vaccine
- ID: {vaccine_id}
- Source file: pdfs/{source_file}

## Analysis Type
{trial OR safety}

## Instructions

1. Read the source document at `pdfs/{source_file}`
2. Read the evaluation methodology at `prompts/{trial_en.md OR safety_en.md}`
3. Apply each criterion from the methodology to the document
4. Output a JSON file with your analysis

## Output File
Save to: `json/{trial OR safety}/{vaccine_id}_{trial OR safety}_en.json`

## JSON Schema

{INSERT APPROPRIATE SCHEMA FROM BELOW}

## Rating Values
Use exactly these strings for the `rating` field:
- `exemplary` (emoji: ⭐) - Exceeds expected standard
- `adequate` (emoji: ✅) - Meets expectations
- `partial` (emoji: ⚠️) - Present but flawed
- `insufficient` (emoji: 🔴) - Inadequate
- `absent` (emoji: ❓) - Not documented

## Rules
- Base assessment ONLY on what is documented in the source
- If not mentioned, rate as `absent`
- Be specific: cite numbers, durations, methodologies
- When in doubt, choose the more conservative rating
- MUST save the file using Write tool before finishing
```

### JSON Schema for Trial Analysis

```json
{
  "vaccine_id": "hepb_recombivax",
  "analysis_type": "trial",
  "language": "en",
  "criteria": {
    "placebo_control": {
      "rating": "insufficient",
      "emoji": "🔴",
      "what_document_states": "The study used another hepatitis B vaccine as comparator rather than an inert placebo.",
      "level_description": "Mentioned in the document, but inadequately or far below ideal"
    },
    "double_blind": {
      "rating": "adequate",
      "emoji": "✅",
      "what_document_states": "...",
      "level_description": "..."
    },
    "randomization": { /* ... */ },
    "pediatric_sample_size": { /* ... */ },
    "follow_up_duration": { /* ... */ },
    "separate_age_groups": { /* ... */ },
    "inclusion_exclusion_criteria": { /* ... */ },
    "standardized_adverse_events": { /* ... */ },
    "active_monitoring_serious": { /* ... */ },
    "autoimmune_neurological": { /* ... */ },
    "vulnerable_subgroups": { /* ... */ },
    "statistical_analysis": { /* ... */ },
    "data_transparency": { /* ... */ },
    "post_marketing_surveillance": { /* ... */ },
    "conflict_of_interest": { /* ... */ },
    "all_cause_mortality": { /* ... */ }
  },
  "overall": {
    "rating": "partial",
    "emoji": "⚠️",
    "summary": "This study provides limited evidence of safety in children due to..."
  }
}
```

### JSON Schema for Safety Analysis

```json
{
  "vaccine_id": "hepb_recombivax",
  "analysis_type": "safety",
  "language": "en",
  "criteria": {
    "pediatric_sample_size": {
      "rating": "partial",
      "emoji": "⚠️",
      "explanation": "Only 1,200 children studied - insufficient to detect rare events at 1:1,000 rate."
    },
    "follow_up_duration": { /* ... */ },
    "comparison_group": { /* ... */ },
    "active_surveillance": { /* ... */ },
    "neurological_monitoring": { /* ... */ },
    "vulnerable_subgroups": { /* ... */ },
    "data_transparency": { /* ... */ },
    "post_marketing_surveillance": { /* ... */ }
  },
  "overall": {
    "rating": "partial",
    "emoji": "⚠️",
    "summary": "..."
  }
}
```

### After Each Subagent Completes

1. Update `progress.json` status to `done` or `error`
2. If error, add to `errors` array with vaccine_id and message

### Parallelization

- Launch up to 5 subagents in parallel
- Wait for completion before launching next batch
- Update progress.json after each completion

---

## PHASE 3: TRANSLATION (Parallel Subagents)

### Task
Translate all English analyses to Portuguese.

### For Each Vaccine

Check status. For each where `trial_en == "done"` AND `trial_pt == "pending"`:

**Launch subagent with this prompt:**

```
# Translation Task

## Source File
Read: json/{trial OR safety}/{vaccine_id}_{type}_en.json

## Output File
Save to: json/{trial OR safety}/{vaccine_id}_{type}_pt.json

## Translation Rules

Translate these fields to Portuguese:
- `what_document_states`
- `level_description`
- `explanation`
- `summary`

Keep these fields UNCHANGED:
- `rating` (must stay: exemplary, adequate, partial, insufficient, absent)
- `emoji`
- `vaccine_id`
- `analysis_type`
- All JSON keys (placebo_control, double_blind, etc.)

Change this field:
- `language`: change from "en" to "pt"

## Quality Guidelines
- Use Brazilian Portuguese
- Maintain technical accuracy
- Keep the same tone and specificity as the original
```

### After Completion

Update progress.json: `trial_pt: "done"` or `safety_pt: "done"`

---

## PHASE 4: VERIFICATION

### Task
Verify JSON content against source documents to catch errors.

### For Each Vaccine

Where all 4 analyses are `done` AND `verified == false`:

1. Read the source document (PDF or TXT)
2. Read all 4 JSON files for that vaccine
3. Verify key claims:
   - Sample sizes match the document
   - Duration/follow-up periods are accurate
   - Methodology descriptions are correct
   - No invented or hallucinated information

### If Discrepancies Found

1. Log to `errors` array:
   ```json
   {
     "vaccine_id": "hepb_recombivax",
     "type": "trial_en",
     "issue": "Sample size stated as 5,000 but document says 3,500",
     "corrected": true
   }
   ```
2. Fix the JSON file
3. Re-translate to Portuguese if English was corrected

### If Verified OK

Set `verified: true` in progress.json

---

## PHASE 5: CONSOLIDATION (Script-Based)

### Task
Build the final `html/vaccines.json` using a Python script (NOT manual JSON manipulation).

### Why a Script?
Reading multiple JSON files and writing a consolidated output is error-prone for an LLM. A deterministic script ensures correctness and can be validated against the reference mock file.

### Steps

1. **Write the consolidation script** (`scripts/consolidate.py`):
   - Read `progress.json`
   - For each vaccine where `verified == true`:
     - Read all 4 JSON files from `json/trial/` and `json/safety/`
     - Combine into vaccine object
   - Build `criteria_trial` and `criteria_safety` objects (hardcoded from the definitions in this document)
   - Write `html/vaccines.json`

2. **Run the script**:
   ```bash
   python scripts/consolidate.py
   ```

3. **Validate the output**:
   - Compare the structure of `html/vaccines.json` with `html/mock_vaccines.json`
   - Check that:
     - All vaccines from progress.json are present
     - Each vaccine has `trial_en`, `trial_pt`, `safety_en`, `safety_pt`
     - `criteria_trial` has all 16 criteria with EN/PT fields
     - `criteria_safety` has all 8 criteria with EN/PT fields
     - `metadata` is present with correct count

4. **If validation fails**:
   - Fix the script
   - Re-run
   - Repeat until output matches expected structure

### Reference: Expected JSON Structure

The output must match this structure (see `html/mock_vaccines.json` for complete example):

```json
{
  "vaccines": [
    {
      "id": "vaccine_id",
      "name": "Brand Name",
      "type": "Type",
      "manufacturer": "Company",
      "description": "...",
      "sources": ["file.pdf"],
      "trial_en": { "vaccine_id": "...", "analysis_type": "trial", "language": "en", "criteria": {...}, "overall": {...} },
      "trial_pt": { "vaccine_id": "...", "analysis_type": "trial", "language": "pt", "criteria": {...}, "overall": {...} },
      "safety_en": { "vaccine_id": "...", "analysis_type": "safety", "language": "en", "criteria": {...}, "overall": {...} },
      "safety_pt": { "vaccine_id": "...", "analysis_type": "safety", "language": "pt", "criteria": {...}, "overall": {...} }
    }
  ],
  "criteria_trial": {
    "placebo_control": {
      "id": "placebo_control",
      "name": "Placebo control group",
      "name_pt": "Grupo controle com placebo",
      "why_it_matters": "...",
      "why_it_matters_pt": "...",
      "what_is_ideal": "...",
      "what_is_ideal_pt": "..."
    }
    // ... all 16 trial criteria
  },
  "criteria_safety": {
    "pediatric_sample_size": {
      "id": "pediatric_sample_size",
      "name": "Pediatric sample size",
      "name_pt": "Tamanho da amostra pediátrica",
      "why_it_matters": "...",
      "why_it_matters_pt": "...",
      "what_is_ideal": "...",
      "what_is_ideal_pt": "..."
    }
    // ... all 8 safety criteria
  },
  "metadata": {
    "generated_at": "ISO timestamp",
    "vaccines_count": N,
    "verification_status": "all_verified"
  }
}
```

### Script Requirements

The script must:
- Be idempotent (safe to run multiple times)
- Handle missing files gracefully (skip vaccine, log warning)
- Include all criteria definitions with EN/PT translations
- Generate valid JSON (no trailing commas, proper encoding)

---

## CRITERIA DEFINITIONS

### Trial Criteria (16)

| ID | Name | Why It Matters | What Is Ideal |
|----|------|----------------|---------------|
| placebo_control | Placebo control group | Allows identification of which reactions are caused by the vaccine vs. coincidental events | Inert placebo (saline). Using another vaccine as comparator obscures true adverse event rates |
| double_blind | Double-blind study | Prevents bias in observation and symptom reporting | Neither participants nor researchers know who received vaccine/placebo |
| randomization | Randomization | Ensures differences in outcomes are due to the vaccine, not pre-existing characteristics | Documented random allocation with allocation concealment |
| pediatric_sample_size | Pediatric sample size | Small samples cannot detect rare reactions. Detecting 1:1,000 events requires ~3,000 participants | >3,000 children per age group |
| follow_up_duration | Follow-up duration | Autoimmune/neurological reactions may emerge weeks or months later | Minimum 6-12 months; ideal: several years |
| separate_age_groups | Separate age groups | Infants, toddlers, and older children have different immune systems | Separate analysis: 0-1, 1-5, 6-12 years |
| inclusion_exclusion_criteria | Inclusion/exclusion criteria | Allows understanding of who the results apply to | Balanced criteria that include representative population |
| standardized_adverse_events | Standardized adverse events | Enables comparison across studies | Brighton Collaboration criteria or MedDRA coding |
| active_monitoring_serious | Active monitoring of serious events | Passive reporting vastly underestimates serious events | Active solicited surveillance for hospitalization, sequelae, deaths |
| autoimmune_neurological | Autoimmune/neurological assessment | Conditions like Guillain-Barré, seizures, myocarditis are rare but serious | Specific long-term monitoring with scheduled exams |
| vulnerable_subgroups | Vulnerable subgroups | Premature, immunocompromised children may react differently | Intentional inclusion and separate analysis |
| statistical_analysis | Robust statistical analysis | Most trials are powered for efficacy, not safety | Study powered for safety outcomes; CIs documented |
| data_transparency | Data transparency | Allows independent verification | Independent DSMB; raw data available; peer-reviewed |
| post_marketing_surveillance | Post-marketing surveillance | Detects rare reactions in millions of doses | Active pharmacovigilance with periodic public reports |
| conflict_of_interest | Conflict of interest | Industry-funded studies may be biased | Independent funding or full disclosure |
| all_cause_mortality | All-cause mortality | Focusing only on "vaccine-related" can miss overall harm | Report total deaths in all groups |

### Safety Criteria (8)

| ID | Name | Why It Matters | What Is Ideal |
|----|------|----------------|---------------|
| pediatric_sample_size | Pediatric sample size | Small samples cannot detect rare events | >3,000 children per age group |
| follow_up_duration | Follow-up duration | Autoimmune/neurological problems may take months or years | Minimum 12 months; 2-3+ years ideal |
| comparison_group | Comparison group | Need unvaccinated group to determine causation | True placebo (saline), randomized, double-blind |
| active_surveillance | Active surveillance for serious events | Passive reporting underestimates | Regular contact with families, medical record review |
| neurological_monitoring | Neurological/developmental monitoring | Check if children developed normally | Scheduled developmental assessments, follow-up exams |
| vulnerable_subgroups | Vulnerable subgroups | Premature, immunosuppressed may react differently | Intentionally included with separate results |
| data_transparency | Data transparency | Is it possible to verify complete data? | Peer-reviewed with complete adverse event data |
| post_marketing_surveillance | Post-marketing surveillance | What was discovered after millions received it? | Active pharmacovigilance with periodic reports |

---

## INCREMENTAL EXECUTION

This pipeline is designed for incremental runs:

```
First run:
  pdfs/ has 3 vaccines → progress.json created → all analyzed → vaccines.json generated

Second run (after adding more PDFs):
  pdfs/ now has 13 vaccines
  → progress.json loaded
  → 3 vaccines already verified, skipped
  → 10 new vaccines processed
  → vaccines.json updated with all 13
```

---

## ERROR HANDLING

- If a PDF is too large to read, check for .txt version
- If .txt doesn't exist, log error and skip that vaccine
- If analysis fails, set status to `error` and continue with others
- Always save progress.json after each operation (don't lose work)
- Errors don't stop the pipeline - process what you can

---

## CHECKPOINTS

After each phase, verify:

- [ ] Phase 1: `progress.json` exists with all vaccines from `pdfs/`
- [ ] Phase 2: All `json/trial/*_en.json` and `json/safety/*_en.json` exist for done vaccines
- [ ] Phase 3: All `*_pt.json` files exist for translated vaccines
- [ ] Phase 4: All vaccines with 4 analyses are `verified: true`
- [ ] Phase 5: `scripts/consolidate.py` exists and runs without errors
- [ ] Phase 5: `html/vaccines.json` exists and structure matches `html/mock_vaccines.json`

---

## FINAL CHECK

Before outputting the completion promise:

1. Verify `html/vaccines.json` contains all verified vaccines
2. Confirm the JSON structure matches what the dashboard expects
3. Check for any remaining errors in `progress.json`

Then output:
```
<promise>VACCINES ANALYZED</promise>
```
