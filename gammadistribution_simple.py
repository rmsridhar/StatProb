import numpy as np
from scipy.stats import gamma
from matplotlib import pyplot as plt
x = np.linspace(1E-6, 10, 100)
print(x)
dist = gamma(1, 0, 1)
plt.plot(x, dist.pdf(x), linewidth=3, color='y')
#plt.plot(x, gamma.pdf(x,1,0,1), linewidth=3, color='y')

dist = gamma(2, 0, 1)
plt.plot(x, dist.pdf(x), linewidth=3, color='b',label='alpha=%.1f' % 2)
dist = gamma(3, 0, 1)
plt.plot(x, dist.pdf(x), linewidth=3, color='g',label='alpha=%.1f' % 3)
dist = gamma(4, 0, 1)
plt.plot(x, dist.pdf(x), linewidth=3, color='r',label='alpha=%.1f' % 4)
dist = gamma(5, 0, 1)
plt.plot(x, dist.pdf(x), linewidth=3, color='c',label='alpha=%.1f' % 5)
dist = gamma(6, 0, 1)
plt.plot(x, dist.pdf(x), linewidth=3, color='c',label='alpha=%.1f' % 6)


plt.xlim(0, 10)
plt.ylim(0, 0.45)

plt.xlabel('$x$')
plt.ylabel(r'$p(x|k,\theta)$')
plt.title('Gamma Distribution')

plt.legend(loc=0)
plt.show()
