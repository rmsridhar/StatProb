import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
from scipy import stats
datafile = "gender.csv"
data = pd.read_csv(datafile)
N = len(data.Score)
df_a = len(data.Gender.unique()) - 1
df_b = len(data.Agegroup.unique()) - 1
df_axb = df_a*df_b 
df_w = N - (len(data.Gender.unique())*len(data.Agegroup.unique()))
print(df_a,df_b,df_axb,df_w)
grand_mean = data['Score'].mean()
print(grand_mean)
ssq_a = sum([(data[data.Gender ==l].Score.mean()-grand_mean)**2 for l in data.Gender])
print(ssq_a)
#print(data[data.Gender=='Boys'])
ssq_b = sum([(data[data.Agegroup ==l].Score.mean()-grand_mean)**2 for l in data.Agegroup])
#print(data[data.Agegroup=='10years'])
# =='10years'].Score.mean()-grand_mean))
print(ssq_b)
ssq_t = sum((data.Score - grand_mean)**2)
print(ssq_t)
vc = data[data.Gender == 'Boys']
oj = data[data.Gender == 'Girls']
vc_Agegroup_means = [vc[vc.Agegroup == d].Score.mean() for d in vc.Agegroup]
oj_Agegroup_means = [oj[oj.Agegroup == d].Score.mean() for d in oj.Agegroup]
ssq_w = sum((oj.Score - oj_Agegroup_means)**2) +sum((vc.Score - vc_Agegroup_means)**2)
print(ssq_w)
ssq_axb = ssq_t-ssq_a-ssq_b-ssq_w
ms_a = ssq_a/df_a
ms_b = ssq_b/df_b
ms_axb = ssq_axb/df_axb
ms_w = ssq_w/df_w
print("ms_A {0},ms_b {1},ms_w {2}".format(ms_a,ms_b,ms_w))
f_a = ms_a/ms_w
f_b = ms_b/ms_w
f_axb = ms_axb/ms_w
p_a = stats.f.sf(f_a, df_a, df_w)
p_b = stats.f.sf(f_b, df_b, df_w)
p_axb = stats.f.sf(f_axb, df_axb, df_w)
results = {'sum_sq':[ssq_a, ssq_b, ssq_axb, ssq_w],
           'df':[df_a, df_b, df_axb, df_w],
           'Mean Square':[ms_a,ms_b,ms_axb,ms_w],
           'F':[f_a, f_b, f_axb, 'NaN'],
            'PR(>F)':[p_a, p_b, p_axb, 'NaN']}
columns=['sum_sq', 'df', 'Mean Square','F', 'PR(>F)']

aov_table1 = pd.DataFrame(results, columns=columns,
                          index=['Gender', 'Age', 
                          'Gender:Age', 'Residual'])
print(aov_table1)
formula = 'Score ~ C(Gender) + C(Agegroup) + C(Gender):C(Agegroup)'
model = ols(formula, data).fit()
aov_table = anova_lm(model, type=2)
print(aov_table)

