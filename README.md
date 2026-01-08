# Fake Review Detection System 🕵️‍♂️

### TL;DR
An explainable NLP-based system that flags **high-risk promotional reviews** using behavioral patterns (not keyword traps).  
Built to prioritize **trust, transparency, and reproducibility** over over-claimed accuracy.

---

## Why this project exists
E-commerce platforms rely heavily on reviews, but promotional and incentivized reviews can distort trust.

Instead of claiming perfect fake-review detection, this project focuses on:
- identifying **spam-like behavioral patterns**
- explaining *why* a review is flagged
- minimizing false positives on genuine human reviews

---

## Key Features
- Behavioral fake review detection (not keyword-based)
- Sentiment analysis using TextBlob
- Explainable decision signals
- Risk-based suspicion scoring
- Unit-tested core logic
- Interactive Streamlit UI

---

## How it Works (High Level)
A review is analyzed using multiple **behavioral signals**, such as:
- unnatural positivity density
- very short but highly positive content
- excessive punctuation
- rating–content mismatch

If multiple risky behaviors are present, the review is flagged as **high-risk**.

> ⚠️ This system is designed for **screening**, not absolute judgment.

---

## Design Decisions & Trade-offs

### Why heuristics instead of ML?
- No reliable labeled dataset available
- Heuristics are transparent and explainable
- Easier to tune and reason about at small scale

### Why behavioral signals over keywords?
Keywords alone cause false positives.  
Behavioral patterns better reflect how spam reviews are actually written.

### Why not deep learning?
Deep models add complexity, opacity, and training cost without guaranteeing better results at this scale.

---

## Limitations & Responsible Usage

- This system does not guarantee detection of all fake reviews

- Subtle or well-written paid reviews may pass

- Genuine users may occasionally be flagged (false positives)

- Intended for review moderation support, not automated banning

---

#### Future Improvements

- Dataset-driven tuning

- Reviewer behavior history

- Semantic similarity detection

- Dashboard analytics for moderators
