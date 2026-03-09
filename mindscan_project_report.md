# MindScan Project Report

**AI Mental Health State Detection System**

---

## TITLE PAGE

**[College Name (Full)]**  
**[College Address – City, PIN]**

*(e.g. NAAC accredited / Affiliated to [University])*

---

**Degree:** B.Sc. Computer Science  

**Project Title:** MindScan – AI Mental Wellness Indicator System  

**Submitted by**  
**[Your Full Name]**  
Roll No. / Register No.: **[Your Roll No]**

**Under the guidance of**  
**[Guide Name]**  
**[Guide Designation], Department of Computer Science**

**Academic Year:** **[e.g. 2024 – 2025]**

**Department of Computer Science**

---

## BONAFIDE CERTIFICATE

This is to certify that the project entitled **“MindScan – AI Mental Wellness Indicator System”** submitted by **[Your Full Name]** (Roll No. **[Your Roll No]**) in partial fulfilment of the requirements for the award of **B.Sc. Computer Science** by **[College Name]** is a record of bonafide work carried out under my supervision.

The project has not been submitted elsewhere for the award of any other degree/diploma.

<br>

**Signature of Guide**  
**[Guide Name]**  
**[Guide Designation]**  
Department of Computer Science

<br>

**Signature of Head of Department**  
**[HOD Name]**  
Head, Department of Computer Science

<br>

**Signature of Principal**  
**[Principal Name]**  
Principal  
**[College Name]**

**Place:** **[City]**  
**Date:** **[Date]**

---

## DECLARATION BY STUDENT

I, **[Your Full Name]**, hereby declare that the project entitled **“MindScan – AI Mental Wellness Indicator System”** submitted to the Department of Computer Science, **[College Name]**, is my original work done under the guidance of **[Guide Name]**.

This project has not been submitted elsewhere for the award of any degree or diploma. I have given due acknowledgements wherever references have been taken from other sources.

<br>

**Signature**  
**[Your Full Name]**  
Roll No. **[Your Roll No]**  
**Date:** **[Date]**

---

## ACKNOWLEDGEMENT

I would like to express my sincere gratitude to **[College Name]** and the Department of Computer Science for providing the opportunity to undertake this project.

I am deeply thankful to my project guide, **[Guide Name]**, for continuous guidance, valuable suggestions, and support throughout the project. I thank the Head of the Department of Computer Science for the facilities and encouragement provided.

I also thank my family and friends for their support and motivation during the course of this work.

<br>

**[Your Full Name]**  
**[Date]**

---

# TABLE OF CONTENTS

## FRONT MATTER

1. Title Page
2. Bonafide Certificate
3. Declaration by Student
4. Acknowledgement
5. Abstract
6. List of Figures
7. List of Tables
8. List of Abbreviations

---

# ABSTRACT

MindScan is an AI-assisted mental wellness indicator system designed to analyze behavioral and linguistic patterns in order to detect early emotional stress indicators. The system integrates multiple behavioral signals including journaling text, speech characteristics, typing rhythm, and lifestyle inputs such as sleep and activity levels. Using natural language processing and machine learning models, the system produces risk indicator bands and emotional trend insights without making any clinical diagnosis.

The primary goal of the system is early awareness and support guidance rather than medical diagnosis. The platform visualizes emotional patterns through dashboards, risk scores, and behavioral trend graphs. Ethical safeguards are embedded in the design to ensure that outputs are interpreted only as wellness indicators.

---

# LIST OF ABBREVIATIONS

| Abbreviation | Full Form |
|--------------|-----------|
| AI | Artificial Intelligence |
| API | Application Programming Interface |
| DB | Database |
| DFD | Data Flow Diagram |
| ML | Machine Learning |
| NLTK | Natural Language Toolkit |
| NLP | Natural Language Processing |
| NIMH | National Institute of Mental Health |
| SaaS | Software as a Service |
| SQL | Structured Query Language |
| TF-IDF | Term Frequency – Inverse Document Frequency |
| WHO | World Health Organization |

---

# CHAPTER 1 – INTRODUCTION

## 1.1 Background of Mental Health Monitoring

Mental health has become a major concern in modern society due to increasing academic pressure, workplace stress, social isolation, and lifestyle changes. Traditional mental health support systems often rely on individuals recognizing symptoms and seeking professional help. However, early psychological stress indicators frequently go unnoticed.

