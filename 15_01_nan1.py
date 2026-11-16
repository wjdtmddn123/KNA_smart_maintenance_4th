import pandas as pd

F_PROC = 'data/15_사출성형_공정.csv'
F_LOG = 'data/15_사출성형_로그.csv'

df = pd.read_csv(F_PROC)

# 결측 처리
# - 종류: NaN, None, NA, NaT
# ㄴ 표현을 달라도 isna()로 결측 여부 확인 가능

s = pd.Series([10, None, 20])
print(s.mean())     # 15.0 -> NaN 값이 있다고 해서 계산이 멈춘다 X (10 + 20) / 2
print(s + 1) # 11.0, NaN, 21.0 


# 실습 1
print("실습 1")
dfl = pd.read_csv(F_LOG)
print(dfl.shape)
print(dfl.isna().sum())
# 측정시각     0
# 사출기      1
# 배럴온도     2
# 사출압력     1
# 스크루속도    1
# 누적샷      0
# 불량여부     0

# print(dfl.isna().sum().sum())

print((dfl['사출압력'] == 0).sum())
print((dfl['스크루속도'] == -999).sum())
print((dfl['배럴온도'] == 999).sum())

# print(int(dfl["사출압력"].eq(0).sum()))           # 2
# print(int(dfl["스크루속도"].eq(-999).sum()))      # 2
# print(int(dfl["배럴온도"].eq(999).sum()))         # 1


# 실습 2
print("실습 2")
print(df.shape)     # (250, 22)
print(df.head(3).to_string(index=False))
print(df.info())
print(df['최대사출속도'].describe())


# 실습 3
print("실습 3")
print(dfl.isna().sum())
NA_RULES = {
    '배럴온도': [999],
    '스크루속도': [-999],
}
log_clean = pd.read_csv(F_LOG, na_values=NA_RULES)
print(log_clean.isna().sum())

NA_RULES['사출압력'] = [0]
log_clean = pd.read_csv(F_LOG, na_values=NA_RULES)
print(log_clean.isna().sum())


# 실습 3 정답
partial = pd.read_csv(F_LOG, na_values={
    '배럴온도': [999], '스크루속도': [-999]})
normalized = pd.read_csv(F_LOG, na_values={
    '배럴온도': [999], '스크루속도': [-999], '사출압력':[0]})
print(int(dfl.isna().sum().sum()),              # 5
      int(partial.isna().sum().sum()),          # 8
      int(normalized.isna().sum().sum()))       # 10


# 실습 4
print("실습 4")
count = df.isna().sum()
percen = (count / len(df) * 100).round(1)

summary = pd.DataFrame({'결측수': count, '결측률':percen})
summary = summary[summary['결측수'] > 0]
print(len(summary))
print(summary.sort_values('결측수', ascending=False))


# 실습 4 정답
count = df.isna().sum()
ratio_pct = count / len(df) * 100
summary = pd.DataFrame({'결측개수': count, '결측률_%': ratio_pct})
missing_summary = summary.loc[summary['결측개수'] > 0].copy()
print(missing_summary.round(1).to_string())
print(len(missing_summary))


# 실습 5
print("실습 5")
percen = (count / len(df) * 100)
print(percen.sort_values(ascending=False).head(3))

row_na = df.isna().sum(axis=1)
print(int((row_na == 0).sum()))
print(int((row_na > 0).sum()))
print(int((row_na >= 5).sum()))


# 실습 5 정답
print(
    ratio_pct.sort_values(
        ascending=False,
        kind="stable"       # 결측률이 같을 때 기존 순서를 유지하도록
    ).head(3)
)
row_missing = df.isna().sum(axis=1)
print(int((row_missing ==0).sum()),
      int((row_missing > 0).sum()))         # 76, 174
many_missing = df.loc[row_missing >= 5]     # 결측이 다섯 칸 이상 있는지
print(many_missing.shape)                   # (27, 22)


# 실습 6
print("실습 6")
count_2 = df[['최대사출속도', '감압시간']]
print(count_2.isna().sum())
print(count_2.isna().head(10))

a = df['최대사출속도'].isna()
b = df['감압시간'].isna()
both = a & b
print(both.sum(), both.sum() / len(df) * 100, "%")

print((a & ~b).sum() + (~a & b).sum())
print((~a & ~b).sum())

# 실습 6 정답
cols = ["최대사출속도", "감압시간"]

print(df[cols].isna().sum())
# 최대사출속도    109
# 감압시간      109
print(df[cols].isna().head(10))

missing_a = df["최대사출속도"].isna()
missing_b = df["감압시간"].isna()

both_missing = missing_a & missing_b

print(int(both_missing.sum()))                  # 109
print(round(both_missing.mean() * 100, 1))      # 43.6
