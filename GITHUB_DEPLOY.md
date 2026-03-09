# MindScan – GitHub & Streamlit Cloud Deploy Guide

## Test Locally First

```bash
cd mindscan_streamlit_project
pip install -r requirements.txt
streamlit run app.py
```

Open http://localhost:8501 in your browser. Test Journal and Dashboard pages.

---

## 1. Push to GitHub

1. Create a new repo on GitHub (e.g. `MindScan` or `mindscan-mental-wellness`).
2. From your project folder, run:

```bash
cd E:\OneDrive\Glor\Others-Project\MindScan

git init
git add .
git commit -m "Initial commit - MindScan project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

Replace `YOUR_USERNAME` and `YOUR_REPO` with your GitHub details.

---

## 2. Deploy on Streamlit Cloud

1. Go to **[share.streamlit.io](https://share.streamlit.io)** and sign in with GitHub.
2. Click **New app**.
3. Set:
   - **Repository:** `YOUR_USERNAME/YOUR_REPO`
   - **Branch:** `main`
   - **Main file path:** `mindscan_streamlit_project/app.py`
4. Click **Deploy**.

Your app will be live at `https://YOUR_APP_NAME.streamlit.app` in a few minutes.

---

## 3. Verify

- Journal page: Enter text, click Analyze → sentiment and risk band appear.
- Dashboard: Shows sample trend when DB is empty; shows your entries after you add journal data.
