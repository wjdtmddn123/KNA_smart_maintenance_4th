import pandas as pd

F = 'data/14_hydraulic.csv'
F_QC = 'data/14_hydraulic_qc.csv'

# 빈도와 그룹 집계
# - 값별로 세기와 그룹별로 집계하기

df = pd.read_csv(F)
qc = pd.read_csv(F_QC)
print(df.shape, qc.shape)       # (120, 8) (200, 11)


# 1. 빈도
# - value_counts
# - pd.cut

print(df['냉각기상태'].value_counts())
# 냉각기상태
# 고장    40
# 저하    40
# 정상    40
# Name: count, dtype: int64
print(df['밸브상태'].value_counts())
# 밸브상태
# 정상    61
# 지연    20
# 경미    20
# 심각    19
# Name: count, dtype: int64

# 개수 -> 비율 : normalize
counts = df["result"].value_counts()
ratios = df["result"].value_counts(normalize=True)
print(counts)                       # 정상 67 고장 53
print(ratios.round(3))
print((ratios * 100).round(1))      # 정상 55.8 고장 44.2


# 실습 1
print("실습 1")

print(df.shape)

print(df['밸브상태'].value_counts())
print(df["밸브상태"].value_counts(normalize=True).round(2))

print(df['운전부하'].value_counts())
print(df["운전부하"].value_counts(normalize=True).round(2))

for counts in [df['밸브상태'].value_counts(), df['운전부하'].value_counts()]:
    print("가장 많은 값:", counts[counts == counts.max()])
    print("가장 적은 값:", counts[counts == counts.min()])


# 실습 2
print("실습 2")
print(qc.shape)
print(qc['검사결과'].value_counts())
print(qc['검사결과'].value_counts(normalize=True).round(3))
print((qc['검사결과'].value_counts(normalize=True) * 100).round(3))
print("불합격 비율:", round((qc['검사결과'].value_counts(normalize=True)).loc["불합격"]* 100,1),"%")


# pd.cut
band = pd.cut(df["온도"], bins=[0, 40, 50, 200], labels=["낮음", "보통", "높음"], right=True)
print(band.value_counts(sort=False))
# 온도
# 낮음    41
# 보통    40
# 높음    39
# Name: count, dtype: int64


# 실습 3
print("실습 3")
print(df['진동'].min(), df['진동'].max())

data = pd.cut(df['진동'], bins=[0, 0.6, 0.7, 10], labels=['약함','보통', '강함'], right=True)
print(data.value_counts())

print(data.isna().sum())
print("검산:",data.value_counts().sum(), "구간 미지정:",data.isna().sum())

data = pd.cut(df['진동'], bins=[0, 0.62, 0.7, 10], labels=['약함','보통', '강함'], right=True)
print(data.value_counts())


# 그룹 집계
# - 분할 -> 적용 -> 결합 구조
# - groupby
print("----------------------------")
means = df.groupby("냉각기상태")["온도"].mean()
print(means.round(2))
# 냉각기상태
# 고장    54.67
# 저하    45.46
# 정상    35.89
# Name: 온도, dtype: float64

print(df.groupby("냉각기상태")["온도"].max())
# 냉각기상태
# 고장    57.8
# 저하    51.2
# 정상    36.4
# Name: 온도, dtype: float64


# 실습 4
print("실습 4")
print(df['냉각기상태'].value_counts())

mean_t = df.groupby('냉각기상태')['온도'].mean().round(2)
print(mean_t)

# max_t = df.groupby('냉각기상태')['온도'].max()
# print(max_t)

print("차이:", mean_t.max() - mean_t.min())

# # 실습 4 정답
# counts = df.groupby("냉각기상태").size()
# means = df.groupby("냉각기상태")["온도"].mean()
# maxima = df.groupby("냉각기상태")["온도"].max()
# print(counts)
# print(means.round(2))
# print(maxima)
# print("평균차이:", round(means.max()-means.min(), 2))


# # 여러 키 그룹 코드
# keys = ["냉각기상태", "운전부하"]
# print(df.groupby(keys)["온도"].mean().round(2))
# # 냉각기상태  운전부하
# # 고장     고부하     55.51
# #        저부하     54.05
# # 저하     고부하     44.07
# #        저부하     45.58
# # 정상     고부하     35.89

# crosstab
print(pd.crosstab(df["냉각기상태"], df["운전부하"]))
# 운전부하   고부하  저부하
# 냉각기상태          
# 고장      17   23
# 저하       3   37
# 정상      40    0


# 실습 5
print("실습 5")
total = df['밸브상태'].value_counts()
print(total)

fail= df[df['result'] == '고장']
fail_t = fail['밸브상태'].value_counts()
print(fail_t)

ratio = (fail_t / total)
print(ratio.round(3))


# 실습 5 정답
# total = df['밸브상태'].value_counts()
# print(total)

# broken = df[df['result'] == '고장']
# broken_counts = broken.groupby("밸브상태").size()
# print(broken_counts)

# # 고장 라벨이 0건인 상태도 빠지지 않도록 이름표를 맞춘다
# broken_counts = broken_counts.reindex(total.index, fill_value = 0)
# ratios = broken_counts / total
# print(ratios.sort_values(ascending=False).round(3))