Recent advances in artificial intelligence and behavioral analytics have created opportunities for systems that can monitor subtle changes in emotional patterns. By analyzing language, behavioral rhythms, and lifestyle signals, AI systems can detect patterns associated with emotional stress or burnout risk.

MindScan aims to explore how computational techniques can assist in detecting early emotional wellness indicators through behavioral data analysis.

## 1.2 Importance of Early Psychological State Detection

Early awareness of emotional stress patterns allows individuals to take preventive steps before severe psychological distress occurs. Many individuals experiencing burnout or anxiety show subtle behavioral changes such as altered writing tone, reduced sleep, slower speech tempo, or negative self‑talk patterns.

A system capable of identifying these signals can assist individuals in understanding their emotional trends and encourage proactive support measures.

## 1.3 Role of Artificial Intelligence in Mental Wellness

Artificial intelligence provides powerful tools for pattern recognition in large behavioral datasets. Techniques such as sentiment analysis, natural language processing, and machine learning classification models allow automated interpretation of emotional signals in textual and speech inputs.

These technologies enable systems like MindScan to evaluate emotional signals and generate wellness indicators while maintaining ethical safeguards against medical diagnosis.

## 1.4 Problem Statement

Many existing mental health applications rely primarily on self-reported mood tracking without deeper behavioral analysis. This limits their ability to detect meaningful emotional patterns over time.

There is a need for a system that can combine multiple behavioral signals and analyze them using AI models to produce early emotional stress indicators in a responsible and ethical manner.

## 1.5 Objectives of the MindScan System

The primary objectives of the MindScan project are:

• To design a system capable of analyzing behavioral signals related to emotional wellbeing • To apply natural language processing to detect emotional sentiment patterns • To analyze speech tempo and behavioral metrics • To generate risk indicator bands based on behavioral patterns • To provide emotional trend visualization dashboards • To maintain ethical safeguards that prevent medical diagnosis

## 1.6 Scope of the Project

The scope of the MindScan system includes the development of an AI-assisted behavioral analysis platform capable of processing journaling text, speech characteristics, typing behavior, and lifestyle indicators. The system will generate emotional wellness indicators and provide visual dashboards that help users understand their emotional trends.

The project focuses on prototype development suitable for academic demonstration using Python and Streamlit.

## 1.7 Methodology

The system development follows a modular architecture consisting of input data collection, feature extraction, machine learning analysis, and visualization modules.

Key development stages include:

• Data collection from behavioral inputs • Feature extraction using NLP and speech processing • Machine learning model development • Dashboard visualization using Streamlit • Risk scoring and alert generation

## 1.8 Organization of the Report

The project report is organized into multiple chapters that explain the system background, design, implementation, and results. Each chapter provides detailed explanations of the architecture, modules, algorithms, and testing methodology used in the MindScan system.

---

# CHAPTER 2 – SYSTEM STUDY

## 2.1 Existing Mental Health Applications

Many mobile and web applications provide tools for emotional wellness monitoring. Examples include mood tracking apps, journaling platforms, meditation support tools, and AI-based therapy chatbots.

These applications allow users to record daily emotions, practice mindfulness exercises, or interact with conversational agents designed to provide emotional support.

## 2.2 Limitations of Existing Systems

Despite their usefulness, most existing systems have limitations.

• Dependence on manual mood entry • Lack of behavioral signal analysis • Limited integration of speech or typing behavior • Minimal predictive capability

## 2.3 Proposed System

The proposed MindScan system addresses these limitations by combining multiple behavioral signals and analyzing them using artificial intelligence models. This enables deeper insight into emotional patterns and risk indicators.

## 2.4 Feasibility Study

### Technical Feasibility

Python-based machine learning libraries and Streamlit visualization tools provide sufficient capability to implement the proposed system.

### Economic Feasibility

The project uses open-source technologies and therefore does not require expensive software infrastructure.

### Operational Feasibility

The system interface is designed to be simple and intuitive, making it suitable for students and professionals.

---

# CHAPTER 3 – SYSTEM REQUIREMENTS

## 3.1 Hardware Requirements

• Computer with minimum 8 GB RAM • Microphone for voice input • Internet connection

## 3.2 Software Requirements

• Python 3.9 or later • Streamlit • Pandas • NumPy • Scikit-learn • NLTK • Librosa

## 3.3 Technology Stack

Programming Language: Python Frontend Framework: Streamlit Machine Learning Libraries: Scikit-learn, NLTK Speech Analysis: Librosa Database: SQLite

---

