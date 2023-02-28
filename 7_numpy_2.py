# numpy dot product
# 행렬 곱 : 다른 사칙연산은 행렬의 원소 개수가 같아야 하지만
# 1. 행렬 곱은 다양한 크기의 행렬 연속으로 만들고
# 2. 행렬 곱을 연속적으로 계산하며 결과값을 만듦 => 머신러닝, 이미지 프로세싱에서 자주 활용
# 예) (64 x 64) X (64 x 256) x (256 x 512) x (512 x 64) x (64 x 10) = (64 x 10)

# 행렬 A의 열벡터, 행렬 B의 행벡터가 같아야 실행할 수 있음
# 같지 않다면 reshape 또는 전치행렬(transpose) 등을 사용하여 형 변환 후 곱을 실행

# A.shape = (2,3), B.shape = (3,2)
# A x B = (2 x 3) x (3 x 2) = (2 x 2)

import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[-1, -2], [-3, -4], [-5, -6]])
C = np.dot(A, B)

print("A.shape == ", A.shape, "B.shape", B.shape)
print("C.shape", C.shape)
print(C)


# numpy broadcast
# numpy에서는 크기가 다른 두 행렬 간 사칙연산이 가능함
# 차원이 작은 쪽이 큰 쪽의 행 단위로 크기를 반복적으로 맞추어 계산
# 행렬 곱 연산에는 적용되지 않음!

a = np.array([[1, 2], [3, 4]])
b = 5
print(a + b)
b = np.array([4, 5])
print(a + b)


# numpy transpose
# 원본 행렬의 열은 행으로, 행은 열로 바꿈

A = np.array([[1, 2], [3, 4], [5, 6]])  # (3x2) 행렬
B = A.T  # (2x3) 행렬

print("A.shape == ", A.shape, "B.shape", B.shape)
print(A)
print(B)

C = np.array([1, 2, 3, 4, 5])   # C는 vector. matrix 아님
D = C.T                         # C는 vector이므로 transpose 안됨

E = C.reshape(1, 5)
F = E.T

print("C.shape == ", C.shape, "D.shape", D.shape)
print("E.shape == ", E.shape, "F.shape", F.shape)
print(F)


# numpy 행렬 indexing / slicing

A = np.array([10, 20, 30, 40, 50, 60]).reshape(3, 2)

print("A.shape == ", A.shape)
print(A)

print("A[0,0] == ", A[0, 0], ", A[0][0] == ", A[0][0])
print("A[2,1] == ", A[2, 1], ", A[2][1] == ", A[2][1])

print("A[0:-1, 1:2] == ", A[0:-1, 1:2])

print("A[ : , 0] == ", A[:, 0])
print("A[ : , : ] == ", A[:, :])


# numpy 행렬 iterator

A = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])

print(A, '\n')
print("A.shape == ", A.shape, '\n')

# 행렬 A의 iterator 생성

it = np.nditer(A, flags=['multi_index'], op_flags=['readwrite'])

while not it.finished:
    idx = it.multi_index
    print("index => ", idx, " , value => ", A[idx])
    it.iternext()
