import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import streamlit as st

from src.predict import predict_customer

from components.styles import load_css
from components.sidebar import render_sidebar
from components.forms import customer_form
from components.cards import show_cards
from components.charts import show_charts
from components.recommendation import show_recommendation
from components.footer import render_footer


# ==========================================
# Page Config
# ==========================================

st.set_page_config(
    page_title="Customer Churn Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# Load UI
# ==========================================

load_css()

render_sidebar()

# ==========================================
# Header
# ==========================================

st.title("📊 Customer Churn Prediction Dashboard")

st.markdown("""
Predict whether a telecom customer is likely to churn using a trained Machine Learning model.

This dashboard helps customer retention teams identify customers at risk of leaving and provides business recommendations.
""")

st.divider()

# ==========================================
# Customer Form
# ==========================================

customer = customer_form()

# ==========================================
# Prediction
# ==========================================

if customer is not None:

    prediction, confidence, probabilities = predict_customer(customer)

    # KPI Cards
    show_cards(
        prediction,
        confidence,
        probabilities
    )

    st.divider()

    # Charts
    show_charts(probabilities)

    # Recommendations
    show_recommendation(
        prediction,
        probabilities,
        customer
    )

# ==========================================
# Footer
# ==========================================

render_footer()