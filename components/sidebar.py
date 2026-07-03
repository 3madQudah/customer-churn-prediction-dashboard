import streamlit as st


def render_sidebar():

    st.sidebar.title("📊 Churn Prediction")

    st.sidebar.markdown("---")

    st.sidebar.markdown(
        """
### AI Dashboard

Customer Churn Prediction using Machine Learning.

---

### Features

✅ Churn Prediction

✅ Risk Analysis

✅ Probability Score

✅ Business Recommendation

---
"""
    )

    st.sidebar.info(
        """
Developer

**Emad Qudah**

AI Engineer
"""
    )

    st.sidebar.markdown("---")

    st.sidebar.success(
        """
Version 1.0
"""
    )