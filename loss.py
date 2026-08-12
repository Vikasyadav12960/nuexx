import numpy as np


prediction = np.array([3.3, 1.8, 3.0])

target = np.array([4.0, 2.0, 3.5])


error = prediction - target

squared_error = error ** 2

loss = np.mean(squared_error)


print("Prediction:", prediction)
print("Target:", target)
print("Loss:", loss)