# Prompt: Evaluation of Vaccine Safety Studies for Children

## INPUT

**Attach the PDF file to be analyzed along with this prompt**
- It may be a vaccine **package insert**
- It may be a **scientific article** describing clinical trials

---

## Instruction

Analyze the attached document — whether it's a package insert or a clinical trial article — and evaluate the safety studies with a focus on pediatric application (children ages 0 to 12 years).

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

Evaluate the following criteria using this reference guide:

| Criterion | Why It Matters | What Is Ideal |
|-----------|----------------|---------------|
| **1. Placebo control group** | Allows identification of which reactions are caused by the vaccine vs. coincidental events | Inert placebo (saline). Using another vaccine as comparator obscures true adverse event rates |
| **2. Double-blind study** | Prevents bias in observation and symptom reporting | Neither participants nor researchers know who received vaccine/placebo |
| **3. Randomization** | Ensures differences in outcomes are due to the vaccine, not pre-existing characteristics | Documented random allocation with allocation concealment (researchers cannot predict next assignment) |
| **4. Pediatric sample size** | Small samples cannot detect rare reactions. Detecting 1:1,000 events requires ~3,000 participants | >3,000 children per age group for adequate safety detection; >1,000 is bare minimum and still misses rarer events |
| **5. Follow-up duration** | Autoimmune/neurological reactions may emerge weeks or months later. 30-42 days (common in trials) is grossly inadequate | Minimum 6-12 months; ideal: several years with scheduled assessments |
| **6. Separate age groups** | Infants, toddlers, and older children have different immune systems | Separate analysis: 0-1 years, 1-5 years, 6-12 years |
| **7. Inclusion/exclusion criteria** | Allows understanding of who the results apply to. Overly restrictive criteria (excluding children with any health conditions) limit real-world applicability | Balanced criteria that include representative population; explicit discussion of generalizability limitations |
| **8. Standardized definition of adverse events** | Enables comparison across studies and prevents under/over-reporting | Brighton Collaboration criteria or MedDRA coding; objective thresholds (e.g., fever >38°C) rather than subjective assessments |
| **9. Active monitoring of serious adverse events** | Passive/unsolicited reporting vastly underestimates serious events | Active solicited surveillance for hospitalization, sequelae, deaths with causal investigation; clear distinction between solicited and unsolicited events |
| **10. Assessment of autoimmune/neurological reactions** | Conditions like Guillain-Barré, seizures, myocarditis, encephalitis, and autoimmune disorders are rare but serious | Specific long-term monitoring with scheduled exams/consultations; predefined list of conditions to watch for |
| **11. Vulnerable subgroups** | Premature infants, immunocompromised, children with allergies, chronic conditions, or on concurrent medications may react differently | Intentional inclusion and separate analysis of these groups; not excluded from trials |
| **12. Robust statistical analysis** | Most vaccine trials are powered for efficacy, not safety—a fundamental limitation. Without proper power, safety signals are missed | Study powered for safety outcomes; confidence intervals, p-values, power calculation documented; intention-to-treat analysis |
| **13. Data transparency** | Allows independent verification by other researchers | Independent Data Safety Monitoring Board (DSMB); raw data and individual participant data (IPD) available; peer-reviewed publication |
| **14. Post-marketing surveillance** | Detects rare reactions that only appear in millions of doses. Passive systems (VAERS, Yellow Card) rely on voluntary reporting and vastly underestimate true rates | Active pharmacovigilance system with periodic public reports; not reliant solely on passive reporting |
| **15. Conflict of interest / funding source** | Industry-funded studies are more likely to report favorable outcomes; financial ties can bias interpretation | Independent funding or full disclosure of all financial ties; researchers without conflicts conduct analysis |
| **16. All-cause mortality and morbidity** | Focusing only on "vaccine-related" outcomes can miss overall harm; causality determination is subjective | Report total deaths and hospitalizations in all groups, not just those judged "related" to vaccine |

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
