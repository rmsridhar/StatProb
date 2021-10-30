import numpy as np
from matplotlib import pyplot as plt
import math
lambda1_values = [0.5, 1.0, 1.5, 2,2.5]
linestyles = ['-', '--', ':', '-.','..-']
color=['y','g','r','b','m']
x=np.arange(0,15,0.1)
for a,b,c in zip(lambda1_values,linestyles,color):
    y=a * np.exp(-a*x)
    plt.plot(x, y, linewidth=3,color=c,label='$\lambda$=%.1f' % (a))
plt.xlabel('$x$')
plt.ylabel(r'$p(x|\lambda)$')
plt.title('Exponential Distribution')
plt.legend(loc=0)
plt.show()
