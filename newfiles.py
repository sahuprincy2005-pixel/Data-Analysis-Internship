import pandas as pd

df = pd.read_csv("/storage/emulated/0/New folder/Projects/Messy_Employee_dataset.csv")

print(df.head())
print(df.shape)
print( df.info())
print( df.columns)
print ( df)
print( df.isnull().sum())

print(df.duplicated().sum())
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print(df.isnull().sum())

print(df.duplicated().sum())
df.to_csv("/storage/emulated/0/New folder/Projects/Messy_Employee_dataset.csv", index=False)

print("Dataset cleaned and saved successfully!")
print(df.shape)

print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df["Status"].value_counts())
print(df["Remote_Work"].value_counts())
print(df["Department_Region"].value_counts())
print("Average Salary:", df["Salary"].mean())

print("Highest Salary:", df["Salary"].max())

print("Lowest Salary:", df["Salary"].min())
print("Average Age:", df["Age"].mean())

print("Youngest Employee:", df["Age"].min())

print("Oldest Employee:", df["Age"].max())
import os
df.to_csv("Cleaned_Employee_Dataset.csv", index=False)

import os
print(os.listdir())
print(df.isnull().sum())

