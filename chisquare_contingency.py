import numpy as np
a1 = [6, 4, 5, 10]
a2 = [8, 5, 3, 3]
a3 = [5, 4, 8, 4]
a4 = [4, 11, 7, 13]
a5 = [5, 8, 7, 6]
a6 = [7, 3, 5, 9]
val= np.array([a1, a2, a3, a4, a5, a6])
from scipy import stats
#print(stats.chi2_contingency(dice))
#a1=[32,12]
#a2=[14,22]
#a3=[6,9]
#val=np.array([a1,a2,a3])
#print(stats.chi2_contingency(val))
chi2_stat, p_val, dof, ex = stats.chi2_contingency(val)
print("===Chi2 Stat===")
print(chi2_stat)
print("\n")
print("===Degrees of Freedom===")
print(dof)
print("\n")
print("===P-Value===")
print(p_val)
print("\n")
print("===Contingency Table===")
print(ex)
