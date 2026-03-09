import streamlit as st
from database.db_manager import init_db

# Ensure database and tables exist
init_db()

st.set_page_config(page_title="MindScan", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for a polished look
st.markdown("""
<style>
    .welcome-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .action-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        text-align: center;
        transition: all 0.2s;
        cursor: pointer;
        height: 140px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .action-card:hover {
        border-color: #6b4ce6;
        box-shadow: 0 4px 12px rgba(107, 76, 230, 0.15);
    }
    .action-card h3 { margin: 0 0 0.5rem 0; font-size: 1.2rem; color: #333; }
    .action-card p { margin: 0; font-size: 0.9rem; color: #666; }
    .step-box { background: #f8f9fa; padding: 1rem; border-radius: 8px; margin: 0.5rem 0; border-left: 4px solid #6b4ce6; }
    .disclaimer { font-size: 0.85rem; color: #666; padding: 0.75rem; background: #fff8e6; border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="welcome-card"><h1 style="margin:0 0 0.5rem 0;">🧠 MindScan</h1><p style="margin:0; font-size:1.1rem; opacity:0.95;">Your AI-powered mental wellness companion. Write, reflect, and track your emotional trends.</p></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("✍️ **Journal Now**", use_container_width=True, type="primary"):
        st.switch_page("pages/journal_page.py")
    st.caption("Write today's thoughts and get instant sentiment insights")
with col2:
    if st.button("📊 **View Dashboard**", use_container_width=True):
        st.switch_page("pages/dashboard_page.py")
    st.caption("See your emotional trend and wellness indicators")

st.subheader("How it works")
st.markdown("""
<div class="step-box">1️⃣ <strong>Journal</strong> – Type your thoughts or how you're feeling</div>
<div class="step-box">2️⃣ <strong>Analyze</strong> – We detect sentiment and wellness indicators</div>
<div class="step-box">3️⃣ <strong>Track</strong> – View trends and get gentle suggestions</div>
""", unsafe_allow_html=True)

st.markdown('<div class="disclaimer">⚠️ This system provides wellness indicators only. It is not a medical diagnostic tool.</div>', unsafe_allow_html=True)
