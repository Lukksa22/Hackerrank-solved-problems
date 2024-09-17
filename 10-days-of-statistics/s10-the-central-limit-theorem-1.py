from math import *

n = 49
mn = 205
stdd = 15

mnp = n*mn
stddp = sqrt(n) * stdd

def nd(mn, stdd, x):
    return (pow(e, -((x-mn)**2)/2*stdd**2)/(stdd*sqrt(2*pi)))


def cdf(mn, std, x):
    return 0.5*(1+erf((x-mn)/(std*sqrt(2))))

x = 9800
answer = cdf(mnp, stddp, x)
print(f'{answer:.4f}')