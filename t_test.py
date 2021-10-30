# paired student's t-test
from numpy.random import seed
from numpy.random import randn
from scipy.stats import ttest_ind
# seed the random number generator seed(1)
# generate two independent samples
#data1 = 5 * randn(100) + 50
#data2 = 5 * randn(100) + 51
data1=[53,56,57,70,70,70,75]
data2=[63,66,67,67,67,68,69,70,72,73,75,76,76,78,79,80,81]
# compare samples
#stat,p = ttest_rel(data1, data2)
stat,p = ttest_ind(data1, data2)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
    print('Same distributions (fail to reject H0)')
else:
    print('Different distributions (reject H0)')
