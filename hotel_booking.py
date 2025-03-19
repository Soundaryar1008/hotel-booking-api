import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv(r"C:\Users\soundarya\hotel-booking-qa\cleaned_hotel_bookings.csv")

# ---------------- OLD VISUALIZATIONS ----------------
# Correlation heatmap
plt.figure(figsize=(12, 6))
numeric_df = df.select_dtypes(include=['number'])  # Select only numerical columns
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap (Numerical Features Only)")
plt.show()


# Booking cancellation count
plt.figure(figsize=(8, 5))
sns.countplot(x='is_canceled', data=df, palette='viridis')
plt.title("Booking Cancellations")
plt.xlabel("Canceled (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()

# ---------------- NEW ADVANCED ANALYSIS ----------------
# 1️⃣ Lead time vs. ADR
plt.figure(figsize=(10, 5))
sns.scatterplot(x=df['lead_time'], y=df['adr'], alpha=0.5)
plt.title("Lead Time vs. ADR (Average Daily Rate)")
plt.xlabel("Lead Time (days)")
plt.ylabel("ADR ($)")
plt.show()

# 2️⃣ Market Segment Distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='market_segment', data=df, palette='Set2', order=df['market_segment'].value_counts().index)
plt.xticks(rotation=45)
plt.title("Market Segment Distribution")
plt.xlabel("Market Segment")
plt.ylabel("Number of Bookings")
plt.show()

# 3️⃣ Deposit Type Impact on Cancellations
plt.figure(figsize=(8, 5))
sns.countplot(x='deposit_type', hue='is_canceled', data=df, palette='coolwarm')
plt.title("Deposit Type vs. Booking Cancellations")
plt.xlabel("Deposit Type")
plt.ylabel("Number of Bookings")
plt.legend(title="Canceled", labels=["No", "Yes"])
plt.show()

# 4️⃣ Average Daily Rate (ADR) per Hotel Type
plt.figure(figsize=(8, 5))
sns.boxplot(x='hotel', y='adr', data=df, palette='muted')
plt.title("ADR Comparison for City vs. Resort Hotels")
plt.xlabel("Hotel Type")
plt.ylabel("ADR ($)")
plt.show()

# 5️⃣ Special Requests vs. Cancellations
plt.figure(figsize=(8, 5))
sns.boxplot(x='is_canceled', y='total_of_special_requests', data=df, palette='pastel')
plt.title("Special Requests vs. Cancellation Rate")
plt.xlabel("Canceled (0 = No, 1 = Yes)")
plt.ylabel("Total Special Requests")
plt.show()

print("✅ Analysis complete! All visualizations generated.")
