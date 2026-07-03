import streamlit as st


def show_recommendation(prediction, probabilities, customer):

    churn = probabilities.get("Yes", 0) * 100

    st.divider()

    st.subheader("💡 Business Recommendation")

    # ======================================================
    # Recommendation Card
    # ======================================================

    if churn < 30:

        st.success("""
### 🟢 Low Risk Customer

The customer is likely to remain with the company.

### Recommended Actions

✅ Maintain current service quality

✅ Offer loyalty rewards

✅ Promote premium packages

✅ Continue customer engagement
""")

    elif churn < 60:

        st.warning("""
### 🟠 Medium Risk Customer

The customer shows moderate churn risk.

### Recommended Actions

✅ Send personalized offers

✅ Offer bundle discounts

✅ Increase customer follow-up

✅ Improve customer experience
""")

    else:

        st.error("""
### 🔴 High Risk Customer

Immediate retention action is recommended.

### Recommended Actions

✅ Contact customer immediately

✅ Offer loyalty discount

✅ Recommend yearly contract

✅ Escalate to Retention Team

✅ Assign account manager
""")

    st.divider()

    # ======================================================
    # Customer Summary
    # ======================================================

    st.subheader("📋 Customer Summary")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(f"""
### Personal

- Gender: **{customer['gender']}**
- Senior Citizen: **{customer['SeniorCitizen']}**
- Partner: **{customer['Partner']}**
- Dependents: **{customer['Dependents']}**
""")

    with col2:

        st.markdown(f"""
### Services

- Internet: **{customer['InternetService']}**
- Contract: **{customer['Contract']}**
- Phone: **{customer['PhoneService']}**
- Payment: **{customer['PaymentMethod']}**
""")

    with col3:

        st.markdown(f"""
### Charges

- Tenure: **{customer['tenure']} Months**

- Monthly Charges:
**${customer['MonthlyCharges']:.2f}**

- Total Charges:
**${customer['TotalCharges']:.2f}**
""")

    st.divider()

    # ======================================================
    # Business Insights
    # ======================================================

    st.subheader("📈 Business Insights")

    if prediction == "Yes":

        st.info("""
The model predicts that this customer is **likely to churn**.

Suggested strategy:

- Focus on retention.
- Offer financial incentives.
- Improve customer support.
- Strengthen customer relationship.
""")

    else:

        st.info("""
The customer is expected to remain with the company.

Suggested strategy:

- Upsell premium services.
- Offer loyalty programs.
- Maintain excellent service quality.
""")