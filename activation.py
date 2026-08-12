import numpy as np


def relu(x):
    """Apply the ReLU activation function."""
    return np.maximum(0, x)


def sigmoid(x):
    """Apply the sigmoid activation function."""
    return 1 / (1 + np.exp(-x))


outputs = np.array([-3.0, 2.0, -1.0, 5.0, 0.5])

relu_outputs = relu(outputs)
sigmoid_outputs = sigmoid(outputs)

print("Before activation:", outputs)
print("After ReLU:", relu_outputs)
print("After Sigmoid:", sigmoid_outputs)