import math

lx = 0.88
ly = 1.55

def E_lambda(l):
    return l + l*l
    
k = 1

x = E_lambda(lx)
y = E_lambda(ly)

cost_A = 160 + 40*x
cost_B = 128 + 40*y

# daily cost of operating A
print(round(cost_A, 3))
# daily cost of operating B
print(round(cost_B, 3))
