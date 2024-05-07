# -*- coding: utf-8 -*-
"""LVADSUSR175_Datla_Prahalladh_Predictive_Analytics_IA_1_LAB_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pcx2H4p54eH5Bmh2af01LK7Cw19lCE2K
"""

import pandas as pd
E = pd.read_csv("/content/expenses.csv")
E

E.head()
E.columns

E.info()

E.shape
E.describe()

E.isnull()

E.isnull().sum() #bmi has 16 null values

E.duplicated().sum() # One duplicate removing It

E = E.drop_duplicates()
# Removed dupliacte

E.duplicated().sum()

# EDA
# Univariate Analysis
# Plotting  histograms for numerical columns
import matplotlib.pyplot as plt
import seaborn as sns
for column in E.select_dtypes(include=['float64', 'int64']).columns:
    plt.figure(figsize=(10, 5))
    sns.histplot(E[column])
    plt.title(f'{column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

# Plotting Barplots for categorical columns
for column in E.select_dtypes(include=['object']).columns:
    plt.figure(figsize=(10, 5))
    E[column].value_counts().plot(kind='bar')
    plt.title(f'{column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

#Bi-Variate Analysis
#Correlation between numerical columns
n = E.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = E[n].corr()
print(correlation_matrix)

# heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Heatmap')
plt.show()
# From the correlation we got we can see that age,bmi,children have low correlation towards charges as
# their mutual correlation is near to 0.

# Outlier detection

M= E.select_dtypes(include=['float64', 'int64']).columns

#boxplot
for column in M:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=E[column])
    plt.title(f'{column}')
    plt.xlabel(column)
    plt.show()
# There are no outliers to work on as seen from the boxplot

E.info()
E.isnull().sum()
#Null Values
E["bmi"].value_counts()
#Decided to go with mean
#replacing null values with mean
E["bmi"].fillna(E["bmi"].mean(),inplace = True)

E["bmi"].isnull().sum() #Zero #sucessfully replaced null values with the avg of the column

E.info()
# Charges id the dependent variable
# So Linear Regression
# rest all are independent varaible
# endoing (converting object datatype columns to either int or float)

E["sex"].value_counts()
E["sex"].replace({"male":1,"female":0},inplace = True)
# replacing male to 1 and female to 0

E["sex"].value_counts()
E["smoker"].value_counts()
E["smoker"].replace({"no":0,"yes":1},inplace = True)

E["smoker"].value_counts()
E["region"].value_counts()
#Using LabelEncoder
from sklearn.preprocessing import LabelEncoder
len = LabelEncoder()
E['region'] = len.fit_transform(E['region'])

E["region"].value_counts()
E.info()
# No null values, No duplicates, All columns are encoded to int or float
# Now moving forward towards model implementation

X = E.drop(columns=["charges"]) # assigning X and Y values # For X considering all the independent values
Y = E["charges"]

X.shape

#neccessary libraries for the implementation
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=40)

# Normalizing
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train=pd.DataFrame(scaler.fit_transform(X_train[list(X.columns)]),
                                    columns=X.columns)
X_test=pd.DataFrame(scaler.transform(X_test[list(X.columns)]),
                                    columns=X.columns)

from sklearn.linear_model import LinearRegression
# Linear Regression model
m= LinearRegression()
m.fit(X_train, Y_train)

# Predictions
Y_pred = m.predict(X_test)

#Evaluation metrix
from sklearn.metrics import r2_score,mean_squared_error
mse = mean_squared_error(Y_test, Y_pred)
print("Mean Squared Error:", mse)

rmse = mean_squared_error(Y_test, Y_pred,squared=False)
print("Root Mean Squared Error:", rmse)

# Coefficients and intercepts
print("Coefficients:", m.coef_)
print("Intercept:", m.intercept_)

r2_s = r2_score(Y_test, Y_pred)
print("R2 Score:", r2_s)