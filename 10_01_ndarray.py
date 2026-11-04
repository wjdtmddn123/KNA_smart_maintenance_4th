import numpy as np

# 리스트 vs 배열
# 1) 리스트
# - 서로 다른 자료형도 같이 존재 가능
# - 계산이 느리고 반복물을 돌아야 한다
list = [70, 72, 71]
print(list * 2)                 # [70, 72, 71, 70, 72, 71] 
print([v * 2 for v in list])    # [140, 144, 142]

# 2) 배열
# - 같은 자료형만 존재 가능
# - 계산이 빠르다

temp = np.array([70, 72, 71])
print(temp)             # [70 72 71]

print(temp + 2)         # [72 74 73] -> 반복문 없는 묶음 계산

# 튜플로 배열 만들기
print(np.array((1, 2, 3)))      # [1 2 3]

# 실습 1
print("실습 1")
temp = np.array([92, 82, 71, 86, 86, 74])
print("측정 온도:", temp)
print("화씨:", temp * 1.8 + 32)

# 배열 생성
# np.arange(시작, 끝, 간격) : 연속 정수
# - 끝값은 포함되지 않음
print(np.arange(5))             # [0 1 2 3 4]
print(np.arange(0, 10, 2))      # [0 2 4 6 8]

# np.linspace(시작, 끝, 개수) : 균등 분할
# - 끝값 포함
print(np.linspace(0, 1, 5))             # [0.   0.25 0.5  0.75 1.  ]
print(np.linspace(0, 10, 5))            # [ 0.   2.5  5.   7.5 10. ]


# 실습 2
print("실습 2")
print(np.linspace(0, 70, 8))

# 실습 3
print("실습 3")
print(np.arange(0, 40, 5))

# 배열 속성
# - ndim, shape, size, dtype
# - 속성은 괄호X

a = np.array([1,2,3])
b = np.array([[1,2,3],[4,5,6]])

print("dim:", a.ndim, b.ndim)           # dim: 1 2
print("shape:", a.shape, b.shape)       # shape: (3,) (2, 3)
print("size:", a.size, b.size)          #size: 3 6

# 실습 4
print("실습 4")
table = np.array([[81, 5.2], [85, 8.3],[87, 10.7], [90, 13.1]])
print("차원:", table.ndim)
print("형태:", table.shape)
print("개수:", table.size)


# 실습 5
print("실습 5")
value = np.array([15.23, 13.25, 18.69, 17.48])
print(value.dtype)
print(value.astype(int))


# reshape()로 형태 바꾸기
# - -1 사용 시 자동 계산 (행 또는 열에 한번만 사용)
c = np.arange(12)
print(c.reshape(3, 4))
# [[0 1 2 3]
# [4 5 6 7]
# [8 9 10 11]]

# flatten() -> 1차원 만듦
b3 = np.array([[1, 2, 3], [4, 5, 6]])
print(b3.flatten())         # [1 2 3 4 5 6]

# 실습 6
print("실습 6")
cycle_time = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(cycle_time.reshape(3,4))

# 실습 7
print("실습 7")
point = np.array([40, 5, 21, 42, 6, 25, 52, 9, 31, 58, 7, 42])
points = point.reshape(4,3)
print(points)
print(points.flatten())
