import pandas as pd

F_SHOT = 'data/13_diecasting_shot.csv'

# 조건 필터링과 정렬
df = pd.read_csv(F_SHOT)
print(df.shape)

# 배열에서 하던 것
arr = df["비스킷두께"].values
print("배열에서 조건 참 개수:", int((arr >=16).sum()))      # 74

# 표에서 하는 것
print("표에서 조건 참 개수:", int((df["비스킷두께"] >=16).sum()))   # 74

# 조건 -> boolean Series
s = df["비스킷두께"] >= 16
print(s.head(3).tolist())       # [False, False, False]

print(int(df["비스킷두께"].isna().sum()))       # 14
print(int((df["비스킷두께"] < 16).sum()))       # 200 - 74


# 실습 1
print("실습 1")
df = pd.read_csv(F_SHOT)
print(df.shape)
print(int((df["비스킷두께"] >= 20).sum()))

print(int(df["비스킷두께"].isna().sum()))
print(int((df["비스킷두께"] < 20).sum()))


# 복합 조건 : &, |
both = df[(df["비스킷두께"] >= 16) & (df["사이클타임"] >= 25)]
either = df[(df["비스킷두께"] >= 16) | (df["사이클타임"] >= 25)]
print(len(both), len(either))

# 부정 조건 : ~
print(len(df[~(df["품질등급"]== "불량")]))

# isin : 값이 포함되어 있는지
print(len(df[df["품질등급"].isin(['주의', '불량'])]))   # | 사용과 같은 결과

# between : 사이를 의미(양쪽 경계 모두 포함)
print(len(df[df["비스킷두께"].between(10, 16)]))

# 문자열 조건
# - 숫자 열에는 쓸 수 없음
# - str.contains : 해당 문자열을 포함하는 값
print(len(df[df["설비ID"].str.contains("A")]))      # A라인 전체

# - str.split, str.replace, str.strip ..
print(df["설비ID"].head(1).tolist())    # ['DIE-A-01']
print(df["설비ID"].str.split("-").head(1).tolist())     # [['DIE', 'A', '01']]


# 실습 2
print("실습 2")

both = df[(df["비스킷두께"] >= 16) & (df["사이클타임"] >= 25)]
either = df[(df["비스킷두께"] >= 16) | (df["사이클타임"] >= 25)]
print(len(both), len(either))
print(len(df[~(df["품질등급"]== "불량")]))


# 실습 3
print("실습 3")
a = df[df["품질등급"].isin(['주의', '불량'])]
print(len(a))

b = df[df["비스킷두께"].between(10, 16)]
print(len(b))

c = df[df["설비ID"].str.contains("A")]
print(len(c))

d = df[df["설비ID"] == "DIE-A-01"]
print(len(d))


# 정렬, 복사본
# 정렬 - sort_values
# - 기본값은 작은 값부터인 오름차순
# - 한 열로 정렬해도 모든 열이 행 단위로 함께 이동한다
asc = df.sort_values("비스킷두께")
print(asc["비스킷두께"].head(3).tolist())   # [2.0, 2.0, 4.0]

# 다중 키 정렬, 내림 차순
dec = df.sort_values("사이클타임", ascending=False)
print(dec["사이클타임"].head(3).tolist())   # [6170.0, 652.3, 125.9]

# 다중 키 정렬
two = df.sort_values(["품질등급", "비스킷두께"], ascending=[True,False])
print(two["샷"].head(3).tolist())       # [198, 192, 197]


# copy
x = df[df["품질등급"] == "불량"].copy()
print(x.shape)      # (20, 8)
x["위험등급"] = "높음"
print(x.shape)      # (20, 9)


# 실습 4
print("실습 4")
top = df.sort_values("비스킷두께",ascending=False)
print(top["샷"].head(5).tolist())

two = df.sort_values(["품질등급", "사이클타임"],ascending=[True,False])
print(two["샷"].head(5).tolist())

print(df["샷"].head(3).tolist())


# 실습 5
print("실습 5")
a = df[(df["품질등급"] != "양품") & (df["비스킷두께"] >= 16)]
print(len(a))

result = a.sort_values("비스킷두께", ascending=False)
print(result[["샷", "비스킷두께", "품질등급"]].head(5))

miss = df[(df["품질등급"] != "양품") & (df["비스킷두께"].isna())]
print(len(miss))

# 실습 5 정답
state = df[(df["품질등급"] != "양품") & (df["비스킷두께"] >= 16)]
print(len(state))

sort_df = state.sort_values("비스킷두께", ascending=True)
report=sort_df[["설비ID", "비스킷두께", "품질등급"]]
print(report.head(3))
#          설비ID  비스킷두께 품질등급
# 120  DIE-A-01   19.0   주의
# 122  DIE-C-01   19.0   주의
# 123  DIE-B-02   19.0   주의

# 결측 때문에 제외된 양품 아닌 샷 확인
x = df[(df["품질등급"] != "양품") & df["비스킷두께"].isna()]
print(len(x))       # 3
