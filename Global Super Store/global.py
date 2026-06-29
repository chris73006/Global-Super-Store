import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Global_Superstore2.csv", encoding="latin1")

# Convert Date Columns
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)

# Remove Duplicates
df = df.drop_duplicates()

# Remove Extra Spaces
text_columns = df.select_dtypes(include="object").columns
for col in text_columns:
    df[col] = df[col].str.strip()

# Fill Missing Postal Codes
df["Postal Code"] = df["Postal Code"].fillna("Unknown")

# Save Cleaned Dataset
df.to_csv("Global_Superstore_Cleaned.csv", index=False)

print("Data Cleaning Completed Successfully!")

print("\n========== AUTOMATED REPORT ==========")
print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])
print("Duplicate Rows:", df.duplicated().sum())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nTotal Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
print("Average Sales:", df["Sales"].mean())

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

region_profit = df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(10,5))
region_profit.plot(kind="bar")
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

ship_mode = df["Ship Mode"].value_counts()

plt.figure(figsize=(6,6))
ship_mode.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Ship Mode Distribution")
plt.show()