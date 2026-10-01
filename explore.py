import pandas as pd

df = pd.read_csv("data/train.csv")
print(df.shape)
print(df.columns.tolist())
print(df.head())
df.info()
print(df.isna().sum())
df["Segment"].value_counts()
df["Region"].value_counts()

print(df["Segment"].value_counts())
print(df["Region"].value_counts())
print(df["Category"].value_counts())
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
print(df.groupby(df["Order Date"].dt.year)["Sales"].sum())