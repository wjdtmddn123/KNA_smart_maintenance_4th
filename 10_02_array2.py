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


# 배열 연산
a = np.array([1,2,3])
b = np.array([10,20,30])
print(a + b)        # [11, 22, 33]
# 같은 위치 값끼리 계산 (반복문 필요x)
# 사칙연산 모두 같은 방식으로 계산

# 스칼라 연산
# - 숫자 하나를 배열 전체에 적용, 크기를 맞출 필요가 없다
# - 연산 숫자는 수학과 같아 곱하기 먼저 
print(a * 10 + 3)

# 브로드캐스팅
table = np.array([[72, 2.4], [95, 6.8]])
print(table.shape)  # (2,2)
base = np.array([70, 2.0])      # (,2)
print(table - base)
#[[ 2.   0.4]
# [25.   4.8]]
# 한 줄짜리 기준값이 모든 행에 퍼져서 계산됨
# 조건) 작은 쪽 크기가 1이거나 같아양 함

# 실습 3
print("실습 3")
rpm = np.array([4603, 4603, 58, 4603, 4603, 4603, 1216, 4987, 1217, 3632])
norm = (rpm - rpm.min()) / (rpm.max()-rpm.min())
print(np.round(norm, 2))


# 비교 연산과 불리언 배열
vals = np.array([70, 95, 71, 88, 73])
print(vals > 75)        # [False  True False  True False]

# 불리언 인덱싱
# - 조건이 참/거짓인 배열을 만듦 -> 그 배열을 대괄호에 넣으면 참인 값만 남는다
print(vals[vals > 75])      # [95 88]

# np.where(조건, 참일 때 값, 거짓일 때 값)
print(np.where(vals > 85, 1, 0))        # [0 1 0 1 0]

# 다중 조건
print(vals[(vals > 70) & (vals <90)])       # [71 88 73]

# 실습 4
print("실습 4")
data = np.array([
    [1217, 17.85],
    [4603, 18.97],
    [4603, 15.71],
    [4603, 19.04],
    [4603, 18.48],
    [4603, 18.48],
    [1241, 36.33],
    [4603, 15.03],
    [4603, 19.17],
    [3143, 46.43],
])
rpm = data[:,0]
current = data[:,1]

low = np.where(rpm <2000, 1, 0)
bad = np.where((rpm < 2000) | (current > 25), 1, 0)

print(low)
print(bad)

print("횟수:", np.sum(low), "개")
print("횟수:", np.sum(bad), "개")

print("비율:", np.mean(low) * 100, "%")
print("비율:", np.mean(bad) * 100, "%")

print("실습 4 정답")
rpm = np.array([1217,4603,4603,4603,4603,4603,1241,4603,4603,3143])
current = np.array([17.85,18.97,15.71,19.04,18.48,18.48,36.33,15.03,19.17,46.43])

low_rpm = rpm<2000
# 회전수 2000미만
print(rpm[low_rpm])
# 회전수 2000미만 또는 전류 25초과
print(rpm[low_rpm],current[current>25])

# 개수
print(np.sum(low_rpm))
print(np.sum((rpm < 2000) | (current > 25)))

#비율
print(np.mean(low_rpm) * 100,"%") 
# - low_rpm : Trume False 배열 -> True:1, False: 0
print(np.mean((rpm < 2000) | (current > 25))* 100, "%")


# # 실습 5
print("실습 5")
torque = np.array([2, 2, 21, 3, 2, 147, 2, 3, 1, 2])
flag = np.where(torque > 10, 1, 0)
print(flag)
count = flag.sum()
print(count, "개")
ratio = flag.mean()
print("비율:", ratio)

print("실습 5 정답")
torque = np.array([2, 2, 21, 3, 2, 147, 2, 3, 1, 2])
high = torque > 10
print(high.sum())
print(round(high.mean(),2))     # 0.2


# 통계
# - 정상을 알아야 이상을 알 수 있다
# ex) 평균을 알아야 평균과 크게 차이가 나는 값이 나왔을 때 이상치 판단 가능
# - 평균, 최대/최소, 표준편차, 분산
# - NumPy 에서 함수 하나로 계산

s = np.array([70, 72, 71, 95, 73])
print("합계:", s.sum())
print("평균:", s.mean())                
print("중앙값:", np.median(s))
print("최대:", s.max())
print("최소:", s.min())

# 분산
stable = np.array([70, 71, 70, 72, 71])
unstable = np.array([60, 85, 65, 95, 70])
print(round(stable.var(), 1))               # 0.6
print(round(unstable.var(), 1))             # 170.0

# 표준편차
print(round(stable.std(), 2))           # 0.75
print(round(unstable.std(), 2))         # 13.04

# axis 개념 (행/열 방향)
mat = np.array([[70, 2.1], [72, 2.3]])
print(mat.mean(axis=0))     # 열별 평균 (센서별)
print(mat.mean(axis=1))     # 행별 평균 (시점별) -> 지금은 큰 의미X
print(mat.mean())           # 전체 평균


# 실습 6
print("실습 6")
table =np.array([
    [1217, 2],
    [4603, 2],
    [4603, 21],
    [4603, 3],
    [4603, 2],
    [4603, 147],
    [1241, 2],
    [4603, 3],
    [4603, 1],
    [3143, 2],
])
print(np.round(table.mean(axis=0), 1))
print(np.round(table.std(axis=0), 1))

print("===============================")

# 파일에서 배열로 불러오기(np.loadtxt)
rpm = np.loadtxt('10_mct_tool.csv',
                  delimiter=',',            # 값을 나누는 기호
                  skiprows=1,               # 첫 줄(제목)은 건너뜀      
                  usecols=4)                # 5번째 열 = 회전수
print(rpm)
print(rpm.shape, rpm.dtype)                 # (40,) float64

rpm_tq = np.loadtxt('10_mct_tool.csv',
                  delimiter=',',            # 값을 나누는 기호
                  skiprows=1,               # 첫 줄(제목)은 건너뜀      
                  usecols=(4,5))
print(rpm_tq.shape)                         # (40, 2)

# 실습 7
print("실습 7")
rpm = np.loadtxt('10_mct_tool.csv',
                 delimiter=',',
                 skiprows=1,
                 usecols=4)
print("회전수 평균:", round(rpm.mean(),1))
print("표준편차:", round(rpm.std(),1))
print("최소:", rpm.min())
print("최대:", rpm.max())

# 실습 8
print("실습 8")
torque = np.loadtxt('10_mct_tool.csv',
                    delimiter=',',
                    skiprows=1,
                    usecols=5)
tq = torque > 10
print(torque[tq])
print("개수:", torque[tq].size, "개")
print("평균:", round(torque[tq].mean(), 1))
print("전체 평균:", torque.mean())

# 실습 9
print("실습 9")
rpm_torque = np.loadtxt('10_mct_tool.csv',
                        delimiter=',',
                        skiprows=1,
                        usecols=(4,5))
print(rpm_torque.shape, rpm_torque.dtype)

rpm =rpm_torque[:,0]
print(rpm)

low = rpm[rpm < 2000]
print("이상 시점:", len(low), "개")
print("이상 평균:", round(low.mean(),1))
print("전체 평균:", round(rpm.mean(), 1))