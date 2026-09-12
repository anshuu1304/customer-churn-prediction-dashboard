# Telecom Customer Churn Data Dictionary

## Target Variable

| Column | Description |
|----------|----------|
| Churn | 0 = Customer Stays, 1 = Customer Leaves |

---

## Customer Information

| Column | Data Type | Description |
|----------|----------|----------|
| CustomerID | String | Unique customer identifier |
| Age | Integer | Customer age |
| Gender | Category | Male / Female |
| Region | Category | North / South / East / West / Central |

---

## Subscription Information

| Column | Data Type | Description |
|----------|----------|----------|
| TenureMonths | Integer | Number of months customer has stayed with company |
| ContractType | Category | Monthly / One Year / Two Year |
| InternetType | Category | Fiber / DSL / 5G / Cable |
| AutoPay | Category | Yes / No |
| PremiumSupport | Category | Yes / No |

---

## Financial Information

| Column | Data Type | Description |
|----------|----------|----------|
| MonthlyCharges | Float | Monthly bill amount |
| TotalCharges | Float | Total revenue generated from customer |
| LatePayments | Integer | Number of delayed payments |

---

## Usage Information

| Column | Data Type | Description |
|----------|----------|----------|
| AvgMonthlyUsageGB | Float | Average monthly data consumption in GB |
| CallMinutes | Integer | Average monthly call minutes |

---

## Customer Service Information

| Column | Data Type | Description |
|----------|----------|----------|
| SupportTickets | Integer | Number of support tickets raised |
| ComplaintCount | Integer | Number of complaints filed |

---

## Customer Satisfaction

| Column | Data Type | Description |
|----------|----------|----------|
| SatisfactionScore | Integer | Customer satisfaction score (1–10) |
| NPSScore | Integer | Net Promoter Score (-100 to 100) |

---

## Dataset Summary

| Metric | Value |
|----------|----------|
| Domain | Telecom |
| Expected Rows | 100,000 |
| Expected Columns | 19 |
| Prediction Type | Binary Classification |
| Target Column | Churn |