import streamlit as st
import requests
import plotly.graph_objects as go

st.set_page_config(
    page_title="Single Customer Prediction",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 Single Customer Churn Prediction")
st.caption("Analyze an individual customer and estimate their churn risk.")

st.divider()

# -----------------------------
# CUSTOMER INFORMATION
# -----------------------------

st.subheader("👤 Customer Information")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])

with col2:
    tenure = st.number_input(
        "Tenure (months)",
        min_value=0,
        max_value=72,
        value=12
    )

    phone = st.selectbox("Phone Service", ["Yes", "No"])
    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

with col3:
    internet = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

st.divider()

# -----------------------------
# SERVICES
# -----------------------------

st.subheader("🛠️ Customer Services")

col1, col2, col3 = st.columns(3)

with col1:
    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )

with col2:
    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

with col3:
    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

st.divider()

# -----------------------------
# BILLING
# -----------------------------

st.subheader("💳 Billing Information")

col1, col2, col3 = st.columns(3)

with col1:
    payment = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

with col2:
    monthly_charges = st.number_input(
        "Monthly Charges ($)",
        min_value=0.0,
        value=70.0
    )

with col3:
    total_charges = st.number_input(
        "Total Charges ($)",
        min_value=0.0,
        value=monthly_charges * tenure
    )

st.divider()

# -----------------------------
# PREDICT BUTTON
# -----------------------------

