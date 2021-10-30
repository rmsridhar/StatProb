import pandas as pd
from scipy import stats
#df = pd.read_csv("Vehicle_weights.csv")
#df[['WeightinMotion','StaticWeight']].describe()
#ttest,pval = stats.ttest_rel(df['WeightinMotion'], df['StaticWeight'])
df = pd.read_csv("blood_sugar.csv")
df[['before','after']].describe()
ttest,pval = stats.ttest_rel(df['before'], df['after'])
print(ttest)
print(pval)
if pval<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")



