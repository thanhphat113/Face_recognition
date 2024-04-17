import numpy as np

# Mảng ban đầu
arr = np.array([2, 5, 7, 10, 1])

# Chuyển đổi thành mảng 0 và 1
binary_arr = np.where(arr > 5, 1, 0)

print(binary_arr)
