import pandas as pd

F = 'data/14_hydraulic.csv'
F_QC = 'data/14_hydraulic_qc.csv'

# 그룹 통계와 상관관계
# - 그룹 통계 -> 원본 행과 그룹 기준 비교 -> 두 기준 표 -> 상관관계

df = pd.read_csv(F)
qc = pd.read_csv(F_QC)

print(round(df["온도"].mean(), 2))
print(round(df["온도"].std(), 2))

print(df.groupby("냉각기상태")["온도"].mean().round(1))
# 냉각기상태
# 고장    54.7
# 저하    45.5
# 정상    35.9
print(df.groupby("냉각기상태")["온도"].std().round(1))
# 냉각기상태
# 고장    3.8
# 저하    1.5
# 정상    0.4

# 분산 / 표준편차
v = df.groupby("냉각기상태")["온도"].var()
std = df.groupby("냉각기상태")["온도"].std()
print(v.round(2))
# 냉각기상태
# 고장    14.13
# 저하     2.15
# 정상     0.13
print(std.round(2))
# 냉각기상태
# 고장    3.76
# 저하    1.47
# 정상    0.36
print((std ** 2).round(2))
# 냉각기상태
# 고장    14.13
# 저하     2.15
# 정상     0.13


# agg - 여러 통계 한번에 표로 모으기
# ㄴ 리스트: 같은 대상에 여러 통계
# ㄴ 딕셔너리: 열별 통계
# ㄴ named aggregation: 결과 열의 이름까지 지정

print(df.groupby("냉각기상태")["온도"].agg(["mean", "std", "max"]).round(2))
print(df.groupby("냉각기상태")[["온도", "진동"]].agg(["mean", "std", "max"]).round(2))

# 이름 붙이기
summary = df.groupby("냉각기상태").agg(
    평균온도=("온도", "mean"),
    평균진동=("진동", "mean")
)
print(summary.round(2))

# 열별로 다른 통계 목록 지정
summary2 = df.groupby("냉각기상태").agg({
    "온도": ["mean", "std"],
    "진동": ["mean", "max"]
})
print(summary.round(2))


# 실습 1
print("실습 1")
print(qc["검사결과"].value_counts())

summary = qc.groupby("검사결과")[["온도", "냉각효율"]].agg(["mean", "std", "max"]).round(2)
print(summary)

summary2 = qc.groupby("검사결과").agg(
    평균온도=("온도", "mean"),
    평균냉각효율=("냉각효율", "mean"),
    측정수=("온도", "count")
).round(2)
print(summary2)


# transform - 그룹 통계를 원래 행에 붙이기
# - 원래 행 인덱스와 모양을 유지한다

# 같은 그룹의 평균 붙이기

print(df.groupby("냉각기상태")["온도"].mean().shape)        # (3,)
print(df.groupby("냉각기상태")["온도"].transform("mean").shape)    # (120,)

marked = df.copy()
marked["그룹평균"] = marked.groupby("냉각기상태")["온도"].transform("mean")
marked["편차"] = marked["온도"] - marked["그룹평균"]
print(marked[["냉각기상태", "온도", "그룹평균", "편차"]].head(3).round(2))
#   냉각기상태    온도   그룹평균     편차
# 0    고장  35.6  54.67 -19.07
# 1    고장  47.5  54.67  -7.17
# 2    고장  50.7  54.67  -3.97

# pivot_table - 두 기준 표를 한 번에
# - margins=True -> 전체 집계 추가
# - 값이 없는 조합의 평균을 0으로 메우지 않도록

temp_table = pd.pivot_table(df, index="밸브상태", columns="운전부하", values="온도", 
                            aggfunc="mean", margins=True, margins_name="전체")
# - index: 결과표의 행을 나누는 기준
# - columns: 결과표의 열을 나누는 기준
# - values: 각 칸에서 계산할 측정값
# - aggfunc: 그 측정값으로 요약
# - margins=True: 전체 집계 행.열 추가
# - margins_name: 추가 집계 이름 표시
print(temp_table.round(2))
# 운전부하    고부하    저부하     전체
# 밸브상태                     
# 경미    42.20  47.52  44.86
# 심각    45.25  47.09  46.02
# 정상    39.34  49.40  45.11
# 지연    43.75  49.79  45.86
# 전체    41.85  48.82  45.34


# 실습 2
print("실습 2")
marked = df.copy()
marked["그룹평균"] = marked.groupby("냉각기상태")["온도"].transform("mean")

marked["편차"] = marked["온도"] - marked["그룹평균"]
cols= ["냉각기상태", "온도", "그룹평균", "편차"]
print(marked[cols].head(3).round(2))

marked["거리"] = marked["편차"].abs()
furthest = marked.sort_values("거리", ascending=False).head(1)
print(furthest[cols].round(2))
#   냉각기상태    온도   그룹평균     편차
# 0    고장  35.6  54.67 -19.07

print(marked.groupby("냉각기상태")["편차"].sum().round(10))

pivot = pd.pivot_table(marked, index="밸브상태", columns="운전부하", values="온도",
                       aggfunc="mean", margins="True", margins_name="전체")
print(pivot.round(2))
print(pivot.shape)


# corr - 두 지표의 상관관계
print(round(df["온도"].corr(df["진동"]), 3))        # 0.931
print(round(df["온도"].corr(df["냉각효율"]), 3))    # -0.951
print(round(df["온도"].corr(df["압력"]), 3))        # 0.284


# 실습 3
print("실습 3")
print(round(df["온도"].corr(df["진동"]), 3))        
print(round(df["온도"].corr(df["냉각효율"]), 3))    
print(round(df["온도"].corr(df["압력"]), 3))  

cols = ["온도", "진동", "냉각효율", "압력"]
corr = df[cols].corr().round(3)
print(corr)


# 실습 4
print("실습 4")
sensor_cols = qc.select_dtypes(include="number").columns.tolist()
corr_matrix=qc[sensor_cols].corr()
rows=[]

for i in range(len(sensor_cols)):
    for j in range(i+1, len(sensor_cols)):
        a = sensor_cols[i]
        b = sensor_cols[j]
        rows.append({"지표1":a, "지표2":b, 
                     "상관계수":corr_matrix.loc[a,b]})
pair_table = pd.DataFrame(rows)
pair_table["절댓값"] = pair_table["상관계수"].abs()
print(corr_matrix.shape, len(pair_table))
print(pair_table.head(3).round(3))

print(len(pair_table))

print((pair_table["절댓값"] >= 0.4).sum())
print((pair_table["절댓값"] >= 0.95).sum())

top = pair_table[pair_table["절댓값"] >= 0.95].sort_values("절댓값", ascending=False).head(5)
print(top.round(4))


# 실습 5
