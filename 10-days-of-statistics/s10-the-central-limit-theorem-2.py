from math import *

x = 250
n = 100
mn = 2.4
stdd = 2.0

mnp = n*mn
stddp = sqrt(n) * stdd

def cdf(mn, std, x):
    return 0.5*(1+erf((x-mn)/(std*sqrt(2))))

answer = cdf(mnp, stddp, x)
print(f'{answer:.4f}')