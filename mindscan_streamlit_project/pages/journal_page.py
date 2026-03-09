import streamlit as st
from services.sentiment_service import analyze_journal_text
from services.risk_engine import calculate_text_risk
from services.wellness_service import get_recommendations, get_support_resources
from database.db_manager import insert_journal_entry

st.header("Journal Sentiment Analysis")

journal = st.text_area("Write today's journal entry", placeholder="e.g. I feel tired and stressed today. Couldn't sleep well...")

if st.button("Analyze"):
    if journal.strip():
        sentiment = analyze_journal_text(journal)
        risk = calculate_text_risk(sentiment)
        insert_journal_entry(
            journal.strip(),
            sentiment["score"],
            sentiment["label"],
        )

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Sentiment", sentiment["label"], f"{sentiment['score']:.2f}")
        with col2:
            risk_color = {"Low": "🟢", "Moderate": "🟡", "Elevated": "🔴"}.get(risk, risk)
            st.metric("Wellness Indicator", risk, risk_color)

        st.divider()
        st.subheader("Suggestions for you")
        for rec in get_recommendations(risk, sentiment["label"]):
            st.markdown(f"- {rec}")

        if risk == "Elevated":
            with st.expander("📞 Support resources (you are not alone)"):
                for r in get_support_resources():
                    st.markdown(f"**{r['name']}** – {r['value']}")
                    st.markdown(f"[Link]({r['url']})")

        st.success("Entry saved. Check the Dashboard to see your trend.")
    else:
        st.warning("Please enter text.")
