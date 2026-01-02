import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data/financial_product_data.csv")

# Basic exploration
print(df.describe())

# Engagement vs churn
sns.boxplot(x="churned", y="monthly_transactions", data=df)
plt.title("Monthly Transactions vs Churn")
plt.show()

# Risk signal: low engagement users
df["risk_flag"] = (df["monthly_transactions"] < 8) & (df["login_frequency"] < 5)

risk_summary = df.groupby("risk_flag")["churned"].mean()
print("Churn rate by risk flag:")
print(risk_summary)
