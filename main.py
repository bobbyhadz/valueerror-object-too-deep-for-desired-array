# ValueError: object too deep for desired array

# Removing the extra dimension to solve the error

import numpy as np

x = np.array([1, 2, 3])

y = np.array([[0.5, 1, 0.3], [0.2, 0.7, 0.8]])

print(y[:, 0])  # 👉️ [0.5 0.2]

arr = np.convolve(x, y[:, 0], 'same')

print(arr)  # 👉️ [0.5 1.2 1.9]