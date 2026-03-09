# MindScan – AI Mental Wellness Indicator System

An AI-assisted mental wellness indicator that analyzes journal text to produce sentiment scores and risk bands. **Not a medical diagnostic tool.**

## Quick Start (Local)

```bash
cd mindscan_streamlit_project
python -m venv venv
venv\Scripts\activate    # Windows
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Cloud Deployment

1. Push this project to a **GitHub** repository.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **New app**.
4. Set:
   - **Repository:** `your-username/your-repo`
   - **Branch:** `main` (or your default branch)
   - **Main file path:** `mindscan_streamlit_project/app.py`
5. Click **Deploy**.

> **Note:** On Streamlit Cloud the filesystem is ephemeral. SQLite data resets on redeploy. The app will use sample datasets when the database is empty.

## Project Structure

```
mindscan_streamlit_project/
├── app.py              # Entry point
├── requirements.txt
├── pages/
│   ├── journal_page.py
│   └── dashboard_page.py
├── services/
│   ├── sentiment_service.py
│   └── risk_engine.py
├── database/
│   ├── schema.sql
│   └── db_manager.py
├── data/               # Datasets
│   ├── sample_journal_entries.csv
│   ├── sentiment_training_data.csv
│   └── dashboard_sample_trend.csv
└── utils/
    └── data_loader.py
```

## Datasets

| File | Description |
|------|-------------|
| `sample_journal_entries.csv` | 15 labeled journal entries (Positive/Negative/Neutral) for demo and reference |
| `sentiment_training_data.csv` | Short labeled texts for sentiment model training |
| `dashboard_sample_trend.csv` | Sample weekly sentiment trend for dashboard when DB is empty |
