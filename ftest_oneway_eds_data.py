import pandas as pd
from scipy import stats
from statsmodels.stats import weightstats as stests
import numpy as np
from scipy.stats import ttest_ind


Friday=[344240.517,521255.393,359796.552,396264.84,753608.63,412430.581,
        434484.63,440871.55,511476.462,491521.126,629902.882,499558.541]

Monday=[360485.9,315524.705,272967.349,388524.884,630076.58,515345.085,
        404355.386,370694.755,383563.165,515493.125,427903.32,440810.118]
Saturday=[472511.442,484268.75,	616175.87,423179.718,861823.55,611786.739,
          538951.837,529860.345,628071.1,531775.096,551005.77,807390.589]
Sunday	=[614313.5335,488113.21,681452.143,478555.84,685513.1325,701062.203,
          545197.915,587776.531,724870.034,570883.34,564881.999,842918.812]
Thursday=[312444.886,472534.994,395084.12,397334.14,476826.155,430294.2465,
          474067.003,420495.415,365172.654,466400.585,584700.524,487653.491]
Tuesday=[419817.764,493496.991,294824.105,468950.189,362013.443,402337.673,
         587596.888,434044.67,383309.68,524660.919,450814.695,456061.48]
Wednesday=[289539.735,384805.999,330680.061,460410.625,322802.935,390657.92,
           493757.453,334892.386,375920.94,410605.713,606084.305,464970.971]



F, p = stats.f_oneway(Friday,Monday,Saturday,Sunday,Thursday,Tuesday,Wednesday)

#F, p = stats.f_oneway(overcast,rainy,sunny)
print("F statistics",F)
print("p-value for significance is: ", p)
if p<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")

ttest,pval = ttest_ind(Friday,Monday)
print("ttest of Friday , Monday:",ttest)
print("p-value of Friday,Monday",pval)

df = pd.DataFrame()
df['Monday'] = Monday
df['Tuesday'] = Tuesday
df['Wednesday'] = Wednesday
df['Thursday'] = Thursday
df['Friday']=Friday
df['Saturday']=Saturday
df['Sunday']=Sunday

# Stack the data (and rename columns):

stacked_data = df.stack().reset_index()
stacked_data = stacked_data.rename(columns={'level_0': 'id',
                                            'level_1': 'Day',
                                            0:'result'})
# Show the first 8 rows:

print (stacked_data.head(8))

from statsmodels.stats.multicomp import (pairwise_tukeyhsd,
                                         MultiComparison)

# Set up the data for comparison (creates a specialised object)
MultiComp = MultiComparison(stacked_data['result'],
                            stacked_data['Day'])

# Show all pair-wise comparisons:

# Print the comparisons

print(MultiComp.tukeyhsd().summary())


#The Holm-Bonferroni method is an alterantive method.

comp = MultiComp.allpairtest(stats.ttest_rel, method='Holm')
print (comp[0])
