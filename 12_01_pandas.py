import numpy as np
import pandas as pd

F = 'data/12_metro_compressor.csv'

# Pandas
# - 표 형태의 데이터를 잘 다루기 위해
# - Series: 하나의 열들
# - DataFrame: Series가 모여서 합쳐진 것, 표 구조 (df)

# 앞 단원 방식 -> 숫자 열만 골라야 함
# Pandas 방식 -> 글자 열까지 그대로, 열은 이름으로

df = pd.read_csv(F)
print("데이터 크기:", df.shape)         # 데이터 크기: (200, 7)
# print(df.head())
# print("열 이름:", df.columns.tolist())
# 열 이름: ['측정시각', '압축압력', '배출압력', '저장압력', '오일온도', '모터전류', '가동상태']

# print(df.dtypes)

# # 실습 1
# print("실습 1")
# data = pd.read_csv(F)
# print(df.shape)
# print(df.head())

state = df["가동상태"].values
print("가동상태 종류 개수:", np.unique(state, return_counts=True))
# 가동상태 종류 개수: (array(['가동', '정지'], dtype=object), array([ 96, 104]))

cur = df["모터전류"].values
print("모터전류 평균 %.2f / 가운데 값 %.2f " % (np.mean(cur), np.median(cur)))
# 모터전류 평균 2.06 / 가운데 값 0.04 

s = df["오일온도"]
print(s.head(3))
# 0    51.3
# 1    56.8
# 2    55.7
# Name: 오일온도, dtype: float64

# Pandas - 열 이름
new = pd.read_csv(F, usecols=["오일온도", "모터전류"])
print(new.shape)        # (200, 2)
# 행 수를 제한하는 설정
print(pd.read_csv(F, nrows=10).shape)       # (10, 7)
# read_csv 옵션
# - usecols, nrows, encoding, sep(구분자)


# 실습 2
print("실습 2")
mk = pd.read_csv(F, usecols=["측정시각", "오일온도", "모터전류"])
print(mk.shape)
print(pd.read_csv(F, nrows=20).shape)


# 실습 3
print("실습 3")

FI = 'data/12_metro_compressor_semicolon.csv'

sh = pd.read_csv(FI)
print(sh.shape)
# print(sh.head())

ke = pd.read_csv(FI, sep=";", encoding="utf-8")
print(ke.shape)

# 실습 4
print("실습 4")
mk = pd.read_csv(FI, sep=";", encoding="utf-8", usecols=["측정시각", "오일온도", "모터전류"], nrows=50)
print(mk.shape)

