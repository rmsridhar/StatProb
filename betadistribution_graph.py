import numpy as np
from scipy.stats import beta
from matplotlib import pyplot as plt


#------------------------------------------------------------
# Define the distribution parameters to be plotted
alpha_values = [0.5, 1.5, 3.0, 7.0]
beta_values = [0.5, 1.5, 8.0, 4]
linestyles = ['-', '--', ':', '-.']
color=['y','g','r','b']
x = np.linspace(0, 1, 1002)
print(x)
#------------------------------------------------------------
# plot the distributions
#fig, ax = plt.subplots(figsize=(5, 3.75))

for a, b, ls,c in zip(alpha_values, beta_values, linestyles,color):
    dist = beta(a, b)
    plt.plot(x, dist.pdf(x), ls=ls, c=c,
             label=r'$\alpha=%.1f,\ \beta=%.1f$' % (a, b))
plt.xlim(0, 1)
plt.ylim(0, 10)
plt.xlabel('$x$')
plt.ylabel(r'$p(x|\alpha,\beta)$')
plt.title('Beta Distribution')
plt.legend(loc=0)
plt.show()
