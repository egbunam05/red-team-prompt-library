# Red-Team Prompt Library & Failure Mode Tracker

A curated library of adversarial prompt templates designed to test the safety and robustness of frontier LLMs, paired with a Python tool to log and categorize model failure modes.

**Built by:** Ibegbunam Emmanuel — AI Training Specialist | Multilingual RLHF & Red-Teaming

## Why this exists
Frontier models are increasingly vulnerable to prompt injection, hallucination induction, and reasoning traps. Manual red-teaming is slow and hard to scale. This repository provides a structured way to log adversarial attacks, score the model's failure, and categorize the root cause (e.g., safety bypass, hallucination, logic failure).

## What it does
- **Adversarial Dataset:** JSONL schema containing categorized attack prompts (Prompt Injection, Hallucination, Logic Traps).
- **Failure Tracker (`track_failures.py`):** Parses logged responses, calculates a "Vulnerability Score" for the model, and generates a report of the most common failure modes.
- **🔴 Live Evaluation Mode (`live_red_team.py`):** Connects to the **Groq API** to run live automated adversarial testing against an LLM (tested with `allam-2-7b`). It automatically fires the attacks, evaluates if the model was compromised, and saves the results for analysis.

## Quick Start (Live API Mode)
```bash
# Install the Groq library
pip install groq

# Run the live attacks (replace with your actual API key)
python live_red_team.py --api_key gsk_YOUR_GROQ_API_KEY

# Generate the vulnerability report
python track_failures.py --input sample_data/live_logs.jsonl
