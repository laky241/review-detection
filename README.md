# Fake Review & Rating Manipulation Detector

## TL;DR
A rule-based system to detect suspicious product reviews by analyzing text patterns, sentiment mismatch, and rating behavior.

## Why this project
Fake reviews mislead customers and damage trust. This tool focuses on explainable heuristics instead of black-box models.

This project focuses on behavioral patterns commonly seen in promotional or incentivized reviews rather than keyword-based detection.
## Features
- Detects promotional language
- Flags rating vs sentiment mismatch
- Identifies repeated phrases
- Streamlit dashboard
- Logging and tests included

## How to run
```bash
pip install -r requirements.txt
streamlit run app.py
