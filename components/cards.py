import streamlit as st


def show_cards(prediction, confidence, probabilities):

    churn_probability = probabilities.get("Yes", 0) * 100
    stay_probability = probabilities.get("No", 0) * 100

    # ===========================
    # Risk Level
    # ===========================

    if churn_probability < 30:
        risk = "🟢 Low"
        risk_color = "#22C55E"

    elif churn_probability < 60:
        risk = "🟠 Medium"
        risk_color = "#F59E0B"

    else:
        risk = "🔴 High"
        risk_color = "#EF4444"

    # ===========================
    # Prediction Text
    # ===========================

    if prediction == "Yes":
        prediction_text = "Likely to Churn 🚨"
    else:
        prediction_text = "Likely to Stay ✅"

    # ===========================
    # Dashboard Cards
    # ===========================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            label="Prediction",
            value=prediction_text
        )

    with col2:

        st.metric(
            label="Confidence",
            value=f"{confidence*100:.2f}%"
        )

    with col3:

        st.markdown(
            f"""
<div style="
background:white;
padding:18px;
border-radius:15px;
text-align:center;
box-shadow:0px 5px 18px rgba(0,0,0,.08);
">

<h4>Risk Level</h4>

<h2 style="color:{risk_color};">
{risk}
</h2>

</div>
""",
            unsafe_allow_html=True,
        )

    with col4:

        st.metric(
            label="Churn Probability",
            value=f"{churn_probability:.2f}%"
        )

    st.progress(churn_probability / 100)