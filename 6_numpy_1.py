import numpy as np

# (3, ) 행렬
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print(A, B)
print(A + B)
print(A.shape, B.shape)
print(A.ndim, B.ndim)

# (2x3) 행렬
C = np.array([[1, 2, 3], [4, 5, 6]])
D = np.array([[-1, -2, -3], [-4, -5, -6]])

print(C, D)
print(C + D)
print(C.shape, D.shape)
print(C.ndim, D.ndim)

# reshape() => 형 변환
print(D.reshape(3, 2))
