import pandas as pd

F_die = 'data/16_diecasting.csv'

df = pd.read_csv(F_die)

# 실습 1
print("실습 1")
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())

# 실습 2
print("실습 2")
print(int(df['실린더압력'].min()))
print(int(df['실린더압력'].max()))
print(int(df['실린더압력'].max() - df['실린더압력'].min()))

# 실습 3
print("실습 3")
sorted = df.sort_values("사이클타임", ascending=False)
print(sorted[['사이클타임']].head(5))
print(sorted['사이클타임'].describe().round(2))

# 실습 4
print("실습 4")
ct_mean = df['사이클타임'].mean()
ct_median = df['사이클타임'].median()
print("평균:",round(ct_mean, 2), "중앙값:", round(ct_median, 2))

normal = df[df['상태']== 0]

mean_normal = normal['사이클타임'].mean()
print(round(mean_normal, 2))

# 실습 5
print("실습 5")
s = df['실린더압력']

q1 = s.quantile(0.25)
print(q1)
q2 = s.quantile(0.5)
print(q2)
print(q2 == s.median())
q3=s.quantile(0.75)
print(q3)

# 실습 6
print("실습 6")
print(df.describe().round(2))

mean_d = df.mean()
median_d = df.median()
gap = mean_d - median_d

result = gap.sort_values(ascending=False)
print(result.round(2))

# 실습 7
print("실습 7")
cols = ['실린더압력', '사이클타임', '비스킷두께']
q = df[cols].quantile([0.25, 0.5, 0.75])
print(q.round(2))

width = q.loc[0.75] - q.loc[0.25]
print(width.round(2))

print(width.sort_values(ascending=False))
