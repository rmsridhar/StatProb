import pandas as pd
from scipy import stats
from statsmodels.stats import weightstats as stests
x=[86,65,90,75]	
y=[96,80,70,80,91]
#z=[85,90,95,70,70]
#F, p = stats.f_oneway(x,y,z)
F, p = stats.f_oneway(x,y)
print("Statistic Value is ", F)
print("p-value for significance is: ", p)
if p<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")
