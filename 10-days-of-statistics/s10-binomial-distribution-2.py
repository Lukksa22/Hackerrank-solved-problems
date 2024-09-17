import math
percentaje = 12
size = 10

p_reject = percentaje/100

at_most_2 = 0
at_least_2 = 0

def from_choose(n, x):
    return math.factorial(n) / (math.factorial(x)*math.factorial(n-x))

for x in range(2+1):
    at_most_2 += from_choose(size, x)* math.pow(p_reject, x) * math.pow(1-p_reject, size-x)

print(round(at_most_2, 3))

for x in range(2, size+1):
    at_least_2 += from_choose(size, x)* math.pow(p_reject, x) * math.pow(1-p_reject, size-x)

print(round(at_least_2, 3))