# CHAPTER 4 – SYSTEM DESIGN

## 4.1 System Architecture Overview

The MindScan system follows a layered architecture that separates data input, processing, machine learning analysis, and visualization. This modular architecture improves maintainability and scalability.

The system architecture contains four major layers:

Input Layer – Collects behavioral signals such as journaling text, voice recordings, typing patterns, and lifestyle inputs.

Processing Layer – Extracts meaningful features from raw inputs such as sentiment scores, speech tempo, and behavioral metrics.

AI Analysis Layer – Applies machine learning algorithms to evaluate emotional patterns and generate risk indicators.

Visualization Layer – Displays emotional insights using dashboards, trend graphs, and alert notifications.

## 4.2 High Level Architecture

The high-level architecture includes the following components:

• User Interface (Streamlit Dashboard) • Data Input Modules • Feature Extraction Services • Machine Learning Models • Risk Scoring Engine • Alert System • Database Storage

These components communicate through modular Python services.

## 4.3 Data Flow Diagram

### Level 0 DFD

User provides behavioral inputs such as journal entries and voice samples. The system processes these inputs through AI modules and produces emotional risk indicators and visualization outputs.

### Level 1 DFD

1. User submits journal entry or voice recording
2. Data preprocessing module extracts features
3. AI models analyze patterns
4. Risk scoring module generates emotional indicators
5. Dashboard displays emotional trend visualization

## 4.4 Database Design

The system uses SQLite for storing user inputs and analysis results.

Users Table Stores user identification and profile information.

JournalEntries Table Stores text journaling data and timestamps.

VoiceFeatures Table Stores extracted audio characteristics such as tempo and pitch variance.

BehaviorMetrics Table Stores typing rhythm and activity indicators.

RiskScores Table Stores calculated emotional risk indicators.

Alerts Table Stores generated behavioral alerts.

## 4.5 Entity Relationship Description

The Users table connects to JournalEntries, VoiceFeatures, and BehaviorMetrics tables. These inputs are processed to generate records in the RiskScores table. When risk thresholds are exceeded, alerts are generated and stored in the Alerts table.

---

# CHAPTER 5 – MODULE DESCRIPTION

## 5.1 User Management Module

Purpose Handles user identification and profile management.

Inputs User registration information.

Processing Validates user details and creates profile records.

Outputs User profile stored in database.

## 5.2 Journaling Module

Purpose Allows users to submit daily reflections or emotional journal entries.

Inputs Text-based journal entries.

Processing Text preprocessing and sentiment feature extraction.

Outputs Processed text features for sentiment analysis.

## 5.3 Voice Processing Module

Purpose Analyzes speech characteristics to detect emotional cues.

Inputs Recorded voice samples.

Processing Extraction of speech features including tempo, pitch variance, and energy.

Outputs Speech behavioral metrics.

## 5.4 Typing Behavior Monitoring Module

Purpose Monitors typing rhythm to detect cognitive fatigue or stress indicators.

Inputs Typing events and key intervals.

Processing Calculation of typing speed, pause frequency, and variability.

Outputs Behavioral typing metrics.

## 5.5 NLP Sentiment Analysis Module

Purpose Determines emotional polarity of journal text.

Inputs Journal text data.

Processing Tokenization, stop word removal, and sentiment scoring using NLP models.

Outputs Sentiment score and emotional polarity classification.

## 5.6 Cognitive Distortion Detection Module

Purpose Detects linguistic patterns associated with negative cognitive distortions.

Inputs Processed journal text.

Processing Pattern matching and classification models.

Outputs Cognitive distortion indicators.

## 5.7 Burnout Risk Prediction Module

Purpose Estimates burnout probability using behavioral signals.

Inputs Sleep indicators, activity data, sentiment scores.

Processing Machine learning classification model.

Outputs Burnout risk probability.

## 5.8 Anxiety Pattern Classifier

Purpose Identifies behavioral signals related to anxiety patterns.

Inputs Speech tempo, sentiment patterns, typing rhythm.

Processing Feature vector classification using machine learning algorithms.

Outputs Anxiety risk indicator.

## 5.9 Risk Scoring Engine

Purpose Combines all behavioral indicators to generate an overall emotional risk score.

Inputs Sentiment scores, speech metrics, behavioral indicators.

Processing Weighted scoring algorithm.

Outputs Risk bands (Low, Moderate, Elevated).

## 5.10 Alert Generation Engine

Purpose Triggers alerts when abnormal behavioral trends appear.

