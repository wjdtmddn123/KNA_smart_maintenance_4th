import pandas as pd

F_SHOT = 'data/13_diecasting_shot.csv'
F_MASTER = 'data/13_diecasting_master.csv'

log = pd.read_csv(F_SHOT)
master = pd.read_csv(F_MASTER)

print(log.shape)
print(master.shape)

three = log.head(3)[["샷", "설비ID", "비스킷두께"]]
print(three.to_string(index=False))

print(three.merge(master, on="설비ID").to_string(index=False))
#  샷     설비ID  비스킷두께 라인  도입연도  정격형체력 담당반
#  1 DIE-A-01   10.0  A  2018    280  1반
#  2 DIE-B-01   11.0  B  2020    320  2반
#  3 DIE-B-01   11.0  B  2020    320  2반

# merge 기본 사용법
# - on: 두 표를 잇는 키 열
# - 행은 예측불가, 열 수는 예측 가능

# - how: 어느쪽을 다 남길 것인가
#   - (기본) how='inner'
#   - how='left' : 왼쪽은 다 남기고 짝 없으면 빈 칸
#   - how='outer': 양쪽 다 남김

m_inner = log.merge(master, on="설비ID")
m_left = log.merge(master, on="설비ID", how='left')
m_outer = log.merge(master, on="설비ID", how='outer')

print(m_inner.shape, m_left.shape, m_outer.shape)       # (185, 12) (200, 12) (201, 12)


# 실습 1
print("실습 1")

log = pd.read_csv(F_SHOT)
master = pd.read_csv(F_MASTER)

print(log.shape)
print(master.shape)

print(log.columns.tolist())
print(master.columns.tolist())

merged = pd.merge(log, master, on="설비ID")
print(merged.shape)


# 합치기 전후 점검 코드
print("----------------------------")
print(len(log))     # 200
print(len(master), master["설비ID"].nunique())    # 5 5

m_left = log.merge(master, on="설비ID", how="left")
print(len(m_left))      # 200
print(int(m_left["라인"].isna().sum()))     # 15

unmatched = m_left[m_left["라인"].isna()]
print(unmatched["설비ID"].head(1).tolist(), len(unmatched))     # ['DIE-C-01'] 15


# 실습 2
print("실습 2")
inner = pd.merge(log, master, on="설비ID")
print(len(inner))

left = pd.merge(log, master, on="설비ID", how="left") 
outer = pd.merge(log, master, on="설비ID", how="outer")
print(len(left))
print(len(outer))

print(left[left["라인"].isna()]["설비ID"].value_counts())

print(outer[outer["샷"].isna()]["설비ID"].tolist())
