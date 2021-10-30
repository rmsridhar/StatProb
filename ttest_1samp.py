from scipy.stats import ttest_1samp
import numpy as np
#ages = np.genfromtxt("body_fat.csv")
ages=[23,22,23,25,25,32,22,28,29,32,24]
#ages1=[23,25,32,28,29]
ages1=[3,5,2,8,9]
#ages = [660149,759822,529826,588718,666383,888950,799112,757679,765153,1297606,989256,1045087]
print(ages)
ages_mean = np.mean(ages)
print(ages_mean)
#tset, pval = ttest_1samp(ages,9747747)
tset, pval = ttest_1samp(ages1,ages_mean)
print("Test Statistics",tset)
print("p-values",pval)
if pval < 0.05:    # alpha value is 0.05 or 5%
   print(" we are rejecting null hypothesis")
else:
  print("we are accepting null hypothesis")
