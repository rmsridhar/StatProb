import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('winequality-white.csv',sep=';')
print(df.head())
l = df.columns.values
print(l)
#number_of_columns=12
#number_of_rows = len(l)-1/number_of_columns
plt.figure(figsize=(100,100))
sns.distplot(df[l[0]],kde=True)
plt.show()
sns.distplot(df[l[1]],kde=True)
plt.show()
for i in range(0,len(l)):
    sns.distplot(df[l[i]],kde=True)
    plt.show()
    
   # plt.subplot(number_of_rows + 1,number_of_columns,i+1)
   # sns.distplot(df[l[i]],kde=True)
   # plt.show()
