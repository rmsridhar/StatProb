# generate a sample of random gaussians
from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot
import numpy as np


# seed the random number generator seed(1)
# generate univariate observations
data = 5 * randn(10000) + 50
print(np.mean(data))
print(np.var(data))
# histogram of generated data
pyplot.hist(data,bins=100)
pyplot.show()
