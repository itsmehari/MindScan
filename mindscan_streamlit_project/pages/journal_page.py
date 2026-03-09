import streamlit as st
from services.sentiment_service import analyze_journal_text
from services.risk_engine import calculate_text_risk
from database.db_manager import insert_journal_entry

st.header("Journal Sentiment Analysis")

journal = st.text_area("Write today's journal entry")

if st.button("Analyze"):
    if journal.strip():
        sentiment = analyze_journal_text(journal)
        risk = calculate_text_risk(sentiment)
        insert_journal_entry(
            journal.strip(),
            sentiment["score"],
            sentiment["label"],
        )
        st.write("Sentiment:", sentiment)
        st.write("Risk Band:", risk)
        st.success("Entry saved.")
    else:
        st.warning("Please enter text.")
