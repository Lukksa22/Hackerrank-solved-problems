from math import *
mean = 20
standard_deviation = 2

less_than = 19.5
between = (20, 22)

def cdf(mean, standard_deviation, x):
    return 0.5*(1+erf((x-mean)/(standard_deviation*sqrt(2))))
    
answer1 = cdf(mean, standard_deviation, less_than)
answer2 = cdf(mean, standard_deviation, between[1]) -\
          cdf(mean, standard_deviation, between[0])
          
print(f'{answer1:.3f}')
print(f'{answer2:.3f}')