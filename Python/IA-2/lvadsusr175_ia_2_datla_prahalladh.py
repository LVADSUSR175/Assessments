# -*- coding: utf-8 -*-
"""LVADSUSR175_IA_2_DATLA_PRAHALLADH.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C019_yRu-02V0WDF9BFDOmSLQQSKdD-l
"""

# 1
import numpy as np
arr1 = np.array([1,2,3,4])
print(arr1)
print(min(arr1))
print(max(arr1))
print(sum(arr1))
print(np.mean(arr1))
print(np.std(arr1))

# 2
health_data = np.array([[160, 70, 30],   # height, weight, age for individual 1
                        [165, 65, 35],   # height, weight, age for individual 2
                        [170, 75, 40]])  # height, weight, age for individual 3


def normalize(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    normalized_data = (data - mean) / std_dev
    return normalized_data


normalized_data = normalize(health_data)
print(normalized_data)

# 3
def calculate(scores):
    last_three= scores[:, -3:]
    valid_scores = np.ma.masked_equal(last_three, -1)
    average_scores = valid_scores.mean(axis=1)
    return average_scores


scores = np.array([[70, 72, 91, 0, -1],
                   [-1, -1, 56, 33, 74],
                   [70, 75, 92, 82, 94]])

average_last_three_subjects = calculate(scores)
print(average_last_three_subjects)

#4

def monthly_adjustments(city_temperatures, adjustment_factors):
    adjusted = city_temperatures + adjustment_factors
    return adjusted

city_temperatures = np.array([[12, 24, 23, 15],
                               [26, 50, 34, 18],
                               [24, 42, 55, 28]])

adjustment_factors = np.array([1.5, 2.0, 1.0, 1.2])
adjusted = monthly_adjustments(city_temperatures, adjustment_factors)
print(adjusted)

# 5
import numpy as np
daily_closing_prices = np.array([100, 102, 98, 105, 107, 110, 108, 112, 115, 118, 120])
window_size = 5
df5 = pd.DataFrame(daily_closing_prices)
df5.rolling(window =5).mean()

# 6
mean_vector = [0,0]
covariance_matrix = [[1,0.5],[0.5,2]]

# 7
import numpy as np
properties_matrix = np.array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]])
properties_matrix.size

# 8
arr8 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
arr8.shape
for (i > 5) in arr8:
  print(arr8[i])

# 9
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Age': [25, 30, 35, 40, 45, 50, 55],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Miami', 'Boston'],
        'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales', 'IT', 'HR']}

import pandas as pd
data_df = pd.DataFrame(data)
data_df.head()
filt = (data_df['Age'] < 45) & (data_df['Department'] != 'HR')
data_df.loc[filt,["Name","City"]]

# 10
data1 = {'Department': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Home Goods'],
        'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Sales': [70000, 50000, 30000, 40000, 60000]}
sales = pd.DataFrame(data1)
sales.head()
sales_grouped = sales.groupby(["Department","Salesperson"]).aggregate({"Sales":"mean"})
sales_grouped

# 11
data2 = {
    'Product': ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Flour', 'Grapes'],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit', 'Bakery', 'Fruit'],
    'Price': [1.20, 0.50, 3.00, 2.50, 4.00, 1.50, 2.00],
    'Promotion': [True, False, True, True, False, True, False]
}

df = pd.DataFrame(data2)
fruit_df = df[df['Category'] == 'Fruit']
average_price = fruit_df['Price'].mean()
pp = fruit_df[(fruit_df['Price'] > average_price) & (~fruit_df['Promotion'])]
print(pp)

# 12
employee_data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'IT', 'Finance', 'IT'],
    'Manager': ['John', 'Rachel', 'Emily', 'Rachel']
}

# Dataset of employee project assignments
project_data = {
    'Employee': ['Alice', 'Charlie', 'Eve'],
    'Project': ['P1', 'P3', 'P2']
}


employee_df = pd.DataFrame(employee_data)
project_df = pd.DataFrame(project_data)

merged_df = pd.merge(project_df, employee_df, on='Employee', how='left')
merged_df['Department'] = merged_df['Department']
merged_df['Manager'] = merged_df['Manager']
department_overview = merged_df.groupby(['Department', 'Manager'])['Project'].apply(list).reset_index()
print(department_overview)

# 13
D13 = pd.read_csv("/content/Q13_sports_team_stats.csv")
D13.head(15)
D13_grouped=D13.groupby(["TeamID"])
D13_grouped.head()
D13["Win_Ratio"] = D13["GamesPlayed"] / D13["Wins"]
print(D13)

# 14
D14 = pd.read_csv("/content/Q14_customer_purchases.csv")
D14.head(20)
D14_Before = D14["Date"]  < D14["LoyaltyProgramSignUp"]

# 15
D15 = pd.read_csv("/content/Q15_student_grades.csv")
D15.head()
D15_grouped = D15.groupby("Subject").aggregate({"Grade":"mean"})
D15_grouped