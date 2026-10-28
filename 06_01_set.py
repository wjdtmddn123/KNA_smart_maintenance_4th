# 셋 - 중복 자동 제거, 순서 없음
# 형식: {값1, 값2} 또는 set(리스트)
# - 빈 셋 set()
logs = ["S01", "S02", "S01", "S03"]
unique_logs = set(logs)
print(unique_logs)    # {'S02', 'S01', 'S03'}  # 셋은 순서가 없어 인덱싱 불가
print(sorted(unique_logs))          # ['S01', 'S02', 'S03']

# add - 값 추가 / in - 포함 확인
alerts = {"S01", "S02"}
alerts.add("S03")
print(alerts)
print("S02" in alerts)

# 실습 4
print("실습 4")
sensor_id = [ "S01","S02","S01", "S03","S02"]
unique_sensor_id = set(sensor_id)
print(sorted(unique_sensor_id))
print("종류 수:",len(unique_sensor_id))



# 집합 연산 - union(전체) / inntersection(공통) / difference(차이)
line_a = {"S01", "S02", "S03"}
line_b = {"S03", "S04"}
print(line_a.union(line_b))
print(line_a.intersection(line_b))
print(line_a.difference(line_b))

print("===============================")
# 실습 5
print("실습 5")
sensor_A = {"S01", "S02", "S03","S05"}
sensor_B = {"S03", "S04", "S05"}
print("전체:", line_a.union(line_b))
print("공통:", sensor_A.intersection(sensor_B))
print("A만:", line_a.difference(line_b))
print("B만:", line_b.difference(line_a))

# 실습 6
print("실습 6")
yesterday = {"S01", "S02", "S03"}
today = {"S02","S03","S05"}
print("신규 이상:", today.difference(yesterday))
print("지속 이상:", today.intersection(yesterday))
