# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 16:53:25 2021

@author: Ahmad Abd Elhameed
"""

import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")

df = df[df['Salary Estimate'] != '-1']

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

k_removed = salary.apply(lambda x: x.replace('K','').replace('$',''))

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)

df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

min_hour = k_removed.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary',''))

df['min_salary'] = min_hour.apply(lambda x: (x.split('-')[0]))
df['max_salary'] = min_hour.apply(lambda x: (x.split('-')[1]))

df['min_salary'] = df['min_salary'].str.replace(r'\D+', '')
df['max_salary'] = df['min_salary'].str.replace(r'\D+', '')

df[["min_salary", "max_salary"]] = df[["min_salary", "max_salary"]].apply(pd.to_numeric)

#df['avg_salary'] = (df['max_salary'] + df['min_salary']) / 2


min_salary = (min_hour.apply(lambda x: (x.split('-')[0]))).str.replace(r'\D+', '')
max_salary = (min_hour.apply(lambda x: (x.split('-')[1]))).str.replace(r'\D+', '')

df.drop(['min_salary',"max_salary"],axis=1,inplace=True)