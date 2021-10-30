import pandas as pd
from scipy import stats
from statsmodels.stats import weightstats as stests
df = pd.read_csv("blood_sugar.csv")
ztest ,pval = stests.ztest(df['before']) #, x2=None, value=0)
print(float(pval))
print(ztest)
if pval<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")
