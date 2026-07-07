import pandas as pd

encodings = ["utf-8", "cp1252", "latin1", "ISO-8859-1"]

for enc in encodings:
    try:
        print(f"Trying encoding: {enc}")
        df = pd.read_csv("../dataset/Superstore.csv", encoding=enc)
        print(f"\n✅ Success! File opened using {enc}")
        print(df.head())
        break
    except Exception as e:
        print(f"❌ {enc}: {e}")
        import pandas as pd

# Load dataset
df = pd.read_csv("../dataset/Superstore.csv", encoding="cp1252")

print("="*50)
print("SALES & REVENUE ANALYSIS DASHBOARD")
print("="*50)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert Order Date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# ================= KPIs =================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
average_sales = df["Sales"].mean()

print("\n========== KPI ==========")

print(f"Total Sales   : ${total_sales:,.2f}")
print(f"Total Profit  : ${total_profit:,.2f}")
print(f"Total Orders  : {total_orders}")
print(f"Average Sales : ${average_sales:.2f}")

# ================= Region Sales =================

print("\nSales by Region")

print(df.groupby("Region")["Sales"].sum())

# ================= Category Sales =================

print("\nSales by Category")

print(df.groupby("Category")["Sales"].sum())

# ================= Top Products =================

print("\nTop 10 Products")

print(df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10))