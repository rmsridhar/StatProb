import numpy as np
import scipy.stats as stats
from scipy.stats import ttest_ind
import pandas as pd
# Create four random groups of data with a mean difference of 1

mu, sigma = 10, 3 # mean and standard deviation
group1 = np.random.normal(mu, sigma, 50)

mu, sigma = 11, 3 # mean and standard deviation
group2 = np.random.normal(mu, sigma, 50)

mu, sigma = 12, 3 # mean and standard deviation
group3 = np.random.normal(mu, sigma, 50)

mu, sigma = 13, 3 # mean and standard deviation
group4 = np.random.normal(mu, sigma, 50)

# Show the results for Anova

F_statistic, pVal = stats.f_oneway(group1, group2, group3, group4)

print ('P value of F-oneway:')
print (pVal)
ttest,pval = ttest_ind(group1,group2)
print("ttest of group1,group2:",ttest)
print("p-value of group1,group2",pval)

ttest,pval = ttest_ind(group1,group3)
print("ttest of group1,group3:",ttest)
print("p-value of group1,group3",pval)

ttest,pval = ttest_ind(group1,group4)
print("ttest of group1,group4:",ttest)
print("p-value of group1,group4",pval)


#For the multicomparison tests we will put the data into a dataframe.
#And then reshape it to a stacked dataframe

# Put into dataframe

df = pd.DataFrame()
df['treatment1'] = group1
df['treatment2'] = group2
df['treatment3'] = group3
df['treatment4'] = group4

# Stack the data (and rename columns):

stacked_data = df.stack().reset_index()
stacked_data = stacked_data.rename(columns={'level_0': 'id',
                                            'level_1': 'treatment',
                                            0:'result'})
# Show the first 8 rows:

print (stacked_data.head(8))

from statsmodels.stats.multicomp import (pairwise_tukeyhsd,
                                         MultiComparison)

# Set up the data for comparison (creates a specialised object)
MultiComp = MultiComparison(stacked_data['result'],
                            stacked_data['treatment'])

# Show all pair-wise comparisons:

# Print the comparisons

print(MultiComp.tukeyhsd().summary())


#The Holm-Bonferroni method is an alterantive method.

comp = MultiComp.allpairtest(stats.ttest_rel, method='Holm')
print (comp[0])
