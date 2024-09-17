import math

answer = 0
p = 1/3
n = 5

def from_choose(n, x):
    return math.factorial(n) / (math.factorial(x)*math.factorial(n-x))

# binomial distribution
for x in range(1, n+1):
    answer += from_choose(n, x)* math.pow(p, x) * math.pow(1-p, n-x)

print(round(answer, 3))