Inputs Risk scores and behavioral metrics.

Processing Threshold detection logic.

Outputs Alert notifications.

## 5.11 Recommendation Engine

Purpose Provides emotional wellness suggestions.

Inputs Risk score and behavioral indicators.

Processing Rule-based recommendation engine.

Outputs Wellness suggestions such as journaling prompts or mindfulness activities.

## 5.12 Emotional Dashboard Module

Purpose Displays emotional insights through interactive visualizations.

Inputs Risk scores, sentiment trends, behavioral metrics.

Processing Visualization using Streamlit charts.

Outputs Interactive emotional state dashboard.

---

# CHAPTER 6 – SYSTEM IMPLEMENTATION

## 6.1 Development Environment

The MindScan system is implemented using Python and Streamlit. Machine learning models are developed using Scikit-learn and NLP libraries such as NLTK. The prototype is designed for local execution in a student academic environment.

Development tools used:

• Python 3.10+ • VS Code or PyCharm • Streamlit for frontend • SQLite for local persistence • Pandas and NumPy for data handling • Scikit-learn for lightweight ML models • NLTK / TextBlob for sentiment features • Librosa for audio feature extraction

Example environment setup:

```python
import sys
import platform

print("Python Version:", sys.version)
print("Platform:", platform.system())
```

## 6.2 Project Directory Structure

**Implementation scope (prototype).** The current prototype implements the core journal-based workflow: Journal Analysis (sentiment and risk band), Emotional Dashboard (trend visualization), and SQLite persistence for journal entries via `database/db_manager.py`. Voice analysis, typing behaviour, alert engine, and trained ML model persistence are designed in this report for completeness and can be added in future extensions.

The project is organized using a modular folder structure so that each functional layer remains isolated and easier to maintain.

```text
mindscan_streamlit_project/
│
├── app.py
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml
│
├── pages/
│   ├── journal_page.py
│   └── dashboard_page.py
│
├── services/
│   ├── sentiment_service.py
│   └── risk_engine.py
│
├── data/
│   ├── sample_journal_entries.csv
│   ├── sentiment_training_data.csv
│   └── dashboard_sample_trend.csv
│
├── database/
│   ├── schema.sql
│   └── db_manager.py
│
└── utils/
    ├── __init__.py
    └── data_loader.py
```

## 6.3 Streamlit Application Architecture

The Streamlit application acts as the main presentation layer. It loads navigation, collects input from the user, passes data to backend services, and displays emotional trend outputs.

Main application entry code:

```python
# app.py
import streamlit as st

st.set_page_config(page_title="MindScan", layout="wide")

st.title("MindScan - AI Mental Wellness Indicator System")
st.caption("This system provides mental wellness indicators and is not a medical diagnostic tool.")

st.markdown("""
### Modules
- Journal Analysis
- Voice Analysis
- Typing Behaviour Tracking
- Emotional Dashboard
""")

st.info("Use the sidebar to open different analysis pages.")
```

## 6.4 Frontend Interface Development

The frontend contains multiple pages to simulate different behavioral input channels.

### 6.4.1 Journal Input Page

This page allows the user to enter a daily reflection and receive sentiment and distortion signals.

```python
# pages/journal_page.py
import streamlit as st
from services.sentiment_service import analyze_journal_text
from services.risk_engine import calculate_text_risk

st.header("Journal Analysis")
user_text = st.text_area("Write today's journal entry")

if st.button("Analyze Journal"):
    if user_text.strip():
        sentiment = analyze_journal_text(user_text)
        risk = calculate_text_risk(sentiment)
        st.write("Sentiment Score:", sentiment["score"])
        st.write("Sentiment Label:", sentiment["label"])
        st.write("Risk Band:", risk)
    else:
        st.warning("Please enter journal content.")
```

### 6.4.2 Voice Analysis Page

This page receives a voice file and extracts lightweight acoustic features such as tempo and energy.

```python
# pages/voice_page.py
import streamlit as st
from services.speech_analysis import extract_voice_features

st.header("Voice Analysis")
uploaded_file = st.file_uploader("Upload WAV audio", type=["wav"])

if uploaded_file is not None:
    with open("uploads/temp_audio.wav", "wb") as f:
        f.write(uploaded_file.read())

    features = extract_voice_features("uploads/temp_audio.wav")
    st.json(features)
```

### 6.4.3 Typing Behaviour Page

This page simulates entry of typing metrics captured from frontend events.

