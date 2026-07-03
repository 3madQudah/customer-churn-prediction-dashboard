import streamlit as st
import plotly.graph_objects as go
import plotly.express as px


def show_charts(probabilities):

    churn = probabilities.get("Yes", 0) * 100
    stay = probabilities.get("No", 0) * 100

    col1, col2 = st.columns(2)

    # ======================================================
    # Gauge Chart
    # ======================================================

    with col1:

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=churn,
                number={"suffix": "%"},
                title={
                    "text": "<b>Churn Risk</b>",
                    "font": {"size": 24}
                },
                gauge={
                    "axis": {
                        "range": [0, 100],
                        "tickwidth": 1
                    },
                    "bar": {
                        "color": "#2563EB",
                        "thickness": 0.35
                    },
                    "steps": [

                        {
                            "range": [0, 30],
                            "color": "#DCFCE7"
                        },

                        {
                            "range": [30, 60],
                            "color": "#FEF3C7"
                        },

                        {
                            "range": [60, 100],
                            "color": "#FEE2E2"
                        }

                    ],

                    "threshold": {

                        "line": {
                            "color": "red",
                            "width": 6
                        },

                        "value": churn

                    }

                }

            )
        )

        gauge.update_layout(

            height=420,

            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20
            )

        )

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

    # ======================================================
    # Pie Chart
    # ======================================================

    with col2:

        pie = px.pie(

            names=[
                "Stay",
                "Churn"
            ],

            values=[
                stay,
                churn
            ],

            hole=0.65,

            color_discrete_sequence=[
                "#22C55E",
                "#EF4444"
            ]

        )

        pie.update_traces(

            textposition="inside",

            textinfo="percent+label"

        )

        pie.update_layout(

            title="<b>Prediction Probability</b>",

            height=420,

            legend_title="",

            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20
            )

        )

        st.plotly_chart(

            pie,

            use_container_width=True

        )

    # ======================================================
    # Progress
    # ======================================================

    st.subheader("Prediction Confidence")

    st.progress(churn / 100)

    left, right = st.columns(2)

    with left:

        st.success(
            f"Stay Probability : {stay:.2f}%"
        )

    with right:

        st.error(
            f"Churn Probability : {churn:.2f}%"
        )