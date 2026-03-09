import streamlit as st
import pandas as pd
from database.db_manager import get_recent_journal_entries
from utils.data_loader import get_dashboard_sample_trend, get_sample_journal_entries
from services.wellness_service import get_weekly_insight

# Custom CSS for dashboard
st.markdown("""
<style>
    .metric-card { background: white; padding: 1.25rem; border-radius: 12px; border: 1px solid #e0e0e0;
        text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
    .risk-low { background: linear-gradient(135deg, #d4edda 0%, #c3e6cb); color: #155724; }
    .risk-moderate { background: linear-gradient(135deg, #fff3cd 0%, #ffeeba); color: #856404; }
    .risk-elevated { background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb); color: #721c24; }
    .insight-box { background: linear-gradient(135deg, #e8f4fd 0%, #d6ebf7); padding: 1rem; border-radius: 10px;
        border-left: 4px solid #2196F3; }
</style>
""", unsafe_allow_html=True)

st.title("📊 Emotional Dashboard")

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
    avg = 0.0
    sample = get_dashboard_sample_trend()
    if sample is not None:
        trend = sample[["day", "sentiment_score"]]
        latest_risk = sample["risk_band"].iloc[-1] if "risk_band" in sample.columns else "Moderate"
        avg = trend["sentiment_score"].mean()
    else:
        trend = pd.DataFrame({"Day": ["Mon","Tue","Wed","Thu","Fri"], "sentiment_score": [0.1,-0.2,-0.5,-0.1,0.2]})
        trend = trend.rename(columns={"Day": "day"})
        latest_risk = "Moderate"
        avg = trend["sentiment_score"].mean()

# Interactive tabs
tab1, tab2, tab3 = st.tabs(["📈 Overview", "📉 Trend Chart", "📝 Recent Entries"])

with tab1:
    # Key metrics in card layout
    risk_class = "risk-low" if latest_risk == "Low" else ("risk-moderate" if latest_risk == "Moderate" else "risk-elevated")
    r1, r2, r3 = st.columns(3)
    with r1:
        st.markdown(f'<div class="metric-card {risk_class}"><strong>Wellness</strong><br><span style="font-size:1.5rem;">{latest_risk}</span></div>', unsafe_allow_html=True)
    with r2:
        avg_val = round(avg, 2)
        st.markdown(f'<div class="metric-card"><strong>Avg. Sentiment</strong><br><span style="font-size:1.5rem;">{avg_val:.2f}</span><br><small>Higher = more positive</small></div>', unsafe_allow_html=True)
    with r3:
        n = len(entries) if entries else 0
        st.markdown(f'<div class="metric-card"><strong>Entries</strong><br><span style="font-size:1.5rem;">{n}</span><br><small>{"Your data" if entries else "Sample data"}</small></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<div class="insight-box">💡 {get_weekly_insight(entries or [], avg, latest_risk)}</div>', unsafe_allow_html=True)

with tab2:
    st.subheader("Sentiment over time")
    st.line_chart(trend.set_index("day"))
    # Optional: area chart for softer look - streamlit line_chart is fine

with tab3:
    if entries and len(entries) > 0:
        for i, (_, e) in enumerate(pd.DataFrame(entries, columns=["id","entry_text","sentiment_score","sentiment_label","created_at"]).iterrows()):
            lbl = e["sentiment_label"]
            icon = "🟢" if lbl == "Positive" else ("🔴" if lbl == "Negative" else "🟡")
            with st.expander(f"{icon} Entry {i+1} — {lbl}"):
                st.write(e["entry_text"][:200] + ("..." if len(str(e["entry_text"])) > 200 else ""))
                st.caption(f"Score: {e['sentiment_score']:.2f}")
    else:
        st.info("No entries yet. Go to **Journal** to add your first entry.")
        with st.expander("Sample entries (reference)"):
            sample_df = get_sample_journal_entries()
            if sample_df is not None:
                st.dataframe(sample_df[["entry_text", "sentiment_label"]].head(5), use_container_width=True)
            else:
                st.caption("Add journal entries to see your data here.")