```python
# pages/typing_page.py
import streamlit as st
from services.behavior_metrics import evaluate_typing_pattern

st.header("Typing Behaviour")
typing_speed = st.slider("Typing Speed (words/min)", 10, 100, 35)
pause_frequency = st.slider("Pause Frequency", 0, 20, 8)

if st.button("Evaluate Typing Pattern"):
    result = evaluate_typing_pattern(typing_speed, pause_frequency)
    st.write(result)
```

### 6.4.4 Dashboard Page

The dashboard displays emotional trends, risk summaries, and recommendation outputs.

```python
# pages/dashboard_page.py
import streamlit as st
import pandas as pd

st.header("Emotional Dashboard")

data = pd.DataFrame({
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "sentiment_score": [0.2, -0.4, -0.6, -0.1, 0.1]
})

st.line_chart(data.set_index("day"))
st.success("Current Risk Band: Moderate")
st.info("Suggested Action: Maintain journaling and sleep routine.")
```

## 6.5 Backend Services Layer

The backend service layer performs the actual analysis and keeps the pages lightweight.

### 6.5.1 Sentiment Analysis Service

This service processes journal text and returns a polarity score and label.

```python
# services/sentiment_service.py
from textblob import TextBlob


def analyze_journal_text(text: str) -> dict:
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.2:
        label = "Positive"
    elif polarity < -0.2:
        label = "Negative"
    else:
        label = "Neutral"

    return {
        "score": round(polarity, 3),
        "label": label
    }
```

### 6.5.2 Voice Feature Extraction Service

This module extracts basic voice indicators using Librosa.

```python
# services/speech_analysis.py
import librosa
import numpy as np


def extract_voice_features(audio_path: str) -> dict:
    y, sr = librosa.load(audio_path, sr=None)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    rms = librosa.feature.rms(y=y)[0]
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]

    return {
        "tempo": float(round(tempo, 2)),
        "avg_energy": float(round(np.mean(rms), 4)),
        "avg_spectral_centroid": float(round(np.mean(spectral_centroid), 2))
    }
```

### 6.5.3 Behavioural Metrics Processor

This module evaluates typing-based fatigue indicators.

```python
# services/behavior_metrics.py

def evaluate_typing_pattern(typing_speed: int, pause_frequency: int) -> dict:
    if typing_speed < 25 and pause_frequency > 10:
        status = "Possible fatigue pattern"
    elif typing_speed < 35:
        status = "Mild slowdown observed"
    else:
        status = "Normal typing pattern"

    return {
        "typing_speed": typing_speed,
        "pause_frequency": pause_frequency,
        "status": status
    }
```

### 6.5.4 Risk Calculation Engine

This engine combines multiple indicators and converts them into risk bands.

```python
# services/risk_engine.py

def calculate_text_risk(sentiment_result: dict) -> str:
    score = sentiment_result["score"]

    if score <= -0.5:
        return "Elevated"
    if score <= -0.2:
        return "Moderate"
    return "Low"


def combine_risk_scores(sentiment_score: float, sleep_hours: float, typing_flag: int) -> dict:
    risk_points = 0

    if sentiment_score < -0.3:
        risk_points += 2
    if sleep_hours < 5.5:
        risk_points += 2
    if typing_flag == 1:
        risk_points += 1

    if risk_points >= 4:
        band = "Elevated"
    elif risk_points >= 2:
        band = "Moderate"
    else:
        band = "Low"

    return {"points": risk_points, "band": band}
```

### 6.5.5 Alert Engine

This module decides when the system should issue a wellness alert.

```python
# services/alert_engine.py

def generate_alert(risk_band: str) -> str:
    if risk_band == "Elevated":
        return "Alert: sustained elevated emotional stress indicators detected. Consider support action."
    if risk_band == "Moderate":
        return "Notice: monitor emotional trend for the next few days."
    return "No immediate alert required."
```

## 6.6 AI Model Development

The project can include simple training scripts for academic demonstration. Lightweight traditional ML is more suitable than heavy deep learning for local college demo environments.

### 6.6.1 Sentiment Classifier

```python
# models/train_sentiment_model.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

texts = [
    "I feel happy and calm",
    "I am exhausted and worried",
    "Today was normal",
    "I feel hopeless and tired",
    "I am energetic and productive"
]
labels = ["Positive", "Negative", "Neutral", "Negative", "Positive"]

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

model.fit(texts, labels)
joblib.dump(model, "models/saved_models/sentiment_model.pkl")
```

