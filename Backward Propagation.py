import math

# User input
x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))

w1 = float(input("Enter w1: "))
w2 = float(input("Enter w2: "))

b = float(input("Enter bias: "))
target = float(input("Enter target output: "))

learning_rate = 0.1

# Forward propagation
net = (x1 * w1) + (x2 * w2) + b
output = 1 / (1 + math.exp(-net))

# Backward propagation
error = target - output
gradient = error * output * (1 - output)

# Update weights and bias
w1 = w1 + learning_rate * gradient * x1
w2 = w2 + learning_rate * gradient * x2
b = b + learning_rate * gradient

# Display results
print("\nOutput =", output)
print("Error =", error)
print("Updated w1 =", w1)
print("Updated w2 =", w2)
print("Updated bias =", b)
