import streamlit as st


def render_footer():

    st.divider()

    st.markdown(
        """
<div style="text-align:center;padding:15px;">

<h4>📊 Customer Churn Prediction Dashboard</h4>

<p>
Powered by <b>Python</b> • <b>Scikit-learn</b> • <b>Streamlit</b> • <b>Plotly</b>
</p>

<p>
Developed by <b>Emad Qudah</b>
</p>

</div>
""",
        unsafe_allow_html=True,
    )