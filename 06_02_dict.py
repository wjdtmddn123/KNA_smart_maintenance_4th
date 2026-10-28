# 딕셔너리
# 형식: {키: 값, 키: 값} - 키는 문자열
# - 리스트는 번호(인덱스)로 찾지만 딕셔너리는 이름(키)으로 찾는다

sensors ={"모터온도": 78, "진동": 0.5}
print(sensors)
print(sensors["모터온도"])      # 78
print(type(sensors))           # <class 'dict'>
# print(sensors["유량"])          # KeyError -> 없는 키를 조회 시 에러

# 추가 / 수정 / 삭제
# 형식: 딕셔너리[키] = 값   (없는 키 - 추가, 있는 키 - 수정)
# 형식: (삭제) del 딕셔너리[키]

sensors["펌프압력"] = 95        # 추가
sensors["모터온도"] = 80        # 수정
del sensors["진동"]             # 삭제
print(sensors)                 # {'모터온도': 80, '펌프압력': 95}

# get / in
# 형식: 딕셔너리.get(키, 기본값)    / 키 in 딕셔너리
print(sensors.get("유량"))      # None
print(sensors.get("유량", 0))   # 0
print("모터온도" in sensors)    # True  (키만 포함 여부 확인 가능)
print(80 in sensors)           # False (값은 확인 안됨)

print("=========================")
# 실습 1
print("실습 1")
sensor = {"모터온도": 78, "펌프압력": 89, "회전속도": 1750}
print(sensor["모터온도"])
sensor["유량"] = 52
sensor["회전속도"] = 2150
print(sensor)
print(sensor.get("베어링진동",0))
print("펌프압력" in sensor)

print("==========================")
# keys / values / items / len
sensors = {"모터온도": 78, "진동": 0.5}
print(list(sensors.keys()))             # ['모터온도', '진동']
print(list(sensors.values()))           # [78, 0.5]
avg = sum(sensors.values()) / len(sensors)
print(avg)          # 39.25

for name, value in sensors.items():
    print(name,value)

# for k in sensor.keys()
# for v in sensor.values()

# update - 여러 항목 한번에 갱신(키가 있으면 수정, 없으면 추가)
d = {"온도": 78}
d.update({"온도": 80, "압력": 95})
print(d)

print("============================")
# 실습 2
print("실습 2")
sensor_d = {"모터 온도": 78, "진동": 0.2,"유량": 52}
new = {"모터 온도": 82, "진동": 0.4, "유량": 42}
sensor_d.update(new)
print(sensor_d)
del sensor_d ["유량"]
print("센서 수:", len(sensor_d))

# 실습 3            # (어렵네)
print("실습 3")
sensors = {"온도": 80, "진동": 55, "압력": 95}
avg = sum(sensors.values()) / len(sensors)
print("평균:", round(avg, 1))

top = ""
high = 0
for name, value in sensors.items():
    if value > high:
        high = value
        top = name
print("최댓값 센서:", top, high)

print("==============================")
# zip : 센서명 - 값 매핑하기
names = ["온도", "진동", "압력"]
values = [78, 0.5, 95]
sensors = dict(zip(names, values))
print(sensors)                  # {'온도': 78, '진동': 0.5, '압력': 95}

# 딕셔너리의 값에 리스트/딕셔너리 - 중첩 딕셔너리
plant = {
    "1번모터": {"온도": 78, "상태": "정상"},
    "2번펌프": {"압력": 95, "상태": "경고"}
}

print(plant["2번펌프"]["압력"])         # 95

# 실습 4
print("실습 4")
name_list = ["온도", "진동","압력"]
value_list = [78, 0.5, 95]
sensors = dict(zip(name_list, value_list))
print(sensors)
for name_list, value_list in sensors.items():
    print(name_list, value_list)

# 실습 5
print("실습 5")
value_mea = {"온도": 77, "진동": 0.1, "압력": 55}
value_lim = {"온도": 70, "진동": 0.3, "압력": 65}
warning = []
for name,value in value_mea.items():
    if value > value_lim[name]:
        warning.append(name)
print("경고 센서",warning)      # ['온도']

# 실습 6
print("실습 6")
equip = {
    "1번펌프": {"온도": 80, "상태": "정상"},
    "2번펌프": {"압력": 95, "상태": "경고"},
    "3번펌프": {"유량": 72, "상태": "정상"}
}
print(equip["2번펌프"]["압력"])
for name, info in equip.items():
    if info["상태"] == "경고":
        print(name, "점검 필요")


print("=================================")
# 실습 7
print("실습 7")
plant = ["온도, 78", "압력, 95", "진동, 0.5"]
plant_split ={}
for p in plant:
    name, value = p.split(",")
    plant_split[name] = float(value)
print(plant_split)

# 실습 8
print("실습 8")
value_s = {"온도": 95, "압력": 96}
limit_s = {"온도": 90, "압력": 90}
avg = sum(value_s.values()) / len(value_s)
print("평균:", avg)
# items()순회 -> 임계값 비교 -> 초과한 값은 셋에 담기(키 값 담기)
danger = set()
for name, v in value_s.items():
    if v > limit_s[name]:
        danger.add(name)
# 셋 정렬하여 출력
print("위험센서:", sorted(danger))
