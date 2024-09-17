import math
# Enter your code here. Read input from STDIN. Print output to STDOUT

l = 2.5
k = 5

x = (math.pow(l, k)*math.pow(math.e, -l))/math.factorial(k)
print(round(x, 3))
