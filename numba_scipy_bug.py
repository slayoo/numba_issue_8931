import scipy.integrate
import numba
import numpy as np
import warnings

@numba.njit("int32(int32)")
def jitted_fun(x):
    return 1

def f(_, y):
  return np.zeros_like(y)

y0 = np.ones(2)

with warnings.catch_warnings(record=True):
    warnings.simplefilter("error")
    for _ in range(1000):
        scipy.integrate.solve_ivp(fun=f, t_span=(0, 1), y0=y0, method="BDF")
