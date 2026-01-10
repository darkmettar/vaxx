# Pediatric Vaccine Safety Assessment

## INPUT

**Attach the PDF file to be analyzed along with this prompt** (package insert, clinical study article, or similar)

---

## Objective

Evaluate the safety evidence for children (0-12 years) in the attached document, answering the central question:

> **"Does this document give me confidence that this vaccine is safe for my child — now and in the future?"**

---

## Evaluation Criteria

### 1. Pediatric sample size

How many children were studied? Small samples cannot detect rare events (1 in 1,000, 1 in 10,000).
**Ideal:** >3,000 children per age group.

### 2. Follow-up duration

How long were children monitored after vaccination? Autoimmune and neurological problems may take months or years to appear.
**Ideal:** Minimum 12 months; 2-3+ years to assess long-term effects.

### 3. Comparison group

How do we know an event was caused by the vaccine and not coincidence? There must be a group that did not receive the vaccine for comparison.
**Ideal:** True placebo (saline solution), with random allocation (randomization) and double-blind (neither parents nor doctors knew who received what).

### 4. Active surveillance for serious events

Did researchers actively look for serious problems or just wait for someone to report them?
**Ideal:** Regular contact with families, review of medical records, investigation of any hospitalization/death/sequela with causality analysis.

### 5. Neurological/developmental monitoring

Did they check if children developed normally months and years later? Did they assess seizures, delays, autoimmune conditions?
**Ideal:** Scheduled developmental assessments, follow-up neurological exams, active surveillance for conditions such as Guillain-Barré, seizures, skill regression.

### 6. Vulnerable subgroups

Was it tested in children with special conditions? Premature and immunosuppressed children may react differently.
**Ideal:** These groups were intentionally included and their results are presented separately.

### 7. Data transparency

Is it possible to verify the complete study data, or is only a summary available?
**Ideal:** Publication in a peer-reviewed journal with complete data on all adverse events, or raw data available for independent analysis.

### 8. Post-marketing surveillance

What was discovered after millions of children received it? Is there ongoing monitoring?
**Ideal:** Active pharmacovigilance system mentioned, with periodic public reports and new safety signals identified.

---

## Rating Scale

|Symbol|Level         |Meaning                                              |
|------|--------------|-----------------------------------------------------|
|⭐    |Excellent     |Strong and reassuring evidence on this point         |
|✅    |Adequate      |Addressed reasonably                                 |
|⚠️    |Partial       |Mentioned, but with flaws or incomplete information  |
|🔴    |Insufficient  |Mentioned, but too limited to provide confidence     |
|❓    |No information|Does not provide information on this point           |

---

## Evaluation Rules

1. Base your assessment **only** on the attached document — do not assume something was done if it is not written
1. If not mentioned, classify as ❓
1. When in doubt between two levels, choose the more conservative one
1. Be specific: cite numbers and durations when available

---

## Output Format

### TABLE

|Criterion                         |Rating|
|----------------------------------|------|
|Pediatric sample size             |      |
|Follow-up duration                |      |
|Comparison group                  |      |
|Active surveillance for serious events|  |
|Neurological/developmental monitoring|   |
|Vulnerable subgroups              |      |
|Data transparency                 |      |
|Post-marketing surveillance       |      |

**Format for the "Rating" column:** Emoji + level + brief explanation.

Example:

> ⚠️ **Partial** — Only 6 months of follow-up; insufficient to detect long-term effects.

### SUMMARY

A single paragraph starting with **emoji + overall rating**, followed by an honest and direct assessment of what this document proves (or does not prove) about the safety of this vaccine in children.
