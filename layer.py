import numpy as np


# Get input from the user
x1 = float(input("Enter input 1: "))
x2 = float(input("Enter input 2: "))

inputs = np.array([x1, x2])


# Randomly initialize weights and biases
weights = np.random.randn(3, 2)
biases = np.random.randn(3)


# Weighted sum + bias
outputs = np.dot(weights, inputs) + biases


# ReLU activation
outputs = np.maximum(0, outputs)


print("\nWeights:")
print(weights)

print("\nBiases:")
print(biases)

print("\nOutputs:")
print(outputs)