if st.button("🚀 Predict Churn Risk", use_container_width=True):

    payload = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "MultipleLines": multiple_lines,
        "InternetService": internet,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }

    try:
        response = requests.post(
            "https://customer-churn-prediction-dashboard-s2f0.onrender.com/predict",
            json=payload,
            timeout=10
        )

        if response.status_code == 200:

            result = response.json()

            st.success("Prediction completed successfully!")

            st.divider()

            # =========================
            # PREDICTION SUMMARY
            # =========================

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Churn Probability",
                    f"{result['churn_probability']:.1%}"
                )

            with col2:
                st.metric(
                    "Prediction",
                    result["prediction"]
                )

            with col3:
                probability = result["churn_probability"]

                if probability >= 0.60:
                    st.error("🔴 High Risk")
                elif probability >= 0.35:
                    st.warning("🟡 Medium Risk")
                else:
                    st.success("🟢 Low Risk")

            # =========================
            # FUTURE CHURN RISK METER
            # =========================

            st.divider()

            st.subheader("🎯 Future Churn Risk Assessment")

            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=probability * 100,
                    number={
                        "suffix": "%",
                        "font": {"size": 40}
                    },
                    title={
                        "text": "Probability of Customer Churning"
                    },
                    gauge={
                        "axis": {
                            "range": [0, 100]
                        },
                        "bar": {
                            "color": "#ef4444"
                        },
                        "steps": [
                            {
                                "range": [0, 35],
                                "color": "#166534"
                            },
                            {
                                "range": [35, 60],
                                "color": "#ca8a04"
                            },
                            {
                                "range": [60, 100],
                                "color": "#991b1b"
                            }
                        ],
                        "threshold": {
                            "line": {
                                "color": "white",
                                "width": 4
                            },
                            "value": 35
                        }
                    }
                )
            )

            fig.update_layout(
                height=350,
                margin=dict(
                    l=30,
                    r=30,
                    t=70,
                    b=20
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            # =========================
            # RISK MESSAGE
            # =========================

            if probability >= 0.60:

                st.error(
                    "🔴 High Risk — Customer has a high probability of churning."
                )

            elif probability >= 0.35:

                st.warning(
                    "🟡 Medium Risk — Customer should be considered for retention."
                )

            else:

                st.success(
                    "🟢 Low Risk — Customer currently has a low churn probability."
                )

        else:

            st.error(
                f"API Error: {response.text}"
            )


        st.divider()

        st.subheader("💡 Recommended Retention Action")

        if probability >= 0.60:
            st.error("""
            **Priority: Immediate Retention**

            Recommended actions:
            - Contact the customer proactively
            - Offer a personalized retention incentive
            - Investigate service/support issues
            - Consider a contract upgrade or loyalty offer
        """)

        elif probability >= 0.35:

            st.warning("""
            **Priority: Preventive Retention**

            Recommended actions:
            - Monitor customer engagement
            - Offer targeted discounts
            - Improve support experience
            - Encourage longer-term contract adoption
        """)

        else:

            st.success("""
            **Priority: Maintain Relationship**

            Recommended actions:
            - Continue regular engagement
            - Maintain service quality
            - Offer relevant loyalty benefits
        """)    

        st.divider()

        st.subheader("💰 Business Impact")

        if probability >= 0.60:
            impact = "High"
            action = "Immediate intervention recommended"
        elif probability >= 0.35:
            impact = "Medium"
            action = "Preventive retention recommended"
        else:
            impact = "Low"
            action = "Continue normal engagement"

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Churn Risk", impact)

        with col2:
            st.metric("Recommended Action", action)    

    except requests.exceptions.RequestException:

        st.error(
            "❌ FastAPI is not running. "
            "Start the API on port 8000."
        )














# import streamlit as st
# import requests
# import pandas as pd
# import plotly.graph_objects as go

# # =========================
# # PAGE CONFIG
# # =========================

# st.set_page_config(
#     page_title="Customer Churn Prediction Dashboard",
#     page_icon="📉",
#     layout="wide"
# )


# st.markdown("""
# <style>

# .main {
#     padding-top: 1rem;
# }

# [data-testid="metric-container"] {
#     background-color: #1e293b;
#     border: 1px solid #334155;
#     padding: 15px;
#     border-radius: 12px;
#     text-align: center;
# }

# div.stButton > button {
#     width: 100%;
#     border-radius: 10px;
#     height: 50px;
#     font-size: 16px;
#     font-weight: bold;
# }

# div.stButton > button:hover {
#     transform: scale(1.02);
# }

# .stAlert {
#     border-radius: 10px;
# }

# h1, h2, h3 {
#     color: #f8fafc;
# }

# </style>
# """, unsafe_allow_html=True)

# # =========================
# # HEADER
# # =========================

# st.title("📉 Customer Churn Prediction Dashboard")

# st.markdown("""
# This dashboard predicts customer churn probability using the
# production CatBoost Champion Model.
# """)

# with st.sidebar:
#     st.image(
#         "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
#         width=100
#     )

#     st.title("Customer Churn")

#     st.markdown("---")

#     prediction_mode = st.radio(
#         "Select Mode",
#         [
#             "Single Customer",
#             "Batch Prediction"
#         ]
#     )

#     st.markdown("---")

#     st.metric(
#         label="Model",
#         value="CatBoost Champion"
#     )

#     st.metric(
#         label="Threshold",
#         value="0.35"
#     )

#     st.metric(
#         label="ROC-AUC",
#         value="84.65%"
#     )

#     st.markdown("---")

#     st.info(
#         "This dashboard helps identify customers likely to churn and suggests retention actions."
#     )

# st.divider()


# kpi1, kpi2, kpi3, kpi4 = st.columns(4)

# with kpi1:
#     st.metric(
#         "Model",
#         "CatBoost"
#     )

# with kpi2:
#     st.metric(
#         "ROC-AUC",
#         "84.65%"
#     )

# with kpi3:
#     st.metric(
#         "Threshold",
#         "0.35"
#     )

# with kpi4:
#     st.metric(
#         "Status",
#         "Production"
#     )

# st.divider()

# # ==========================================================
# # SINGLE CUSTOMER PREDICTION
# # ==========================================================

# if prediction_mode == "Single Customer":

#     col1, col2 = st.columns([1, 1])

#     # =========================
#     # LEFT PANEL
#     # =========================

#     with col1:

#         st.subheader("Customer Information")

#         gender = st.selectbox(
#             "Gender",
#             ["Female", "Male"]
#         )

#         senior_citizen = st.selectbox(
#             "Senior Citizen",
#             [0, 1]
#         )

#         partner = st.selectbox(
#             "Partner",
#             ["Yes", "No"]
#         )

#         dependents = st.selectbox(
#             "Dependents",
#             ["Yes", "No"]
#         )

#         tenure = st.slider(
#             "Tenure (Months)",
#             min_value=0,
#             max_value=72,
#             value=12
#         )

#         monthly_charges = st.number_input(
#             "Monthly Charges",
#             min_value=0.0,
#             value=70.0
#         )

#         total_charges = st.number_input(
#             "Total Charges",
#             min_value=0.0,
#             value=800.0
#         )

#         phone_service = st.selectbox(
#             "Phone Service",
#             ["Yes", "No"]
#         )

#         multiple_lines = st.selectbox(
#             "Multiple Lines",
#             ["Yes", "No", "No phone service"]
#         )

#         internet_service = st.selectbox(
#             "Internet Service",
#             ["DSL", "Fiber optic", "No"]
#         )

#         online_security = st.selectbox(
#             "Online Security",
#             ["Yes", "No", "No internet service"]
#         )

#         online_backup = st.selectbox(
#             "Online Backup",
#             ["Yes", "No", "No internet service"]
#         )

#         device_protection = st.selectbox(
#             "Device Protection",
#             ["Yes", "No", "No internet service"]
#         )

#         tech_support = st.selectbox(
#             "Tech Support",
#             ["Yes", "No", "No internet service"]
#         )

#         streaming_tv = st.selectbox(
#             "Streaming TV",
#             ["Yes", "No", "No internet service"]
#         )

#         streaming_movies = st.selectbox(
#             "Streaming Movies",
#             ["Yes", "No", "No internet service"]
#         )

#         contract = st.selectbox(
#             "Contract",
#             ["Month-to-month", "One year", "Two year"]
#         )

#         paperless_billing = st.selectbox(
#             "Paperless Billing",
#             ["Yes", "No"]
#         )

#         payment_method = st.selectbox(
#             "Payment Method",
#             [
#                 "Electronic check",
#                 "Mailed check",
#                 "Bank transfer (automatic)",
#                 "Credit card (automatic)"
#             ]
#         )

#         predict_btn = st.button(
#             "Predict Customer Churn",
#             use_container_width=True
#         )

#     # =========================
#     # RIGHT PANEL
#     # =========================

#     with col2:
#         st.markdown("""<div style="
#            background-color:#111827;
#            padding:20px;
#            border-radius:15px;
#            border:1px solid #374151;">
#        <h2>Prediction Results</h2>
#     </div>
#     """, unsafe_allow_html=True)
        

#         if predict_btn:

#             payload = {
#                 "gender": gender,
#                 "SeniorCitizen": senior_citizen,
#                 "Partner": partner,
#                 "Dependents": dependents,
#                 "tenure": tenure,
#                 "PhoneService": phone_service,
#                 "MultipleLines": multiple_lines,
#                 "InternetService": internet_service,
#                 "OnlineSecurity": online_security,
#                 "OnlineBackup": online_backup,
#                 "DeviceProtection": device_protection,
#                 "TechSupport": tech_support,
#                 "StreamingTV": streaming_tv,
#                 "StreamingMovies": streaming_movies,
#                 "Contract": contract,
#                 "PaperlessBilling": paperless_billing,
#                 "PaymentMethod": payment_method,
#                 "MonthlyCharges": monthly_charges,
#                 "TotalCharges": total_charges
#             }

#             try:

#                 response = requests.post(
#                     "http://localhost:8000/predict",
#                     json=payload
#                 )

#                 result = response.json()

#                 probability = result["churn_probability"]
#                 prediction = result["prediction"]
#                 risk_level = result["risk_level"]

#                 st.success("Prediction Completed")

#                 st.metric(
#                      "Churn Probability",
#                      f"{probability:.1%}"
#                 )


#                 fig = go.Figure(go.Indicator(
#                       mode="gauge+number",
#                       value=probability * 100,
#                       title={"text": "Churn Risk Score"},
#                       gauge={
#                            "axis": {"range": [0, 100]},
#                            "steps": [
#                                 {"range": [0, 35], "color": "lightgreen"},
#                                 {"range": [35, 70], "color": "gold"},
#                                 {"range": [70, 100], "color": "salmon"}
#                             ]
#                          }
#                 ))

#                 st.plotly_chart(
#                     fig,
#                     use_container_width=True
#                 )


#                 st.progress(float(probability))

#                 st.caption(
#                     f"Probability Score: {probability:.4f}"
#                 )

#                 st.progress(float(probability))

#                 if prediction == "Yes":
#                     st.error("⚠️ Customer Likely to Churn")
#                 else:
#                     st.success("✅ Customer Likely to Stay")

#                 st.subheader("Risk Assessment")

#                 if risk_level == "High":
#                      st.error("🔴 HIGH RISK CUSTOMER")
#                      st.progress(100)

#                 elif risk_level == "Medium":
#                      st.warning("🟡 MEDIUM RISK CUSTOMER")
#                      st.progress(60)

#                 else:
#                      st.success("🟢 LOW RISK CUSTOMER")
#                      st.progress(25)

#                 st.subheader("Recommended Action")

#                 if risk_level == "High":

#                     st.markdown("""
#                     - Immediate retention campaign
#                     - Offer contract upgrade
#                     - Provide loyalty discount
#                     - Customer success follow-up
#                     """)

#                 elif risk_level == "Medium":

#                     st.markdown("""
#                     - Targeted promotional offer
#                     - Service satisfaction survey
#                     - Monitor engagement
#                     """)

#                 else:

#                     st.markdown("""
#                     - Continue standard engagement
#                     - Upsell premium services
#                     - Maintain customer satisfaction
#                     """)

#                 st.subheader("Customer Summary")

#                 st.write(f"Tenure: {tenure} months")
#                 st.write(f"Contract: {contract}")
#                 st.write(f"Internet Service: {internet_service}")
#                 st.write(f"Monthly Charges: ${monthly_charges:.2f}")


#                 st.subheader("Business Impact")

#                 if risk_level == "High":

#                     estimated_clv = monthly_charges * 24

#                     st.metric(
#                         "Estimated Customer Value",
#                         f"${estimated_clv:,.0f}"
#                     )

#                     st.metric(
#                         "Retention Priority",
#                         "High"
#                     )

#                     st.error(
#                         "Potential revenue loss if customer churns."
#                     )

#                 elif risk_level == "Medium":

#                     estimated_clv = monthly_charges * 18

#                     st.metric(
#                         "Estimated Customer Value",
#                         f"${estimated_clv:,.0f}"
#                     )

#                     st.metric(
#                         "Retention Priority",
#                         "Medium"
#                     )

#                 else:

#                     estimated_clv = monthly_charges * 12

#                     st.metric(
#                         "Estimated Customer Value",
#                         f"${estimated_clv:,.0f}"
#                     )

#                     st.metric(
#                         "Retention Priority",
#                         "Low"
#                     )


#                 st.subheader("Why This Prediction?")

#                 reasons = []

#                 if tenure < 12:
#                     reasons.append("🔴 Low tenure customer")

#                 if contract == "Month-to-month":
#                     reasons.append("🔴 Month-to-month contract")

#                 if internet_service == "Fiber optic":
#                     reasons.append("🟡 Fiber optic service")

#                 if monthly_charges > 80:
#                     reasons.append("🟡 High monthly charges")

#                 if tech_support == "No":
#                     reasons.append("🔴 No tech support")

#                 if online_security == "No":
#                     reasons.append("🟡 No online security")

#                 if len(reasons) > 0:

#                     st.info("Top factors influencing prediction")

#                     for reason in reasons:
#                          st.write(reason)

#                 else:
#                     st.success(
#                         "No major churn risk factors detected."
#                     )  


#                 st.subheader("Customer Segment")

#                 if risk_level == "High":

#                     st.error(
#                         "⚠️ At-Risk Customer"
#                     )

#                 elif monthly_charges > 80 and tenure > 24:
#                     st.success(
#                         "⭐ Premium Customer"
#                     )

#                 elif tenure > 36:
#                     st.success(
#                         "💎 Loyal Customer"
#                     )

#                 else:

#                     st.info(
#                         "📊 Standard Customer"
#                     )      


#             except Exception as e:

#                 st.error(f"Error: {e}")

#         else:

#             st.info("Prediction results will appear here.")


# # ==========================================================
# # BATCH PREDICTION
# # ==========================================================

# elif prediction_mode == "Batch Prediction":

#     st.subheader("Batch Customer Churn Prediction")

#     uploaded_file = st.file_uploader(
#         "Upload Customer CSV",
#         type=["csv"]
#     )

#     if uploaded_file is not None:

#         df = pd.read_csv(uploaded_file)

#         st.write("Dataset Preview")

#         st.dataframe(df.head())

#         st.info(
#             "Batch prediction functionality will be added next."
#         )