import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import scatter_matrix
np.random.seed(1)

# 1000 random integers between 0 and 50
x = np.random.randint(0, 50, 1000)

# Positive Correlation with some noise
y = x + np.random.normal(0, 10, 1000)

print(np.corrcoef(x, y))
plt.scatter(x,y)
plt.show()

# Negative Correlation
y = 100 - x + np.random.normal(0, 5, 1000)

print(np.corrcoef(x, y))
plt.scatter(x,y)
plt.show()

# No difference in the correlation
y = np.random.randint(0, 50, 1000)

print(np.corrcoef(x, y))
plt.scatter(x,y)
plt.show()


df = pd.DataFrame({'a': np.random.randint(0, 50, 1000)})
df['b'] = df['a'] + np.random.normal(0, 10, 1000) # positively correlated with 'a'
df['c'] = 100 - df['a'] + np.random.normal(0, 5, 1000) # negatively correlated with 'a'
df['d'] = np.random.randint(0, 50, 1000) # not correlated with 'a'

print(df.corr())
scatter_matrix(df, figsize=(6, 6))
plt.show()


