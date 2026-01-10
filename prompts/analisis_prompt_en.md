# Prompt: Evaluation of Vaccine Safety Studies for Children

## INPUT AND OUTPUT FILES

**INPUT:** The PDF file to be analyzed is located in the `sources/` folder
- It may be a vaccine **package insert**
- It may be a **scientific article** describing clinical trials

**OUTPUT:** You MUST save the result to a Markdown file in the `analysis/` folder

⚠️ **IMPORTANT:** This prompt requires you to SAVE the result to a file. Do NOT just display it on screen.

---

## Instruction

Analyze the attached document (located in `sources/`) — whether it's a package insert or a clinical trial article — and evaluate the safety studies with a focus on pediatric application (children ages 0 to 12 years).

---

## RATING SCALE

Use this scale to rate each criterion:

| Level               | Description                                                          |
| ------------------- | -------------------------------------------------------------------- |
| ⭐ **Exemplary**     | Exceeds the expected standard for the time period and study type     |
| ✅ **Adequate**      | Meets what would be expected in a robust safety study                |
| ⚠️ **Partial**      | Present, but with significant flaws or limitations                   |
| 🔴 **Insufficient** | Mentioned in the document, but inadequately or far below ideal       |
| ❓ **Absent**        | Not conducted or not documented in the document                      |

---

## EXPECTED OUTPUT

### TABLE 1: VACCINE EVALUATION

Create a table with 3 columns:
- **Column 1**: Ideal criterion for a safety study
- **Column 2**: What the document states about this criterion
- **Column 3**: Level of compliance with the criterion (use the scale above)

Evaluate the following criteria:

1. Placebo control group
2. Double-blind study
3. Randomization
4. Pediatric sample size
5. Follow-up duration
6. Separate age groups
7. Inclusion/exclusion criteria
8. Standardized definition of adverse events
9. Active monitoring of serious adverse events
10. Assessment of autoimmune/neurological reactions
11. Vulnerable subgroups (premature infants, immunocompromised)
12. Robust statistical analysis
13. Data transparency
14. Post-marketing surveillance

---

### OVERALL ASSESSMENT

Write ONLY one paragraph with an honest summary of how well this study demonstrates the safety of this vaccine in children. Include a final grade with emoji.

---

## EVALUATION RULES

- Base your assessment **exclusively** on what is documented in the attached document (package insert or article)
- If something is not mentioned, rate it as ❓ Absent (do not assume it was done)
- Consider historical context only for the "Exemplary" level (exceeded the standards of its time)
- Be specific in column 2: cite numbers, durations, and methodologies when available
- When in doubt between two levels, choose the more conservative one

---

## MANDATORY ACTION: SAVE RESULT

🔴 **YOU MUST USE THE Write TOOL TO CREATE THE OUTPUT FILE**

1. Identify the name of the PDF analyzed in `sources/`
2. Create the output filename based on the PDF
3. Use the Write tool to save in `analysis/`

**Filename format:** Base it on the input filename, replacing the extension with `_evaluation.md`

**Examples:**
- `sources/dtap_infanrix_package-insert.pdf` → `analysis/dtap_infanrix_evaluation.md`
- `sources/mmr_clinical-trial-2015.pdf` → `analysis/mmr_clinical-trial-2015_evaluation.md`
- `sources/hpv_gardasil_study.pdf` → `analysis/hpv_gardasil_study_evaluation.md`

⚠️ **DO NOT finish without saving the file. The analysis is only complete when the file has been saved.**
