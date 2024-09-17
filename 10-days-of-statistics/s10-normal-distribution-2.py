from math import *
mn = 70
std = 10

def cdf(mn, std, x):
    return 0.5*(1+erf((x-mn)/(std*sqrt(2))))

# X > 80
answer1 = 1 - cdf(mn, std, 80)

# 60 <= X <= 100
answer2 = 1 - cdf(mn, std, 60)

# X < 60
answer3 = cdf(mn, std, 60)
          
print(f'{answer1*100:.2f}')
print(f'{answer2*100:.2f}')
print(f'{answer3*100:.2f}')