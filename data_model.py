# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 06:44:50 2021

@author: Ahmad Abd Elhameed
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("eda_df.csv")
df.drop(['index','Unnamed: 0'],axis=1,inplace=True)

## choose revelant columns
df_model = df[['Rating','Size', 'Founded',
       'Type of ownership', 'Industry', 'Sector', 'Revenue', 'Competitors',
       'hourly', 'employer_provided',
       'company_name', 'job_state', 'same_state', 'age', 'python', 'math',
       'data_analysis', 'database', 'Power_BI', 'tableau', 'MATLAB', 'word',
       'excel', 'spark', 'r_studio', 'aws', 'azure', 'title_simp', 'seniority',
       'comp_count', 'job_desc_len', 'avg_salary']]

## create dummy data
df_dummy = pd.get_dummies(df_model)

## train test split
from sklearn.model_selection import train_test_split
X = df_dummy.drop('avg_salary',axis=1)
y = df_dummy['avg_salary'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

## muliple linear regression  stats
import statsmodels.api as sm

X_sm = X = sm.add_constant(X)

model = sm.OLS(y, X)
result = model.fit().summary()

## sklearn linear regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

reg = LinearRegression()
reg.fit(X_train, y_train)

print(np.mean(cross_val_score(reg,X_train,y_train,scoring='neg_mean_absolute_error',cv=3)))


## sklearn lasso regression
from sklearn.linear_model import Lasso

las_model = Lasso()
las_model.fit(X_train, y_train)
print(np.mean(cross_val_score(las_model,X_train,y_train,scoring='neg_mean_absolute_error',cv=3)))



alpha = []
error = []

for i in range (1,100):
    alpha.append(i/100)
    lml = Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(lml,X_train,y_train,scoring='neg_mean_absolute_error',cv=3)))

plt.plot(alpha,error)


err = tuple(zip(alpha,error))
df_err = pd.DataFrame(err,columns=['alpha','error'])
df_err[df_err.error == max(df_err.error)]

## random forest
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor()


np.mean(cross_val_score(rf,X_train,y_train,scoring='neg_mean_absolute_error',cv=3))





