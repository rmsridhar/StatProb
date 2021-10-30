from scipy import stats
import pandas as pd
x=[18.3,13.3,16.5,12.8,9.5,13.6,8.1,8.9,10,8.3,7.9,8.1,13.4]
y=[12.7,11.1,15.3,12.7,10.5,15.6,11.2,14.2,16.2,15.5,19.9,20.4,36.1]
print(stats.wilcoxon(x, y))

df = pd.read_csv("blood_pressure1.csv")
#print(df.describe())
x=df['bp_before']
y=df['bp_after']
print(stats.wilcoxon(x, y))
#print(df[['bp_before','bp_after']].describe())
