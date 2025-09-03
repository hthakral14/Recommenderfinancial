

### `streamlit_app.py`

import streamlit as st
from src.serve import get_recommendations, load_users

st.set_page_config(page_title="Financial Recommender Demo", layout="wide")
st.title("📈 Personalized Financial Recommender — Demo")

users = load_users()
user_id = st.selectbox("Select user id", users["user_id"].tolist())

if st.button("Get recommendations"):
    recs = get_recommendations(user_id, top_k=8)
    st.write("Top recommendations (asset_id, ticker, sector, score):")
    st.table(recs[["asset_id", "ticker", "sector", "score"]])
