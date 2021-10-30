import pandas as pd
from scipy import stats
from statsmodels.stats import weightstats as stests
df = pd.read_csv("blood_sugar.csv")
ztest ,pval1 = stests.ztest(df['before'], x2=df['after'], value=0,alternative='two-sided')
#df = pd.read_csv("Vehicle_weights.csv")
#df[['WeightinMotion','StaticWeight']].describe()
#ttest,pval = stats.ttest_rel(df['WeightinMotion'], df['StaticWeight'])
#ztest ,pval1 = stests.ztest(x1=df['WeightinMotion'], x2=df['StaticWeight'])#, value=0,alternative='two-sided')
print("Test statistics",ztest)
print(float(pval1))
if pval1<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")
