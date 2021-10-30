import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
h = [186, 176, 158, 180, 186, 168, 168, 164, 178, 170, 189, 195, 172,
     187, 180, 186, 185, 168, 179, 178, 183, 179, 170, 175, 186, 159,
     161, 178, 175, 185, 175, 162, 173, 172, 177, 175, 172, 177, 180]
h.sort()
hmean = np.mean(h)
print(hmean)
hstd = np.std(h)
print(hstd)
pdf = stats.norm.pdf(h, hmean, hstd)
plt.plot(h, pdf,linewidth=3, color='y') # including h here is crucial
plt.show()



#Standard Normal Distribution
from scipy.stats import norm
fig, ax = plt.subplots()
x= np.arange(-4,4,0.001)
ax.set_title('N(0,$1^2$)')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.plot(x, norm.pdf(x))
ax.set_ylim(0,0.45)
plt.show()

#Normal distribution curve with different standard deviation
fig, ax = plt.subplots()
x = np.linspace(-10,10,100)
stdvs = [1.0, 2.0, 3.0, 4.0]
for s in stdvs:
    ax.plot(x, norm.pdf(x,scale=s), label='stdv=%.1f' % s)    
ax.set_xlabel('x')
ax.set_ylabel('pdf(x)')
ax.set_title('Normal Distribution')
ax.legend(loc='best', frameon=True)
ax.set_ylim(0,0.45)
ax.grid(True)
plt.show()
# cumulative distribution function
cdf=stats.norm.cdf(h,hmean,hstd)
plt.plot(h,cdf,linewidth=3,color='b')
plt.show()
