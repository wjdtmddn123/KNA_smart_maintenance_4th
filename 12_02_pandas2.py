import pandas as pd
import numpy as np

F = 'data/12_metro_compressor.csv'
FD = 'data/12_metro_digital.csv'

df = pd.read_csv(F)

# 데이터 미리보기 및 구조 파악

# # -1) 앞 부분 미리보기
# # - df.head() > 위에서 5줄, 숫자 지정 가능
# print(df.head())

# # 2) 뒷 부분 미리보기
# # - df.tail() > 밑에서 5줄, 숫자 지정 가능
# print(df.tail())


# # 실습1
# print("실습 1")
# print(df.head())
# print(df.tail())
# print(df.head(3))
# print(df.tail(10))


# # 3) 행/열 크기
# # - df.shape
# print(df.shape)     # (행, 열)

# # 4) 열 이름 목록
# # - df.columns      >   인덱스 형태로 출력
# # - df.columns.tolist() > 목록으로 보기 좋게
# print(df.columns.tolist())
# # ㄴ 여기서 나오는 값으로 특정 열의 데이터 값 추출

# # 5) 행 번호표
# # - df.index
# print(df.index)         # RangeIndex(start=0, stop=200, step=1)
# # ㄴ 0부터 시작, 199까지 1씩

# # 6) 열별 자료형
# # - df.types
# print(df.dtypes)
# print("-------------------------------")
# print(pd.read_csv(FD).dtypes)
# # 측정시각       str
# # 압축기      int64
# # 타워       int64
# # 저압스위치    int64
# # dtype: object
# df2 = pd.read_csv(FD, dtype={"압축기": str})

# # 실습 2
# print("실습 2")
# print(pd.read_csv(FD).shape)
# print(pd.read_csv(FD).columns.tolist())
# print(pd.read_csv(FD).dtypes)
# print(pd.read_csv(FD).head())

# 7) 전체 구조
# - df.info()
# print(df.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 200 entries, 0 to 199         > 200행
# Data columns (total 7 columns):           > 7열
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   측정시각    200 non-null    str
#  1   압축압력    200 non-null    float64
#  2   배출압력    200 non-null    float64
#  3   저장압력    200 non-null    float64
#  4   오일온도    199 non-null    float64
#  5   모터전류    200 non-null    float64
#  6   가동상태    200 non-null    str
# dtypes: float64(5), str(2)
# memory usage: 11.1 KB
# None

# 기초 통계 요약
# - 숫자 열들의 평균/최대/최소 등을 한번에 자동 계산. 글자 열은 자동으로 빠짐

# print(df.describe().round(2))
#          압축압력    배출압력    저장압력    오일온도    모터전류
# count  200.00  200.00  200.00  199.00  200.00
# mean     9.17   -0.02    9.17   63.18    2.06
# std      0.58    0.05    0.58    6.25    2.20
# min      8.13   -0.03    8.13   50.10    0.03
# 25%      8.70   -0.02    8.70   58.10    0.04
# 50%      9.18   -0.02    9.18   62.90    0.04
# 75%      9.66   -0.02    9.66   68.10    3.81
# max     10.22    0.60   10.22   75.00    6.19

# 특정 조건에서의 통계 필요 시
# state = df["가동상태"].values
# cur = df["모터전류"].values
# print(round(float(np.mean(cur[state == "가동"])),2))


# # 실습 3
# print("실습 3")
# print(df.info())
# # 오일 온도 -> 199 -> 결측 1개

# # 실습 4
# print("실습 4")
# print(df.describe().round(2))
# # 두 열을 배열로 꺼내 상태별로 나눠 확인
# state = df["가동상태"].values
# cur = df["모터전류"].values

# print(round(float(np.mean(cur[state == '가동'])), 2))
# print(round(float(np.mean(cur[state == '정지'])), 2))


# 실습 6
print("실습 6")
FS = "data/12_metro_small.csv"
ds = pd.read_csv(FS)
print(ds.head(3))
print('크기:', ds.shape)
print(ds.info())

stats = df.describe()
miss = int(df["오일온도"].isna().sum())
print('오일온도 결측:', miss, '건')

mean_current = round(float(stats["모터전류"]["mean"]),2)
median_current = round(float(stats["모터전류"]["50%"]),2)
print("모터전류 평균/중앙값:", mean_current, median_current)
