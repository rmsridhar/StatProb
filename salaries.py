import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('Salaries1.csv')
#print(df.head())
df1=df.groupby('rank').count()
print(df1.head())
df1=df.groupby(['rank','Gender']).count()
print(df1)
df1=df.groupby(['rank','Gender']).describe()
print(df1)                
df1=df.groupby(['rank','Gender','discipline'])['salary'].mean()
print(df1)
df1=df.groupby(['rank','Gender','discipline'])['salary'].agg([np.sum, np.mean, np.std,np.count_nonzero])
print(df1)
df6=df['yrs.since.phd']-df['yrs.service']
print(df6)
df7=df.corr()
print(df7)
#df7.to_csv("corr_salary1.csv")
df7.to_excel("corr_salary.xlsx",sheet_name='corr_salary')
