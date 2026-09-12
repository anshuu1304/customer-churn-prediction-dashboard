import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)


# =========================
# LOAD DATA
# =========================

@st.cache_data
def load_data():

    BASE_DIR = Path(__file__).resolve().parents[2]

    DATA_PATH = (
        BASE_DIR
        / "data"
        / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
    )

    df = pd.read_csv(DATA_PATH)

    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    return df


df = load_data()

# =========================
# HEADER
# =========================

# st.markdown("""
# <div style="
#     padding: 25px 30px;
#     border-radius: 15px;
#     background: linear-gradient(135deg, #172554, #0f172a);
#     border: 1px solid #334155;
#     margin-bottom: 25px;
# ">
#     <h1 style="margin:0;">
#         📊 Churn Analytics
#     </h1>

#     <p style="
#         margin-top:10px;
#         color:#94a3b8;
#         font-size:17px;
#     ">
#         Customer behavior, churn patterns and business insights
#     </p>
# </div>
# """, unsafe_allow_html=True)

st.title("📊 Churn Analytics")
st.caption("Customer behavior, churn patterns and business insights")


# =========================
# KPI CALCULATIONS
# =========================

total_customers = len(df)

churned_customers = (df["Churn"] == "Yes").sum()

churn_rate = (
    churned_customers / total_customers
) * 100

avg_monthly = df["MonthlyCharges"].mean()

avg_tenure = df["tenure"].mean()


# =========================
# KPI CARDS
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Total Customers",
        f"{total_customers:,}"
    )

with col2:
    st.metric(
        "📉 Churn Rate",
        f"{churn_rate:.1f}%"
    )

with col3:
    st.metric(
        "💳 Avg Monthly Charges",
        f"${avg_monthly:.2f}"
    )

with col4:
    st.metric(
        "⏳ Avg Tenure",
        f"{avg_tenure:.0f} Months"
    )

st.divider()


# =========================
# CHURN OVERVIEW
# =========================

st.subheader("📈 Churn Overview")

churn_counts = (
    df["Churn"]
    .value_counts()
    .reset_index()
)

churn_counts.columns = [
    "Churn",
    "Customers"
]

fig = px.pie(
    churn_counts,
    names="Churn",
    values="Customers",
    hole=0.45,
    title="Customer Churn Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()


# =========================
# CHURN BY CONTRACT
# =========================

st.subheader("📋 Churn by Contract")

contract_churn = (
    pd.crosstab(
        df["Contract"],
        df["Churn"],
        normalize="index"
    ) * 100
)

fig = px.bar(
    contract_churn,
    barmode="group",
    title="Churn Percentage by Contract Type",
    labels={
        "value": "Percentage",
        "Contract": "Contract Type"
    }
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()


# =========================
# CHURN BY INTERNET SERVICE
# =========================

st.subheader("🌐 Churn by Internet Service")

internet_churn = (
    pd.crosstab(
        df["InternetService"],
        df["Churn"],
        normalize="index"
    ) * 100
)

fig = px.bar(
    internet_churn,
    barmode="group",
    title="Churn Percentage by Internet Service",
    labels={
        "value": "Percentage",
        "InternetService": "Internet Service"
    }
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()


# =========================
# TENURE VS CHURN
# =========================

st.subheader("⏳ Tenure vs Churn")

fig = px.box(
    df,
    x="Churn",
    y="tenure",
    title="Customer Tenure Distribution by Churn Status",
    labels={
        "tenure": "Tenure (Months)",
        "Churn": "Churn"
    }
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()


# =========================
# MONTHLY CHARGES VS CHURN
# =========================

st.subheader("💰 Monthly Charges vs Churn")

fig = px.box(
    df,
    x="Churn",
    y="MonthlyCharges",
    title="Monthly Charges Distribution by Churn Status",
    labels={
        "MonthlyCharges": "Monthly Charges ($)",
        "Churn": "Churn"
    }
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()


# =========================
# BUSINESS INSIGHTS
# =========================

st.subheader("💡 Business Insights")

col1, col2 = st.columns(2)

with col1:
    st.info(
        """
        **Key Churn Indicators**

        • Month-to-month customers show higher churn.

        • Customers with shorter tenure are more vulnerable.

        • Higher monthly charges are associated with greater churn.

        • Fiber optic customers show elevated churn.

        • Customers without support services may face higher risk.
        """
    )

with col2:
    st.success(
        """
        **Retention Strategy**

        • Prioritize month-to-month customers.

        • Focus on newly acquired customers.

        • Monitor customers with high monthly charges.

        • Provide proactive technical support.

        • Encourage longer-term contracts.
        """
    )