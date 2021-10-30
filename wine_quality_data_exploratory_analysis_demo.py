import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('winequality-red.csv')

# number of data in the table
print(df.shape)
# number of datatypes in the table
print(df.dtypes)

# min,mean,median,1st quartile, 2nd quartile, 3rd quartile
df.describe()
#Correlation
df4=df.corr()
print(df4)

#Filtering numerical data
df_numerics_only = df.select_dtypes(include=[np.number])
df_numerics_only
print(df_numerics_only.head())
df3=df_numerics_only.columns.values
print(len(df3))
fig=plt.figure(figsize=(10,10))
rows=2
cols=np.absolute(len(df3)/rows)+1
#probability distribution plot
for i in range(len(df3)):
    plt.subplot(rows,cols,i+1)
    sns.distplot(df[df3[i]],kde=True)

plt.show()
# linear regression
from statsmodels.graphics.gofplots import qqplot
for i in range(len(df3)):
    qqplot(df[df3[i]], line='s')
    plt.xlabel(df3[i])
    plt.show()

#df5=df.groupby('quality').count()


#----------------------
# Complete Exploratory Analysis
#----------------------

