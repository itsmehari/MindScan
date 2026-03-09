import streamlit as st
from database.db_manager import init_db

# Ensure database and tables exist
init_db()

st.set_page_config(page_title="MindScan", layout="wide")

st.title("MindScan – AI Mental Wellness Indicator System")
st.caption("This system provides mental wellness indicators and is not a medical diagnostic tool.")

st.write("Navigate using the sidebar pages to test journal analysis and view the dashboard.")
