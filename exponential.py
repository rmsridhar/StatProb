import numpy as np
from scipy.stats import beta
from matplotlib import pyplot as plt
import math
lambda1=2.5

x=np.arange(0,15,0.1)
y=lambda1 * np.exp(-lambda1*x)
plt.plot(x,y,linewidth=3,color='y',label=r'$\lambda$=%.1f' % (lambda1))
plt.title('Exponential:$\lambda$=%.2f'%lambda1)
#plt.xlabel('x')
#plt.ylabel('Probability density')

plt.legend(loc=0)
plt.show()
