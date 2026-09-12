# import streamlit as st

# st.set_page_config(
#     page_title="Customer Churn Dashboard",
#     page_icon="📉",
#     layout="wide"
# )

# st.title("📉 Customer Churn Dashboard")

# st.markdown("""
# ### Welcome

# Use the sidebar to navigate:

# - Home
# - Single Prediction
# - Analytics
# """)



import streamlit as st

st.set_page_config(
    page_title="Customer Churn Dashboard",
    page_icon="📉",
    layout="wide"
)

# =========================
# HEADER
# =========================

st.title("📉 Customer Churn Intelligence")

st.write(
    "AI-powered customer retention & decision-support platform"
)

st.info(
    "Predict customer churn, understand risk factors, "
    "and take data-driven retention decisions."
)

st.divider()

# =========================
# PLATFORM CAPABILITIES
# =========================

st.subheader("🚀 Platform Capabilities")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🎯 Churn Prediction")
    st.write("Analyze individual customers and estimate their future churn risk.")
    st.write("✓ Churn probability")
    st.write("✓ Risk classification")
    st.write("✓ Retention recommendation")

with col2:
    st.markdown("### 📊 Business Analytics")
    st.write("Explore customer behavior and discover important churn patterns.")
    st.write("✓ Churn trends")
    st.write("✓ Contract analysis")
    st.write("✓ Customer behavior")

with col3:
    st.markdown("### ⚙️ Production ML")
    st.write("Powered by a production-ready machine learning pipeline.")
    st.write("✓ CatBoost Champion Model")
    st.write("✓ FastAPI prediction service")
    st.write("✓ MLflow experiment tracking")

st.divider()

# =========================
# HOW IT WORKS
# =========================

st.subheader("⚙️ How It Works")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### 01")
    st.markdown("**Customer Data**")
    st.write("Enter customer information.")

with col2:
    st.markdown("### 02")
    st.markdown("**ML Prediction**")
    st.write("Model calculates churn probability.")

with col3:
    st.markdown("### 03")
    st.markdown("**Risk Assessment**")
    st.write("Identify low, medium or high risk.")

with col4:
    st.markdown("### 04")
    st.markdown("**Action**")
    st.write("Apply targeted retention strategy.")

st.divider()

# =========================
# NAVIGATION
# =========================

st.subheader("🧭 Explore the Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎯 Single Prediction")
    st.write(
        "Predict the churn risk of an individual customer "
        "and receive a recommended retention action."
    )

with col2:
    st.markdown("### 📊 Analytics")
    st.write(
        "Explore churn patterns, customer behavior, "
        "contract trends and business insights."
    )

st.success(
    "💡 Use the sidebar to navigate between Prediction and Analytics."
)