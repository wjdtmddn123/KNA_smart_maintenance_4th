import pandas as pd

F_PROC = 'data/15_사출성형_공정.csv'
F_LOG = 'data/15_사출성형_로그.csv'

df = pd.read_csv(F_PROC)
log_raw = pd.read_csv(F_LOG)


# dropna : 행삭제, 열 삭제
# - axis: 제거할 축을 선택, axis = 1 -> 열 전체가 빠지게 됨
rows_removed = df.dropna()
cols_removed = df.dropna(axis=1)
print(rows_removed.shape)       # (76, 22)       
print(cols_removed.shape)       # (250, 10)
print(df.shape)                 # (250, 22)

# - how: 하나라도 비면, 전부 비면
# - any, all
print(df.dropna(how='any').shape)   # (76, 22)
print(df.dropna(how='all').shape)   # (250, 22)

# - thresh : 유효값 최소 개수
print(df.dropna(thresh=20).shape)   # (162, 22)

# - subset : 중요한 열만 검사
#  ㄴ 다른 열의 결측이 남아 있어도 지정한 조건을 충족하면 유지한다
print(df.dropna(subset=['배럴온도1']).shape)    # (250, 22)

# 실습 1
print("실습 1")
print(df.shape)
print(df.dropna().shape)
print(df.dropna(axis=1).shape)

# 실습 2
print("실습 2")
print(df.dropna(how='all').shape)
print(df.dropna(thresh=20).shape)
print(int(df['불량여부'].isna().sum()))
print(df.dropna(subset=['불량여부']).shape)

# 실습 3
print("실습 3")
META = ['측정시각', '사출기', '불량여부']
feature_cols = [c for c in df.columns if c not in META]
# feature_cols = []
# for c in df.columns:
#     if c not in META:
#         feature_cols.append(c)

feature_rate = df[feature_cols].isna().mean()
drop_cols = feature_rate[feature_rate >= 0.4].index.tolist()
print(drop_cols)    # ['최대사출속도', '감압시간']
base = df.drop(columns=drop_cols).copy()
print(base.shape)