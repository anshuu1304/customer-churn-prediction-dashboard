# import streamlit as st

# st.set_page_config(
#     page_title="Customer Churn Platform",
#     page_icon="📊",
#     layout="wide"
# )

# # ---------- Header ----------
# st.markdown("""
# <div style="
#     padding: 25px 30px;
#     border-radius: 15px;
#     background: linear-gradient(135deg, #172554, #0f172a);
#     border: 1px solid #334155;
#     margin-bottom: 25px;
# ">
#     <h1 style="margin:0; font-size:42px;">
#         📊 Customer Churn Analytics
#     </h1>
#     <p style="font-size:17px; margin-top:10px; color:#94a3b8;">
#         AI-powered customer retention & decision-support platform
#     </p>
# </div>
# """, unsafe_allow_html=True)

# st.divider()

# # ---------- KPI Cards ----------
# # ---------- KPI CARDS ----------

# cols = st.columns(4)

# kpis = [
#     ("👥", "Total Customers", "7,043"),
#     ("📉", "Historical Churn", "26.5%"),
#     ("🎯", "Model ROC-AUC", "84.65%"),
#     ("⚙️", "Decision Threshold", "0.35")
# ]

# for col, (icon, label, value) in zip(cols, kpis):
#     with col:
#         st.markdown(
#             f"""
#             <div style="
#                 background:#111827;
#                 border:1px solid #334155;
#                 border-radius:8px;
#                 padding:20px;
#                 text-align:center;
#             ">
#                 <div style="font-size:24px;">{icon}</div>
#                 <div style="color:#94a3b8;font-size:13px;">
#                     {label}
#                 </div>
#                 <div style="
#                     color:#f8fafc;
#                     font-size:28px;
#                     font-weight:700;
#                 ">
#                     {value}
#                 </div>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )
# # ---------- Overview ----------
# st.subheader("🚀 Platform Overview")

# col1, col2 = st.columns(2)

# with col1:
#     st.markdown("""
#     ### 🔮 Single Customer Prediction

#     Analyze an individual customer and receive:

#     - Churn probability
#     - Risk level
#     - Retention priority
#     - Recommended action
#     - Business impact
#     """)

#     st.page_link(
#         "pages/2_Single_Prediction.py",
#         label="Go to Single Prediction →"
#     )

# with col2:
#     st.markdown("""
#     ### 📊 Analytics Dashboard

#     Explore:

#     - Churn trends
#     - Contract-wise churn
#     - Internet-service churn
#     - Customer demographics
#     - Probability distributions
#     """)

#     st.page_link(
#         "pages/3_Analytics.py",
#         label="Go to Analytics →"
#     )

# st.divider()

# # ---------- Model Information ----------
# st.subheader("🤖 Production Model")

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.info("**Model**\n\nCatBoost Champion")

# with col2:
#     st.info("**ROC-AUC**\n\n84.65%")

# with col3:
#     st.info("**Status**\n\n🟢 Production")

# st.divider()

# st.success(
#     "💡 Use the sidebar to navigate through the Customer Churn Platform."
# )



import streamlit as st

st.set_page_config(
    page_title="Customer Churn Dashboard",
    page_icon="📉",
    layout="wide"
)

# =========================
# HERO SECTION
# =========================

st.title("📊 Customer Churn Analytics")
st.caption(
    "AI-powered customer retention & decision-support platform"
)

st.divider()

# =========================
# PLATFORM OVERVIEW
# =========================

st.subheader("🚀 Platform Overview")

st.write(
    "A machine-learning powered platform that helps businesses "
    "identify customers at risk of churn and take proactive retention actions."
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### 🔮")
    st.markdown("**Predict Churn**")
    st.caption("Estimate the probability that a customer will churn.")

with col2:
    st.markdown("### 🎯")
    st.markdown("**Identify Risk**")
    st.caption("Classify customers into low, medium and high risk.")

with col3:
    st.markdown("### 📊")
    st.markdown("**Analyze Patterns**")
    st.caption("Explore customer behavior and historical churn trends.")

with col4:
    st.markdown("### 💡")
    st.markdown("**Take Action**")
    st.caption("Get practical retention recommendations.")

st.divider()

# =========================
# MAIN FEATURES
# =========================

st.subheader("⚡ Explore the Platform")

col1, col2 = st.columns(2)

with col1:
    st.markdown("## 🔮 Single Customer Prediction")

    st.write(
        "Analyze an individual customer and get:"
    )

    st.markdown("""
    - Churn probability
    - Risk level
    - Recommended retention action
    - Business impact
    """)

    st.page_link(
        "pages/2_Single_Prediction.py",
        label="🚀 Go to Single Prediction",
        icon="🔮"
    )

with col2:
    st.markdown("## 📊 Churn Analytics")

    st.write(
        "Explore historical customer behavior and churn patterns:"
    )

    st.markdown("""
    - Churn distribution
    - Contract-wise churn
    - Internet service churn
    - Tenure analysis
    - Monthly charges analysis
    """)

    st.page_link(
        "pages/3_Analytics.py",
        label="📈 Go to Analytics",
        icon="📊"
    )

st.divider()

# =========================
# HOW IT WORKS
# =========================

st.subheader("⚙️ How It Works")

step1, step2, step3, step4, step5 = st.columns(5)

with step1:
    st.markdown("### 1️⃣")
    st.markdown("**Customer Data**")
    st.caption("Customer profile and service information")

with step2:
    st.markdown("### 2️⃣")
    st.markdown("**ML Model**")
    st.caption("CatBoost analyzes customer behavior")

with step3:
    st.markdown("### 3️⃣")
    st.markdown("**Churn Probability**")
    st.caption("Model estimates future churn risk")

with step4:
    st.markdown("### 4️⃣")
    st.markdown("**Risk Level**")
    st.caption("Low, Medium or High")

with step5:
    st.markdown("### 5️⃣")
    st.markdown("**Retention Action**")
    st.caption("Recommended business response")

st.divider()

# =========================
# PRODUCTION MODEL
# =========================

st.subheader("🤖 Production Model")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Model**")
    st.markdown("### CatBoost Champion")
    st.caption("Production-ready classification model")

with col2:
    st.markdown("**Performance**")
    st.markdown("### ROC-AUC: 84.65%")
    st.caption("Test-set performance")

with col3:
    st.markdown("**Status**")
    st.markdown("### 🟢 Production")
    st.caption("Model tracked with MLflow")

st.divider()

st.success(
    "💡 Use the sidebar to explore predictions and customer churn analytics."
)