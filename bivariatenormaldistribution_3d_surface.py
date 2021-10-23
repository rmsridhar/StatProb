from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from matplotlib import cm
import math
#def f(x, y):
#    return np.sin(np.sqrt(x ** 2 + y ** 2))
def f(x,y):
    t=np.exp(-0.5*x**2-0.5*y**2)/(2*np.pi)
    return t
#x = np.linspace(-6, 6, 30)
#y = np.linspace(-6, 6, 30)
#h = [186, 176, 158, 180, 186, 168, 168, 164, 178, 170, 189, 195, 172,
#     187, 180, 186, 185, 168, 179, 178, 183, 179, 170, 175, 186, 159,
#     161, 178, 175, 185, 175, 162, 173, 172, 177, 175, 172, 177, 180]
h=[-10,10,-11,12,12,-13,20,22,34,-11,-45,-18,-10,8,-10,10,-11,12,12,-13,20,22,34,
   -11,-45,-18,-10,8,-10,10,-11,12,12,-13,20,22,34,-11,-45,-18,-10,8]
h.sort()

x=h
y=h
#print("mean=",np.mean(x),"var=",np.var(x))
#pdfx=stats.norm.pdf(x,np.mean(x),np.std(x))
pdfx=stats.norm.pdf(x,np.mean(x),1)
plt.plot(x, pdfx,linewidth=3, color='y') # including h here is crucial
plt.show()
#pdfy=stats.norm.pdf(y,np.mean(y),np.std(y))
pdfy=stats.norm.pdf(y,np.mean(y),1)
plt.plot(y, pdfy,linewidth=3, color='b') # including h here is crucial
plt.show()
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
#ax.contour3D(X, Y, Z, 50, cmap=cm.coolwarm,linewidth=1)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
