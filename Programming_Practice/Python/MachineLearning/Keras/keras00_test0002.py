import numpy as np

a_test = np.array([1, 2, 3, 4, 5])

print(a_test.shape) # (5, ) ≒ (1, 5)

a_test = a_test.reshape(1, 5)
print(a_test.shape)

b_test = np.array([[1, 2, 3], [4, 5, 6]])

print(b_test.shape) # (2, 3)

c_test = np.array([[1, 2], [3, 4], [5, 6]])

print(c_test.shape) # (3, 2)

d_test = c_test.reshape(3, 1, 2, 1) 
# d_test = c_test.reshape(3, 2, 2, 1) # 같은 차원이어야 한다. (계수의 곱이 같아야 한다.)

print(d_test.shape) # (3, 1, 2, 1)

print(d_test)