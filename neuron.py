import numpy as np


inputs = np.array([2.0, 3.0])

weights = np.array([0.5, 0.8])

bias = 0.2


output = np.dot(inputs, weights) + bias

print("Outputt -->>", output)