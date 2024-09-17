from math import *

n = 100
mn = 500
stdd = 80
z = 1.96
p = 0.95

xA = mn - z*stdd/sqrt(n)
xB = mn + z*stdd/sqrt(n)

#p = B - A
print(f'{xA:.2f}')
print(f'{xB:.2f}')
