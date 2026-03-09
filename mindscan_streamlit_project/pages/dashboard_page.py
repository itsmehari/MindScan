import streamlit as st
import pandas as pd
from database.db_manager import get_recent_journal_entries
from utils.data_loader import get_dashboard_sample_trend, get_sample_journal_entries

st.header("Emotional Dashboard")

# Use DB entries for trend when available; else fall back to sample dataset
entries = get_recent_journal_entries(limit=14)
if entries and len(entries) >= 1:
    df = pd.DataFrame(
        entries,
        columns=["id", "entry_text", "sentiment_score", "sentiment_label", "created_at"],
    )
    df = df.sort_values("created_at", ascending=True)
    df["day"] = range(1, len(df) + 1)
    df["day"] = "Entry " + df["day"].astype(str)
    trend = df[["day", "sentiment_score"]]
    avg = df["sentiment_score"].mean()
    mn = df["sentiment_score"].min()
    latest_risk = "Low"
    if mn <= -0.5 or avg <= -0.5:
        latest_risk = "Elevated"
    elif avg < -0.2 or mn < -0.2:
        latest_risk = "Moderate"
else:
    sample = get_dashboard_sample_trend()
    if sample is not None:
        trend = sample[["day", "sentiment_score"]]
        latest_risk = sample["risk_band"].iloc[-1] if "risk_band" in sample.columns else "Moderate"
    else:
        trend = pd.DataFrame({"Day": ["Mon","Tue","Wed","Thu","Fri"], "sentiment_score": [0.1,-0.2,-0.5,-0.1,0.2]})
        trend = trend.rename(columns={"Day": "day"})
        latest_risk = "Moderate"

st.line_chart(trend.set_index("day"))
st.success(f"Current Risk: {latest_risk}")

# Sample dataset reference (expandable)
with st.expander("Sample Journal Dataset (for reference)"):
    sample_df = get_sample_journal_entries()
    if sample_df is not None:
        st.dataframe(sample_df[["entry_text", "sentiment_label"]].head(5), use_container_width=True)
    else:
        st.caption("Add journal entries to see your data here.")
