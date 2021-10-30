import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import Axes3D
import scipy.stats as stats

#Dataset

h = [186, 176, 158, 180, 186, 168, 168, 164, 178, 170, 189, 195, 172,
     187, 180, 186, 185, 168, 179, 178, 183, 179, 170, 175, 186, 159,
     161, 178, 175, 185, 175, 162, 173, 172, 177, 175, 172, 177, 180]
h.sort()
#Create grid and multivariate normal
x=h
y=h
z=h
pdf_x = stats.norm.pdf(x, np.mean(x), np.std(x))
pdf_y =stats.norm.pdf(y, np.mean(y), np.std(y))
plt.plot(x,pdf_x,linewidth=3,color='y')
plt.show()
plt.plot(y,pdf_y,linewidth=3,color='b')
plt.show()
X, Y, Z = np.meshgrid(x,y,z)
pos = np.empty(X.shape + (3,))
pos[:, :, :,0] = X; pos[:, :,:, 1] = Y; pos[:, :,:, 2] = Z
#rv = multivariate_normal([mu_x, mu_y], [[variance_x, 0], [0, variance_y]])
rv = multivariate_normal([np.mean(x), np.mean(y),np.mean(z)], [[np.var(x), 0,0], [0, np.var(y),0],[0,0,np.var(z)]])
#Make a 3D plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, rv.pdf(pos),cmap='viridis',linewidth=0)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.show()
