import streamlit as st
import joblib
import warnings

warnings.filterwarnings("ignore")

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Student Marks Predictor",
    page_icon="🎓",
    layout="centered"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.stApp{
background: #F4F6FB;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Card */
.main-card{
background:#FFFFFF;
padding:40px;
border-radius:20px;
box-shadow:0 8px 24px rgba(0,0,0,0.08);
border-top:6px solid #7C3AED;
}

/* Title */
.title{
text-align:center;
font-size:34px;
font-weight:800;
color:#1E1B4B;
margin-bottom:0px;
}

.subtitle{
text-align:center;
color:#6B7280;
font-size:16px;
margin-bottom:30px;
}

/* Input label */
label{
color:#374151 !important;
font-weight:600;
}

/* Button */
.stButton>button{
width:100%;
height:50px;
border-radius:10px;
border:none;
font-size:18px;
font-weight:700;
background:#7C3AED;
color:white;
transition:0.25s;
}

.stButton>button:hover{
background:#6D28D9;
box-shadow:0px 6px 16px rgba(124,58,237,0.35);
}

/* Result card */
.result-box{
margin-top:20px;
padding:22px;
border-radius:14px;
background:#ECFDF5;
border-left:6px solid #10B981;
text-align:center;
}

.result-label{
color:#065F46;
font-size:15px;
font-weight:600;
}

.result-value{
color:#047857;
font-size:36px;
font-weight:800;
margin-top:4px;
}

/* Warning card */
.warn-box{
margin-top:20px;
padding:20px;
border-radius:14px;
background:#FFF7ED;
border-left:6px solid #F59E0B;
text-align:center;
color:#9A3412;
font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Sidebar ---------------- #

st.sidebar.title("🎓 About this Project")
st.sidebar.write("""
This app predicts a student's expected marks based on daily study hours, using a Linear Regression model trained on study-hours vs marks data.

**Valid Input Range:** 4 – 12 hours
""")

# ---------------- Main Card ---------------- #

st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown('<div class="title">🎓 Student Marks Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter your daily study hours to predict your expected marks</div>', unsafe_allow_html=True)

sh = st.number_input("Study Hours (per day)", min_value=0.0, max_value=24.0, step=0.5, format="%.1f")

predict = st.button("Predict My Marks")

if predict:
    if 4 <= sh <= 12:
        model = joblib.load("smp.pkl")
        res = model.predict([[sh]])[0][0].round(2)

        st.markdown(f"""
        <div class="result-box">
            <div class="result-label">Predicted Marks</div>
            <div class="result-value">{res} / 100</div>
        </div>
        """, unsafe_allow_html=True)

        st.progress(min(max(res / 100, 0.0), 1.0))
    else:
        st.markdown(
            '<div class="warn-box">⚠️ Please enter study hours between 4 and 12 for an accurate prediction.</div>',
            unsafe_allow_html=True
        )

st.markdown("</div>", unsafe_allow_html=True)