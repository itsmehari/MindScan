"""Load datasets for MindScan – demo and training."""
import os
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def get_sample_journal_entries():
    """Load sample journal entries CSV. Returns DataFrame or None if not found."""
    path = os.path.join(DATA_DIR, "sample_journal_entries.csv")
    if os.path.exists(path):
        return pd.read_csv(path)
    return None


def get_sentiment_training_data():
    """Load sentiment training data. Returns DataFrame or None if not found."""
    path = os.path.join(DATA_DIR, "sentiment_training_data.csv")
    if os.path.exists(path):
        return pd.read_csv(path)
    return None


def get_dashboard_sample_trend():
    """Load sample sentiment trend for dashboard. Returns DataFrame or None."""
    path = os.path.join(DATA_DIR, "dashboard_sample_trend.csv")
    if os.path.exists(path):
        return pd.read_csv(path)
    return None
