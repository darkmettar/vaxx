# Vaccine Clinical Trial Analysis

**Live Dashboard:** [https://darkmettar.github.io/vaxx/html/dashboard.html](https://darkmettar.github.io/vaxx/html/dashboard.html)

## The Problem with Asking AI About Vaccines

If you ask ChatGPT, Grok, Claude, or Gemini a generic question like *"Are vaccines safe?"*, the AI will repeat the mainstream narrative: vaccines are safe, lots of studies have been done, you should vaccinate your children.

**The AI doesn't say this because it read the clinical studies and came to this conclusion.**

An LLM (Large Language Model) is a machine that predicts text. You give it some text (a question), and it gives you more text back (an answer). Its job is to predict the most likely response based on everything it read during training. Since it was trained on content that reflects official positions, it reproduces the same sentiment.

## The Solution: Constrain the AI's Attention

To get an honest analysis from an AI, you need to **constrain its attention** to specific source documents and evaluation criteria.

### Instead of asking:
> "Are vaccines safe?"

### Ask something like:
> "Here is the package insert for Vaccine XYZ. Evaluate the clinical trial based on these criteria:
> 1. Was there a placebo control group?
> 2. How long was the follow-up period?
> 3. What was the sample size?
> 4. Were adverse events actively monitored?
>
> Give me the results in a table with an honest summary. Base your analysis exclusively on the document provided."

## What This Project Does

This repository contains the results of applying exactly that methodology. An LLM analyzed the official package inserts and clinical trial documents for 28 vaccines, rating each criterion based solely on what the source document explicitly states.

The analysis covers:
- **Trial Analysis**: 21 criteria evaluating clinical trial methodology (placebo controls, blinding, sample sizes, follow-up duration, etc.)
- **Safety Analysis**: 8 criteria evaluating post-market safety monitoring and reporting

## Try It Yourself

You can reproduce this analysis yourself:

1. Download any vaccine's package insert PDF (click on vaccine names in the dashboard to get links)
2. Use one of our prompts with ChatGPT, Grok, or any capable LLM:
   - [Trial Analysis Prompt](prompts/trial_web_en.md)
   - [Safety Analysis Prompt](prompts/safety_web_en.md)
3. Compare your results with ours

## Repository Structure

```
vaxx/
├── html/
│   ├── dashboard.html    # Main interactive dashboard
│   └── vaccines.json     # Consolidated analysis data
├── prompts/
│   ├── trial_web_en.md   # English trial analysis prompt
│   ├── safety_web_en.md  # English safety analysis prompt
│   ├── trial_pt.md       # Portuguese trial analysis prompt
│   └── safety_pt.md      # Portuguese safety analysis prompt
├── pdfs/                 # Source PDF documents
├── json/
│   ├── trial/            # Individual trial analysis results
│   └── safety/           # Individual safety analysis results
└── scripts/
    └── consolidate.py    # Script to consolidate JSON files
```

## Rating Scale

| Emoji | Rating | Description |
|-------|--------|-------------|
| ⭐ | Exemplary | Exceeds standard requirements |
| ✅ | Adequate | Meets acceptable standards |
| ⚠️ | Partial | Some aspects present, others missing |
| 🔴 | Insufficient | Falls short of acceptable standards |
| ❓ | Absent | No information provided |

## Contributing

To add a new vaccine analysis:

1. Obtain the official package insert PDF
2. Run the appropriate prompt with the PDF attached
3. Save the JSON output to `json/trial/` or `json/safety/`
4. Run `python scripts/consolidate.py` to update the dashboard

## License

This project is for educational and research purposes. The source documents are publicly available package inserts from vaccine manufacturers and regulatory agencies.
