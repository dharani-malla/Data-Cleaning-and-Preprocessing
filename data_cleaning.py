import pandas as pd
import numpy as np

# Step 1: Load dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Step 2: Display first 5 rows
print("First 5 rows:")
print(df.head())

# Step 3: Dataset information
print("\nDataset info:")
df.info()

# Step 4: Dataset shape
print("\nShape:")
print(df.shape)

# Step 5: Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Step 6: Handle missing values

# Fill Age with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill Embarked with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Cabin has too many missing values remove the column
df = df.drop('Cabin', axis=1)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Step 7: Check duplicates
print("\nDuplicate rows:")
print(df.duplicated().sum())

# Step 8: Remove duplicates
df = df.drop_duplicates()

print("\nRows after removing duplicates:")
print(df.shape)

# Step 9: Show before normalization
print("\nAge and Fare before normalization:")
print(df[['Age','Fare']].head())

# Normalize features
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

df[['Age','Fare']] = scaler.fit_transform(df[['Age','Fare']])

print("\nAge and Fare after normalization:")
print(df[['Age','Fare']].head())

# Step 10: Handle outliers

print("\nRows before removing outliers:")
print(df.shape)

Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - (1.5 * IQR)
upper = Q3 + (1.5 * IQR)

df = df[(df['Fare'] >= lower) & (df['Fare'] <= upper)]

print("\nRows after removing outliers:")
print(df.shape)

# Step 11: Save cleaned dataset
df.to_csv("Cleaned_Titanic.csv", index=False)

print("\nDataset cleaned successfully")
