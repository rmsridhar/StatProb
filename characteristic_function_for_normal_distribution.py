import numpy as np
from scipy import stats, special

def chf_normal(t, loc=0, scale=1):
    '''characteristic function of normal distribution

 #   Parameters
    ----------
    t : array_like
        points at which characteristic function is evaluated
    loc : float (or array_like ?)
        mean of underlying normal distribution
    scale : float (or array_like ?)
        standard deviation, scale of normal distribution

    Returns
    -------
    chfval : ndarray
        characteristic function evaluated at x

    Notes
    -----
    Can be used for higher dimensional arguments if ``t``, ``mean`` and ``var``
    broadcast.

    '''
    t = np.asarray(t)
    return np.exp(1j * t * loc - 0.5 * t**2 * scale**2)


def chf_t(t, df, loc=0, scale=1):
    '''characteristic function of t distribution

    breaks down for large df and t close to zero
    '''
    t = np.asarray(t)
    vhalf = df / 2.
    term = np.sqrt(df) * np.abs(t*scale)
    cf = special.kv(vhalf, term) * np.power(term, vhalf)
    cf = cf / special.gamma(vhalf) / 2**(vhalf - 1)
    cf = cf * np.exp(1j * loc * t)
    if cf.shape == () and t == 0:
        #special case: kv(0) returns nan
        #for df>15 or so, we also get nans in the result in neighborhood of 0
        cf = np.ones((), cf.dtype)  #return same dtype as cf would
    else:
        cf[t == 0] = 1

    return cf

def chf_t_(t, df, loc=0, scale=1):
    #not much, but a bit better with log
    vhalf = df / 2.
    term = np.sqrt(df) * np.abs(t*scale)
    cf = np.log(special.kv(vhalf, term)) + vhalf * np.log(term)
    cf = cf - special.gammaln(vhalf) - (vhalf - 1) * np.log(2)
    cf = cf + 1j * loc * t
    if cf.shape == () and t == 0:
        #special case: kv(0) returns nan
        #for df>15 or so, we also get nans in the result in neighborhood of 0
        cf = np.zeros((), cf.dtype)  #return same dtype as cf would
    else:
        cf[t == 0] = 0
    return np.exp(cf)


def chfn(self, t, *args, **kwds):
    return chf_normal(t, *args, **kwds)

#monkeypatch scipy.stats
stats.distributions.norm_gen._chf = chfn

t = np.linspace(-1, 1, 11)
print (stats.norm._chf(t, loc=1, scale=2))
print (chf_t(t, 50, loc=1, scale=2))
print (chf_t_(t, 50, loc=1, scale=2))