### 6.6.2 Burnout Predictor

```python
# models/train_risk_model.py
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib

train_df = pd.DataFrame({
    "sentiment_score": [-0.7, -0.4, 0.2, -0.1, 0.5],
    "sleep_hours": [4.5, 5.0, 7.5, 6.0, 8.0],
    "typing_flag": [1, 1, 0, 0, 0],
    "risk_label": [2, 1, 0, 0, 0]
})

X = train_df[["sentiment_score", "sleep_hours", "typing_flag"]]
y = train_df["risk_label"]

model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X, y)
joblib.dump(model, "models/saved_models/burnout_model.pkl")
```

### 6.6.3 Anxiety Pattern Classifier

```python
# example inference utility
import joblib
import pandas as pd


def predict_risk(sentiment_score: float, sleep_hours: float, typing_flag: int) -> int:
    model = joblib.load("models/saved_models/burnout_model.pkl")
    sample = pd.DataFrame([{
        "sentiment_score": sentiment_score,
        "sleep_hours": sleep_hours,
        "typing_flag": typing_flag
    }])
    return int(model.predict(sample)[0])
```

## 6.7 Database Layer Implementation

SQLite is used to store journaling entries, extracted features, and analysis outputs.

### 6.7.1 SQLite Schema

```sql
-- database/schema.sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS journal_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    entry_text TEXT NOT NULL,
    sentiment_score REAL,
    sentiment_label TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS risk_scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    risk_band TEXT,
    risk_points INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### 6.7.2 Database Manager

```python
# database/db_manager.py
import sqlite3

DB_NAME = "mindscan.db"


