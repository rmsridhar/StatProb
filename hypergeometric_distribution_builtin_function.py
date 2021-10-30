from scipy.stats import hypergeom
import matplotlib.pyplot as plt
import numpy as np
#[M, n, N] = [20, 7, 12]
[M,n,N]=[10,3,4]
rv = hypergeom(M, n, N)
x = np.arange(0, n+1)
pmf_dogs = rv.pmf(x)
print(pmf_dogs)
mean,var,skew,kurt=hypergeom.stats(M,n,N,moments='mvsk')
print(mean,var,skew,kurt)
