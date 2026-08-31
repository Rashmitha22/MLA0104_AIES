import math

# User inputs
x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))

# Weights
w1 = float(input("Enter w1: "))
w2 = float(input("Enter w2: "))

# Bias
b = float(input("Enter bias: "))

# Calculate weighted sum
net = (x1 * w1) + (x2 * w2) + b

# Sigmoid activation function
output = 1 / (1 + math.exp(-net))

print("Weighted Sum =", net)
print("Output =", output)
