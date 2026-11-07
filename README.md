# Red-Team Prompt Library & Failure Mode Tracker

A curated library of adversarial prompt templates designed to test the safety and robustness of frontier LLMs, paired with a Python tool to log and categorize model failure modes.

**Built by:** Ibegbunam Emmanuel — AI Training Specialist | Multilingual RLHF & Red-Teaming

## Why this exists
Frontier models are increasingly vulnerable to prompt injection, hallucination induction, and reasoning traps. This repository provides a structured way for red-teamers to log adversarial attacks, score the model's failure, and categorize the root cause (e.g., safety bypass, hallucination, logic failure).

## What it does
- **Adversarial Dataset:** JSONL schema containing categorized attack prompts (Prompt Injection, Hallucination, Bias).
- **Failure Tracker:** Python script to parse logged responses, calculate a "Vulnerability Score" for the model, and generate a report of the most common failure modes.

## Quick Start
```bash
python track_failures.py --input sample_data/red_team_logs.jsonl
