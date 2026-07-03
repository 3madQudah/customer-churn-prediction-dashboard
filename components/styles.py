import streamlit as st


def load_css():

    st.markdown(
        """
<style>

html, body, [class*="css"]{
    font-family: 'Inter', sans-serif;
}

.main{
    background:#f5f7fb;
}

.block-container{

    max-width:1450px;

    padding-top:2rem;

    padding-bottom:2rem;

    padding-left:2rem;

    padding-right:2rem;

}

section[data-testid="stSidebar"]{

    background:#0F172A;

}

section[data-testid="stSidebar"] *{

    color:white;

}

.stButton>button{

    width:100%;

    height:58px;

    border-radius:12px;

    border:none;

    background:#2563EB;

    color:white;

    font-size:18px;

    font-weight:600;

    transition:0.3s;

}

.stButton>button:hover{

    background:#1D4ED8;

    transform:translateY(-2px);

}

div[data-testid="stMetric"]{

    background:white;

    border-radius:16px;

    padding:18px;

    box-shadow:0 8px 20px rgba(0,0,0,.08);

    transition:.3s;

}

div[data-testid="stMetric"]:hover{

    transform:translateY(-3px);

    box-shadow:0 12px 25px rgba(0,0,0,.15);

}

.card{

    background:white;

    padding:22px;

    border-radius:16px;

    box-shadow:0 6px 20px rgba(0,0,0,.08);

    transition:.3s;

}

.card:hover{

    transform:translateY(-4px);

    box-shadow:0 10px 25px rgba(0,0,0,.12);

}

.success-card{

    background:#DCFCE7;

    border-left:8px solid #22C55E;

    border-radius:16px;

    padding:22px;

}

.danger-card{

    background:#FEE2E2;

    border-left:8px solid #EF4444;

    border-radius:16px;

    padding:22px;

}

.warning-card{

    background:#FEF3C7;

    border-left:8px solid #F59E0B;

    border-radius:16px;

    padding:22px;

}

hr{

    margin-top:25px;

    margin-bottom:25px;

}

</style>
""",
        unsafe_allow_html=True,
    )