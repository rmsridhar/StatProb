import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
#from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import scipy.stats as stats


#%a=np.array([[11,12,15,14,23],[10,11,13,24,23]])
#%b=np.array([[12,21,22,16,34],[10,11,13,24,23]])
#a=np.array([11,12,15,14,23])
#b=np.array([12,21,22,16,34])
#h=[-10,10,-11,12,12,-13,20,22,34,-11,-45,-18,-10,8,-10,10,-11,12,12,-13,20,22,34,
   #-11,-45,-18,-10,8,-10,10,-11,12,12,-13,20,22,34,-11,-45,-18,-10,8]
#h.sort()

h = [186, 176, 158, 180, 186, 168, 168, 164, 178, 170, 189, 195, 172,
     187, 180, 186, 185, 168, 179, 178, 183, 179, 170, 175, 186, 159,
     161, 178, 175, 185, 175, 162, 173, 172, 177, 175, 172, 177, 180]
h.sort()
#x = np.linspace(-0.5,1.5,500)
#x=np.arange(-3, 3, 0.001)
#y = np.linspace(-0.5,1.5,500)
#y=np.arange(-5,5,0.001)
a=h
b=h
#a=x
#b=y
a_mean=np.mean(a)
b_mean=np.mean(b)
a_std=np.std(a)
b_std=np.std(b)
a_var=np.var(a)
b_var=np.var(b)
pdf_a = stats.norm.pdf(a, a_mean, a_std)
pdf_b =stats.norm.pdf(b,b_mean,b_std)
corr=np.corrcoef(a,b)
print(corr[0][1])
z1=(((a-a_mean)**2)/a_var)
z2=(((b-b_mean)**2)/b_var)
a1=a-a_mean
b1=b-b_mean
c1=a1*b1
z3=(2*corr[0][1]/(a_std*b_std))*c1
z=z1-z3+z2
#print("z=",z)
c=2*np.pi*a_std*b_std*math.sqrt(1-corr[0][1]*corr[0][1])
c3=2*(1-(corr[0][1]*corr[0][1]))
zx=-z/c3
#print("zx=",zx)
#print("len of zx",len(zx))
d=[]
for i in range(len(zx)):
    d.append(i)
    d[i]=math.exp(zx[i])
    
print(d)
e=d/c
print("x=",pdf_a)
print("y=",pdf_b)
pdf_e=stats.norm.pdf(e, np.mean(e), np.std(e))
print("Bivariate=",pdf_e)

plt.plot(a,pdf_a,linewidth=3,color='g')
plt.show()
plt.plot(b,pdf_b,linewidth=3,color='r')
plt.show()
plt.plot(e,pdf_e,linewidth=3,color='b')
plt.show()
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(pdf_a, pdf_b, pdf_e, 'gray')
plt.show()




