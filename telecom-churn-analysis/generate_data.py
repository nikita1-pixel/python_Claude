"""
Generate a realistic telecom customer-churn dataset for a Business Analyst
Tableau project. ~7,000 customers, ~20 fields.

A real churn STORY is baked in (so the dashboard reveals genuine drivers):
  - Month-to-month contracts churn FAR more than 1- or 2-year contracts
  - Brand-new customers (low tenure) churn much more than loyal ones
  - Fiber-optic internet churns more than DSL (price/expectation)
  - No tech support / no online security -> higher churn
  - Electronic-check payers churn more
  - Higher monthly charges -> higher churn
Each customer's churn is drawn from a probability built from these factors,
so the patterns are statistically real, not hard-coded labels.

Run:  python generate_data.py
Out:  telecom_churn.csv
"""

import csv
import random

random.seed(42)  # reproducible -> same dataset every run

N = 7043  # same size as the famous IBM Telco dataset

genders = ["Male", "Female"]
yes_no = ["Yes", "No"]
internet_types = ["DSL", "Fiber optic", "No"]
contracts = ["Month-to-month", "One year", "Two year"]
payments = ["Electronic check", "Mailed check",
            "Bank transfer (automatic)", "Credit card (automatic)"]


def pick(options):
    return random.choice(options)


def addon(internet):
    """Add-on services only exist if the customer has internet."""
    if internet == "No":
        return "No internet service"
    return pick(yes_no)


def churn_probability(row):
    """Build a 0..1 churn probability from the real-world drivers."""
    p = 0.02  # base rate

    # Contract is the strongest driver
    if row["Contract"] == "Month-to-month":
        p += 0.26
    elif row["Contract"] == "One year":
        p += 0.03
    else:  # Two year
        p += 0.005

    # Tenure: new customers churn a lot, loyal ones rarely
    if row["tenure"] <= 6:
        p += 0.13
    elif row["tenure"] <= 18:
        p += 0.06
    elif row["tenure"] >= 48:
        p -= 0.07

    # Internet type
    if row["InternetService"] == "Fiber optic":
        p += 0.08
    elif row["InternetService"] == "No":
        p -= 0.04

    # Protective services reduce churn
    if row["TechSupport"] == "No":
        p += 0.04
    if row["OnlineSecurity"] == "No":
        p += 0.03

    # Payment method
    if row["PaymentMethod"] == "Electronic check":
        p += 0.06

    # Price sensitivity
    if row["MonthlyCharges"] > 80:
        p += 0.04

    # Senior citizens churn a bit more
    if row["SeniorCitizen"] == 1:
        p += 0.04

    return max(0.01, min(p, 0.95))


def make_row(i):
    senior = 1 if random.random() < 0.16 else 0
    tenure = random.randint(0, 72)
    internet = random.choices(internet_types, weights=[34, 44, 22])[0]
    contract = random.choices(contracts, weights=[55, 21, 24])[0]

    # Monthly charges depend on internet type + add-ons (realistic pricing)
    base = 20.0
    if internet == "DSL":
        base = 50.0
    elif internet == "Fiber optic":
        base = 80.0
    monthly = round(base + random.uniform(-8, 25), 2)
    monthly = max(18.25, monthly)

    row = {
        "customerID": f"{random.randint(1000,9999)}-{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5))}",
        "gender": pick(genders),
        "SeniorCitizen": senior,
        "Partner": pick(yes_no),
        "Dependents": pick(yes_no),
        "tenure": tenure,
        "PhoneService": "Yes" if random.random() < 0.9 else "No",
        "InternetService": internet,
        "OnlineSecurity": addon(internet),
        "OnlineBackup": addon(internet),
        "DeviceProtection": addon(internet),
        "TechSupport": addon(internet),
        "StreamingTV": addon(internet),
        "StreamingMovies": addon(internet),
        "Contract": contract,
        "PaperlessBilling": pick(yes_no),
        "PaymentMethod": pick(payments),
        "MonthlyCharges": monthly,
        "TotalCharges": round(monthly * max(tenure, 1) + random.uniform(-30, 30), 2),
    }

    p = churn_probability(row)
    row["Churn"] = "Yes" if random.random() < p else "No"
    return row


def main():
    fields = ["customerID", "gender", "SeniorCitizen", "Partner", "Dependents",
              "tenure", "PhoneService", "InternetService", "OnlineSecurity",
              "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV",
              "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod",
              "MonthlyCharges", "TotalCharges", "Churn"]

    rows = [make_row(i) for i in range(N)]

    with open("telecom_churn.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    churned = sum(1 for r in rows if r["Churn"] == "Yes")
    print(f"Wrote telecom_churn.csv: {len(rows)} customers, {len(fields)} columns")
    print(f"Overall churn rate: {churned/len(rows)*100:.1f}%")


if __name__ == "__main__":
    main()
