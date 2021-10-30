import numpy as np
from scipy.stats import gamma
from matplotlib import pyplot as plt
x = np.linspace(1E-6, 10, 100)
print(x)
dist = gamma(1, 0, 1)
plt.plot(x, dist.pdf(x), linewidth=3, color='y',label='lambda %s' %1)
#plt.plot(x, gamma.pdf(x,1,0,1), linewidth=3, color='y')

dist = gamma(1, 0, 2)
plt.plot(x, dist.pdf(x), linewidth=3, color='b',label='lambda %s' %2)
dist = gamma(1, 0, 3)
plt.plot(x, dist.pdf(x), linewidth=3, color='g',label='lambda %s' %3)
dist = gamma(1, 0, 4)
plt.plot(x, dist.pdf(x), linewidth=3, color='r',label='lambda %s' %4)
dist = gamma(1, 0, 5)
plt.plot(x, dist.pdf(x), linewidth=3, color='c',label='lambda %s' %5)
dist = gamma(1, 0, 6)
plt.plot(x, dist.pdf(x), linewidth=3, color='c',label='lambda %s' %6)



plt.xlim(0, 10)
plt.ylim(0, 0.45)

plt.xlabel('$x$')
plt.ylabel(r'$p(x|k,\theta)$')
plt.title('Gamma Distribution')

plt.legend(loc=0)
plt.show()
