import numpy as np


def relu(x):
    """Apply the ReLU activation function."""
    return np.maximum(0, x)


outputs = np.array([-3.0, 2.0, -1.0, 5.0, 0.5])

relu_outputs = relu(outputs)

print("Before ReLU:", outputs)
print("After ReLU:", relu_outputs)