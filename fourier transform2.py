import numpy as np
from scipy.fftpack import fft, ifft
import scipy.stats as stats
import math
t = np.array([1.0, 2.0, 3.0, 4.0, 5])
x=[]
#for i in range(5):
#    x.append(i)
#    x[i]=i
mean_t=np.mean(t)
var_t=np.var(t)
cos=[]
sin=[]
#normal characteristic function
for i in range(5):
    cos.append(i)
    sin.append(i)
    cos[i]=math.cos(t[i]*mean_t-0.5*var_t*t[i]*t[i])
    sin[i]=math.sin(t[i]*mean_t-0.5*var_t*t[i]*t[i])
    print("direct transform to cosine and sine {0}+i{1}".format(math.cos(i),math.sin(i)))
print(t)
y = fft(t)
print("Fourier transform from t", y)
y1=fft(cos+sin)
print("Fourier transform from cos+sin", y1)

#print("Cosine and Sine data")
#print("{0} +i {1},".format(cos,sin))
#for i in range(5):
 #   print("direct transform to cosine and since {0}+i{1}".format(math.cos(i),math.sin(i)))
yinv = ifft(y)
print("inverse of t",yinv)
y1inv=ifft(y1)
print("Original data of Cos+sin",cos+sin)
print("inverse of cos+sin",y1inv)













