# Titanic Dataset - Data Cleaning and Preprocessing

## Project Overview
This project performs data cleaning and preprocessing on the Titanic dataset using Python and Pandas.

The goal is to improve data quality by handling missing values, removing duplicates, normalizing features, and handling outliers.


## Dataset Information

Dataset Name: Titanic Dataset

Total Rows: 891

Total Columns: 12

Columns:
- PassengerId
- Survived
- Pclass
- Name
- Sex
- Age
- SibSp
- Parch
- Ticket
- Fare
- Cabin
- Embarked


## Steps Performed

### 1. Loaded Dataset
Loaded the Titanic dataset using Pandas.

### 2. Displayed Dataset Information
- Displayed first 5 rows
- Checked dataset shape
- Displayed column details and data types

### 3. Handled Missing Values
Missing values found:
- Age → 177
- Cabin → 687
- Embarked → 2

Actions performed:
- Filled Age missing values using Mean
- Filled Embarked missing values using Mode
- Removed Cabin column due to excessive missing values

### 4. Checked and Removed Duplicates
- Checked duplicate rows
- Removed duplicate records if found

### 5. Normalized Features
Used MinMaxScaler to normalize:
- Age
- Fare

Converted values into range:
0 to 1

### 6. Handled Outliers
Used IQR (Inter Quartile Range) method on Fare column to remove outliers.

### 7. Saved Cleaned Dataset
Saved processed dataset as:

Cleaned_Titanic.csv

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn

## Files Included

- Titanic-Dataset.csv
- Titanic_Preprocessing.py
- Cleaned_Titanic.csv
- README.md

## Output

Successfully cleaned and preprocessed Titanic dataset for analysis and machine learning tasks.