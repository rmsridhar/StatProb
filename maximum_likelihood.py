import numpy as np
import scipy.stats as st
import statsmodels.datasets
import matplotlib.pyplot as plt
#matplotlib inline
data = statsmodels.datasets.heart.load_pandas().data
print(data)
data.tail()
data = data[data.censors == 1]
survival = data.survival
print(survival)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(sorted(survival)[::-1], 'o')
ax1.set_xlabel('Patient')
ax1.set_ylabel('Survival time (days)')

ax2.hist(survival, bins=15)
ax2.set_xlabel('Survival time (days)')
ax2.set_ylabel('Number of patients')
plt.show()

smean = survival.mean()
rate = 1. / smean
smax = survival.max()
days = np.linspace(0., smax, 1000)
# bin size: interval between two
# consecutive values in `days`
dt = smax / 999.

dist_exp = st.expon.pdf(days, scale=1. / rate)

nbins = 30
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
ax.hist(survival, nbins)
ax.plot(days, dist_exp * len(survival) * smax / nbins,
        '-r', lw=3)
ax.set_xlabel("Survival time (days)")
ax.set_ylabel("Number of patients")
plt.show()
dist = st.expon
args = dist.fit(survival)
print(args)

st.kstest(survival, dist.cdf, args)
print(st.kstest(survival, dist.cdf, args))
#the Birnbaum-Sanders distribution, which is typically used to model failure times.
dist = st.fatiguelife
args = dist.fit(survival)
st.kstest(survival, dist.cdf, args)
print(st.kstest(survival, dist.cdf, args))
dist_fl = dist.pdf(days, *args)
nbins = 30
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
ax.hist(survival, nbins)
ax.plot(days, dist_exp * len(survival) * smax / nbins,
        '-r', lw=3, label='exp')
ax.plot(days, dist_fl * len(survival) * smax / nbins,
        '--g', lw=3, label='BS')
ax.set_xlabel("Survival time (days)")
ax.set_ylabel("Number of patients")
ax.legend()
plt.show()




