import math

ratio_boy = 1.09
ratio_girl = 1

p_boy = ratio_boy / (ratio_boy + ratio_girl)
p_girl = ratio_girl / (ratio_boy + ratio_girl)

# given A as my objective (on 6 children have at least 3 boys)
# we should use binomial distribution formula
# b(x, n, p) having x>=3 (as boys), n as children and p as boy probability


def from_choose(n, x):
    return math.factorial(n) / (math.factorial(x)*math.factorial(n-x))

answer = 0
children = 6
for x in range(3, children+1):
    answer += from_choose(children, x)* math.pow(p_boy, x) * math.pow(p_girl, children-x)

print(round(answer, 3))