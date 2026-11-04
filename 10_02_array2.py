import numpy as np

# 인덱싱, 슬라이싱
a = np.array([0,1,2,3,4])
print(a[0], a[-1])               # 0 4
print(a[1:4])                   # [1 2 3]
print(a[::2])                   # [0 2 4]

# 실습 1
print("실습 1")
rpm = np.array([4603, 4603, 4967, 4603, 4603, 4603, 4603, 4987, 4603, 4603])
print(rpm[0], rpm[-1])
print(rpm[1:4])
print(rpm[::2])

# 실습 2
print("실습 2")
rpm_tor = np.array([[4603,2], 
                   [4603,2],
                   [4967,21],
                   [4603,2]])
print(rpm_tor[2])
print(rpm_tor[:,0])
print(rpm_tor[:,1])
