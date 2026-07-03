import streamlit as st


def customer_form():

    st.subheader("👤 Customer Information")

    col1, col2 = st.columns(2)

    with col1:

        gender = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )

        SeniorCitizen = st.selectbox(
            "Senior Citizen",
            [0, 1]
        )

        Partner = st.selectbox(
            "Partner",
            ["Yes", "No"]
        )

        Dependents = st.selectbox(
            "Dependents",
            ["Yes", "No"]
        )

        tenure = st.slider(
            "Tenure (Months)",
            min_value=0,
            max_value=72,
            value=12
        )

    with col2:

        PhoneService = st.selectbox(
            "Phone Service",
            ["Yes", "No"]
        )

        MultipleLines = st.selectbox(
            "Multiple Lines",
            [
                "No",
                "Yes",
                "No phone service"
            ]
        )

    st.divider()

    # ==========================================
    # Internet Services
    # ==========================================

    st.subheader("🌐 Internet Services")

    col3, col4 = st.columns(2)

    with col3:

        InternetService = st.selectbox(
            "Internet Service",
            [
                "DSL",
                "Fiber optic",
                "No"
            ]
        )

        OnlineSecurity = st.selectbox(
            "Online Security",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        OnlineBackup = st.selectbox(
            "Online Backup",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

    with col4:

        DeviceProtection = st.selectbox(
            "Device Protection",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        TechSupport = st.selectbox(
            "Tech Support",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        StreamingTV = st.selectbox(
            "Streaming TV",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        StreamingMovies = st.selectbox(
            "Streaming Movies",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

    st.divider()

    # ==========================================
    # Billing
    # ==========================================

    st.subheader("💳 Billing Information")

    col5, col6 = st.columns(2)

    with col5:

        Contract = st.selectbox(
            "Contract",
            [
                "Month-to-month",
                "One year",
                "Two year"
            ]
        )

        PaperlessBilling = st.selectbox(
            "Paperless Billing",
            [
                "Yes",
                "No"
            ]
        )

    with col6:

        PaymentMethod = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

    st.divider()

    # ==========================================
    # Charges
    # ==========================================

    st.subheader("💰 Charges")

    col7, col8 = st.columns(2)

    with col7:

        MonthlyCharges = st.number_input(
            "Monthly Charges",
            min_value=0.0,
            max_value=200.0,
            value=70.0,
            step=0.1
        )

    with col8:

        TotalCharges = st.number_input(
            "Total Charges",
            min_value=0.0,
            max_value=10000.0,
            value=1000.0,
            step=1.0
        )

    st.divider()

    predict = st.button(
        "🔍 Predict Customer Churn",
        use_container_width=True
    )

    if not predict:
        return None

    customer = {

        "gender": gender,

        "SeniorCitizen": SeniorCitizen,

        "Partner": Partner,

        "Dependents": Dependents,

        "tenure": tenure,

        "PhoneService": PhoneService,

        "MultipleLines": MultipleLines,

        "InternetService": InternetService,

        "OnlineSecurity": OnlineSecurity,

        "OnlineBackup": OnlineBackup,

        "DeviceProtection": DeviceProtection,

        "TechSupport": TechSupport,

        "StreamingTV": StreamingTV,

        "StreamingMovies": StreamingMovies,

        "Contract": Contract,

        "PaperlessBilling": PaperlessBilling,

        "PaymentMethod": PaymentMethod,

        "MonthlyCharges": MonthlyCharges,

        "TotalCharges": TotalCharges,
    }

    return customer