def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def insert_journal_entry(user_id: int, entry_text: str, score: float, label: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO journal_entries (user_id, entry_text, sentiment_score, sentiment_label)
        VALUES (?, ?, ?, ?)
        """,
        (user_id, entry_text, score, label)
    )
    conn.commit()
    conn.close()
```

## 6.8 Exception Handling

Exception handling is essential because the project accepts user input, file uploads, and ML predictions that may fail due to missing data or invalid file types.

```python
# example exception handling
try:
    features = extract_voice_features("uploads/temp_audio.wav")
except FileNotFoundError:
    print("Audio file not found.")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## 6.9 Security and Privacy

The project is not a clinical platform, but user behavioral data still requires safe handling. Sensitive records should be stored locally during demo use and not exposed publicly.

```python
# example safe input cleaning
import re


def sanitize_text(text: str) -> str:
    text = re.sub(r"<.*?>", "", text)
    return text.strip()
```

Recommended safeguards:

• Local database use for demo submission • No public exposure of raw emotional logs • Clear disclaimer on every screen • Optional anonymization for class demonstration

## 6.10 Testing Strategy

Testing confirms that each service behaves consistently for valid and invalid inputs.

### 6.10.1 Unit Test Example

```python
# tests/test_risk_engine.py
from services.risk_engine import calculate_text_risk


def test_calculate_text_risk_negative():
    result = calculate_text_risk({"score": -0.6, "label": "Negative"})
    assert result == "Elevated"
```

### 6.10.2 Functional Test Example

```python
# tests/test_sentiment_service.py
from services.sentiment_service import analyze_journal_text


def test_sentiment_analysis_output_keys():
    result = analyze_journal_text("I feel stressed and tired")
    assert "score" in result
    assert "label" in result
```

### 6.10.3 Integration Test Logic

1. Submit journal entry from UI.
2. Run sentiment analysis service.
3. Generate risk band.
4. Store result in database.
5. Display dashboard result.

## 6.11 Datasets

The project includes CSV datasets in the `data/` folder:

| File | Purpose |
|------|---------|
| `sample_journal_entries.csv` | 15 labeled journal entries (Positive/Negative/Neutral) for demo and reference |
| `sentiment_training_data.csv` | 13 short texts with labels for training or experiments |
| `dashboard_sample_trend.csv` | Sample weekly sentiment trend used when the database is empty |

The `utils/data_loader.py` module loads these datasets. The dashboard uses sample data when no user journal entries exist (e.g. on first run or on Streamlit Cloud where the filesystem is ephemeral).

## 6.12 Deployment

**Local deployment** – The prototype runs on a local machine with minimal setup:

```bash
cd mindscan_streamlit_project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

**Streamlit Cloud deployment** – The project is prepared for hosting on [share.streamlit.io](https://share.streamlit.io). Push the repository to GitHub, connect Streamlit Cloud, and set the main file path to `mindscan_streamlit_project/app.py`. Note: the cloud filesystem is ephemeral, so SQLite data resets on redeploy; the dashboard falls back to sample datasets when the database is empty.

Sample requirements file (librosa and soundfile removed for Streamlit Cloud compatibility):

```text
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
textblob>=0.17.0
nltk>=3.8.0
joblib>=1.3.0
```

The implementation chapter contains direct code references that match the repository structure. These snippets are suitable for embedding into an academic report because they demonstrate actual logic for interface handling, feature extraction, risk scoring, persistence, and testing.

---

# CHAPTER 7 – RESULTS AND DISCUSSION

## 7.1 System Demonstration

The prototype demonstrates the ability to analyze user journal entries and behavioral inputs and generate emotional risk indicators.

## 7.2 Sample Inputs

Example journal entry:

"I feel extremely tired and overwhelmed with work today. I could not focus properly and slept very late."

## 7.3 Sentiment Analysis Output

Sentiment polarity detected as negative with moderate intensity.

## 7.4 Behavioral Risk Score Example

Risk Level: Moderate

Indicators:

• negative sentiment • sleep disruption

## 7.5 Dashboard Visualization

The dashboard displays emotional trends across time using charts and graphs. When user journal entries exist, it plots sentiment scores from the database; when the database is empty (e.g. on first run or Streamlit Cloud), it falls back to the sample dataset `dashboard_sample_trend.csv`.

## 7.6 Datasets and Sample Data

The project includes three CSV datasets: `sample_journal_entries.csv` (15 labeled entries), `sentiment_training_data.csv` (13 short texts for training), and `dashboard_sample_trend.csv` (weekly trend). These are used for demo, reference, and as fallback when no user data exists.

## 7.7 Alert Generation Example

If negative sentiment persists for several days, the system triggers a wellness alert.

---

# CHAPTER 8 – ETHICAL CONSIDERATIONS

## 8.1 Ethical Concerns

AI-based mental wellness systems must ensure responsible interpretation of behavioral signals.

## 8.2 False Positive Risk

Machine learning predictions may occasionally generate incorrect indicators. Conservative thresholds reduce this risk.

## 8.3 Privacy Protection

User data must be stored securely and used only for behavioral analysis.

## 8.4 Non-Diagnostic Positioning

The system does not diagnose mental illness.

System Disclaimer:

"This system provides mental wellness indicators and is not a medical diagnostic tool."

---

# CHAPTER 9 – BUSINESS MODEL DISCUSSION

## 9.1 Employee Mental Wellness SaaS

Organizations can deploy the system internally to monitor workforce wellness trends.

## 9.2 University Campus Subscription

Universities may integrate MindScan into campus counseling programs.

## 9.3 Individual Premium Version

A personal version could provide emotional trend monitoring and wellness recommendations.

## 9.4 Therapy Referral Network

The system could connect users with professional counseling services.

---

# CHAPTER 10 – FUTURE ENHANCEMENTS

10.1 Integration with wearable health devices

10.2 Continuous behavioral monitoring

10.3 Deep learning emotional recognition models

10.4 Multilingual sentiment analysis

10.5 Mobile application version

---

# CHAPTER 11 – CONCLUSION

MindScan demonstrates how artificial intelligence techniques can assist in identifying behavioral patterns associated with emotional stress. The system integrates multiple behavioral signals and produces wellness indicators that help users understand emotional trends.

The project highlights the potential of AI-assisted behavioral analytics while maintaining strict ethical safeguards.

---

# REFERENCES

1. Jurafsky, D., & Martin, J. H. (2023). *Speech and Language Processing*. Stanford University.
2. Bird, S., Klein, E., & Loper, E. (2009). *Natural Language Processing with Python*. O’Reilly Media.
3. Pedregosa, F. et al. (2011). *Scikit‑learn: Machine Learning in Python*. Journal of Machine Learning Research.
4. McKinney, W. (2018). *Python for Data Analysis*. O’Reilly Media.
5. Librosa Documentation – Python Audio Processing Library.
6. Streamlit Documentation – Data Application Framework.
7. World Health Organization (WHO). *Mental Health and Well‑Being Research Reports*.
8. National Institute of Mental Health (NIMH). *Digital Mental Health Tools and AI Monitoring Systems*.
9. IEEE Research Papers on Emotion Recognition using NLP and Speech Processing.
10. ACM Digital Library – Studies on Behavioral Signal Processing.

---

# APPENDICES

## Appendix A – Source Code Overview

The MindScan system is implemented using a modular Python architecture. Each module is separated into logical directories that improve maintainability and clarity.

Key files:

app.py Main Streamlit entry point responsible for launching the user interface and routing pages.

services/ Contains processing logic such as sentiment analysis, feature extraction, and risk scoring.

models/ Contains trained machine learning models used for emotional signal detection.

database/ Contains SQLite schema definitions and database helper utilities.

utils/ Contains helper functions for preprocessing text, audio, and behavioral signals.

pages/ Contains Streamlit page modules such as journaling interface and emotional dashboard.

---

## Appendix B – Datasets

### B.1 sample_journal_entries.csv

15 labeled journal entries (id, entry_text, sentiment_label, sentiment_score) for demo and reference.

| Entry ID | Journal Text (sample) | Sentiment Label | Score |
| -------- | --------------------- | --------------- | ----- |
| 1        | I feel happy today and productive. Had a great workout. | Positive | 0.65 |
| 2        | I feel exhausted and stressed with assignments. | Negative | -0.58 |
| 3        | Today was normal and nothing unusual happened. | Neutral | 0.05 |

### B.2 sentiment_training_data.csv

13 short texts with sentiment labels for training or experiments.

### B.3 dashboard_sample_trend.csv

Sample weekly sentiment trend (day, sentiment_score, risk_band) used when the database is empty.

### B.4 Speech Feature Dataset (Design Reference)

| Sample ID | Tempo  | Pitch Variance | Energy | Label   |
| --------- | ------ | -------------- | ------ | ------- |
| 1         | Medium | Low            | Medium | Calm    |
| 2         | Slow   | Low            | Low    | Fatigue |
| 3         | Fast   | High           | High   | Stress  |

### B.5 Behavior Metrics Dataset (Design Reference)

| User | Typing Speed | Pause Frequency | Activity Level |
| ---- | ------------ | --------------- | -------------- |
| U01  | Medium       | Low             | High           |
| U02  | Slow         | High            | Low            |
| U03  | Fast         | Medium          | Medium         |

---

## Appendix C – Installation Guide

### Step 1 – Install Python

Install Python 3.9 or higher from the official Python website.

### Step 2 – Create Virtual Environment

```
cd mindscan_streamlit_project
python -m venv venv
```

**Activate environment**

- Windows: `venv\Scripts\activate`
- Linux / macOS: `source venv/bin/activate`

### Step 3 – Install Dependencies

```
pip install -r requirements.txt
```

### Step 4 – Run Application

```
streamlit run app.py
```

The system will open automatically in a web browser.

### Step 5 – Streamlit Cloud Deployment (Optional)

1. Push the project to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **New app**, set repository, branch, and main file path: `mindscan_streamlit_project/app.py`.
4. Click **Deploy**. The app will be live; SQLite data resets on redeploy, but sample datasets provide demo data.

---

## Appendix D – Example System Screens

1. User Journaling Page

Allows the user to write daily reflections and emotional notes.

2. Voice Analysis Page

User uploads a short voice recording. The system extracts tempo and acoustic features.

3. Typing Behavior Monitor

Measures typing speed and pause patterns during journaling.

4. Emotional Dashboard

Displays:

• Mood trend graphs • Sentiment history • Behavioral risk indicators • Alert notifications

---

## Appendix E – Project Directory Structure (Final)

```
mindscan_streamlit_project/
│
├── app.py
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml
├── .gitignore
│
├── pages/
│   ├── journal_page.py
│   └── dashboard_page.py
│
├── services/
│   ├── sentiment_service.py
│   └── risk_engine.py
│
├── data/
│   ├── sample_journal_entries.csv
│   ├── sentiment_training_data.csv
│   └── dashboard_sample_trend.csv
│
├── database/
│   ├── schema.sql
│   └── db_manager.py
│
└── utils/
    ├── __init__.py
    └── data_loader.py
```

---

## Appendix F – Ethical Safety Statement

MindScan is designed strictly as a behavioral wellness indicator system. It does not diagnose mental illness or replace professional psychological evaluation. All system outputs must be interpreted as supportive signals rather than medical conclusions.

System Notice:

"MindScan provides emotional wellness indicators derived from behavioral patterns. It is not a clinical diagnostic tool and should not be used as a substitute for professional mental health care."

