---
marp: true
theme: default
paginate: true
size: 16:9
---

<!-- _class: lead -->
# MindScan
## AI Mental Wellness Indicator System

B.Sc. Computer Science – Final Year Project  
**[College Name]**  
**[Academic Year]**

**[Your Full Name]** | **[Roll No]**  
Guide: **[Guide Name]**

---

# Contents

1. Introduction
2. Problem Statement
3. Objectives
4. System Study
5. Solution Overview
6. Requirements & Tech Stack
7. Design / Architecture
8. Datasets
9. Implementation
10. Results
11. Deployment
12. Limitations
13. Future Work
14. Conclusion
15. Thank You

---

# Introduction

- **MindScan** – AI-assisted mental wellness indicator system
- Analyzes behavioral and linguistic patterns for early emotional stress indicators
- Integrates: journaling text, speech characteristics, typing rhythm, lifestyle inputs
- Uses NLP and ML to produce **risk indicator bands** and emotional trend insights
- **Not a medical diagnostic tool** – for awareness and support guidance only

---

# Problem Statement

- Many mental health apps rely only on **self-reported mood** with little behavioral analysis
- Hard to detect meaningful emotional patterns over time
- **Need:** A system that combines multiple behavioral signals and uses AI to produce early emotional stress indicators in a responsible, ethical way

---

# Objectives

- Design a system to analyze behavioral signals related to emotional wellbeing
- Apply **NLP** to detect emotional sentiment patterns
- Analyze speech tempo and behavioral metrics
- Generate **risk indicator bands** (Low / Moderate / Elevated)
- Provide emotional trend **dashboards**
- Maintain ethical safeguards (no medical diagnosis)

---

# System Study

**Existing systems:** Mood trackers, journaling apps, meditation tools, AI therapy chatbots  

**Limitations:**
- Dependence on manual mood entry
- Little behavioral signal analysis
- Limited speech/typing integration
- Minimal predictive capability  

**Proposed:** MindScan combines multiple behavioral signals and AI analysis for deeper insight and risk indicators.

---

# Solution Overview

- **Input:** Journal text (primary); voice/typing designed for future
- **Processing:** Sentiment analysis (TextBlob), risk scoring, SQLite persistence
- **Output:** Risk bands (Low/Moderate/Elevated), trend charts, sample data fallback
- **Prototype:** Journal analysis + dashboard + SQLite + CSV datasets for demo

---

# Requirements & Tech Stack

**Hardware:** 8 GB RAM, microphone (optional), internet  

**Software:**
- Python 3.9+
- **Streamlit** (frontend)
- **TextBlob / NLTK** (NLP, sentiment)
- **Pandas, NumPy, Scikit-learn**
- **SQLite** (database)

---

# Design / Architecture

**Layers:**
1. **Input** – Journal, voice, typing, lifestyle
2. **Processing** – Feature extraction (sentiment, tempo, metrics)
3. **AI Analysis** – Risk scoring, classification
4. **Visualization** – Dashboards, charts, alerts  

**Components:** Streamlit UI, sentiment service, risk engine, DB layer, data loader, dashboard

---

# Datasets

| Dataset | Purpose |
|---------|---------|
| `sample_journal_entries.csv` | 15 labeled entries (Positive/Negative/Neutral) for demo & reference |
| `sentiment_training_data.csv` | 13 short texts for training/experiments |
| `dashboard_sample_trend.csv` | Sample weekly sentiment trend (used when DB is empty) |

Dashboard falls back to sample data when no user entries exist (e.g. Streamlit Cloud).

---

# Implementation

- **Journal page:** Text input → sentiment analysis → risk band → save to DB
- **Dashboard:** Sentiment trend chart, current risk summary
- **Backend:** `sentiment_service.py`, `risk_engine.py`, `db_manager.py`, `utils/data_loader.py`
- **Database:** SQLite – `journal_entries` with sentiment and timestamp
- **Data:** Sample CSVs in `data/` for demo and fallback

---

# Results

- Sentiment polarity (Positive / Neutral / Negative) from journal text
- Risk band: **Low**, **Moderate**, or **Elevated** from score thresholds
- Dashboard shows sentiment trend over days
- Journal entries persisted in SQLite for demo
- Sample dataset shown in dashboard when DB is empty

---

# Deployment (Streamlit Cloud)

- **Hosted on:** [share.streamlit.io](https://share.streamlit.io)
- **Main file:** `mindscan_streamlit_project/app.py`
- **Note:** Ephemeral filesystem – SQLite resets on redeploy; sample datasets provide demo data
- **Stack:** Streamlit, Pandas, TextBlob, SQLite; no librosa/soundfile (removed for cloud compatibility)

---

# Limitations

- Prototype implements journal-based flow; voice/typing modules are designed but not built
- Not a clinical tool; results are wellness indicators only
- Single-user, local deployment; no authentication in prototype
- Sentiment from general-purpose NLP; not tuned for clinical language

---

# Future Work

- Voice analysis (tempo, energy) and typing behaviour modules
- Integration with wearables / sleep data
- Deeper ML models (e.g. burnout/anxiety classifiers)
- Multilingual sentiment
- Mobile app and optional therapy referral network

---

# Conclusion

- MindScan shows how **AI** can help identify behavioral patterns linked to emotional stress
- Combines sentiment analysis and risk scoring with **wellness indicators** and ethical safeguards
- Prototype: journal analysis, dashboard, SQLite persistence, sample datasets, Streamlit Cloud–ready
- Suitable as an academic project and base for future extensions

---

<!-- _class: lead -->
# Thank You

**MindScan – AI Mental Wellness Indicator System**

**[Your Full Name]** | **[Roll No]**  
**[College Name]** | **[Academic Year]**

Questions?
