import pandas as pd

df = pd.read_csv("blood_pressure1.csv")
#print(df.describe())
print(df[['bp_before','bp_after']].describe())
from scipy import stats
import matplotlib.pyplot as plt

#First thing we need to do is import the stats library and then test the assumptions of the paired samples t-test.
#First let’s check for any significant outliers in each of the variables.
df[['bp_before', 'bp_after']].plot(kind='box')
plt.show()
df['bp_difference'] = df['bp_before'] - df['bp_after']
#histogram
df['bp_difference'].plot(kind='hist', title= 'Blood Pressure Difference Histogram')
plt.show()
#Remember that for the dependent sample T-test the normality check needs to be conducted
#on differences between the two scores. There are a few ways one can test this assumption
#– make a histogram, use a Q-Q plot, and/or
#use a statistical test. Let’s create a variable for the differences and run through these.
stats.probplot(df['bp_difference'], plot= plt)
plt.title('Blood pressure Difference Q-Q Plot')
plt.show()
#There is some deviation from normality, but it does not appear to be severe
#so there is no need to worry. To be sure, let’s test this statistically to see
#if the data is normally distributed. To test this, one can use the Shapiro-Wilk test
#for normality. Unfortunately the output is not labeled.
#The first value is the W test value, and the second value it the p-value.

print("Shapiro test", stats.shapiro(df['bp_difference']))
print("Normality test",stats.normaltest(df['bp_difference']))
#The test was non-significant. Therefore, the difference between the two conditions
#is normally distributed. If this test were to be significant,
#an appropriate alternative to use would be the Wilcoxon signed-rank Test.


print(stats.ttest_rel(df['bp_before'], df['bp_after']))
#The findings are statistically significant! One can reject the null hypothesis
#in support of the alternative.
#A paired sample t-test was used to analyze the blood pressure before
#and after the intervention to test if the intervention had a significant affect
#on the blood pressure. The blood pressure before the intervention was higher
#(156.45 ± 11.39 units) compared to the blood pressure post intervention
#(151.36 ± 14.18 units); there was a statistically
#significant decrease in blood pressure (t(119)=3.34, p= 0.0011) of 5.09 units.







