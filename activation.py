import numpy as np


outputs = np.array([-3.0, 2.0, -1.0, 5.0, 0.5])


relu_outputs = np.maximum(0, outputs)


print("Before ReLU:", outputs)
print("After ReLU:", relu_outputs)