# 실습 1
print("실습 1")
temp = [25, 27, 32, 35, 31]
for i in temp:
    if i >= 30:
        print("고온:", i)

# 실습 2
print("실습 2")
work = [4, 12, 8, 10, 9, 6,5,10]
for i in work:
    if i >= 5 and i <= 10:
        print(i)


# 최대, 최소
temps = [25, 32, 28, 36, 27, 31]
biggest = temps[0]
for t in temps:
    if t > biggest:
        biggest = t         # 더 큰값일 때 갱신
print(biggest)


# 빈 리스트 채우기
doubled = []
for t in temps:
    doubled.append(t * 2)
print(doubled)

print("=======================")
# 실습 3
print("실습 3")
temp = [32, 36, 31, 25, 28, 21]
total = 0
count = 0
for i in temp:
    if i > 30:
        total += i
        count += 1
print("고온 평균:", total/count)

# 실습 4
print("실습 4")
temp = [32, 28, 35, 20, 31, 33, 28]
empty =[]
for t in temp:
    if t > 30:
        empty.append(t)
print(empty)
print("개수", len(empty))

print(temp)
print("개수",len(temp))

# 실습 5
print("실습 5")
temp_list = [25, 26, 24, 28, 27]
temp_empty =[]
for t in temp_list:
    temp_empty.append(t * 1.8 + 32)
print(temp_empty)

print("원본:", temp_list)

print("==============================")

# 중첩 리스트 - 리스트 안에 리스트
# - 표(행,열)처럼 한 줄에 여러 값이 묶인 데이터. 바깥 반복은 '행', 안쪽 인덱스로 '열'
rows = [["펌프", 25], ["모터", 32], ["압축기", 28]]
for row in rows:
    print(row[0], "온도", row[1])

print("=====================================")    
# 실습 6    # 좀 많이 어렵네
print("실습 6")
temps = [25, 32, 28, 35, 27, 31, 24, 33, 29, 36]
total = 0
hot =[]
for t in temps:
    total +=t

    if t>30:
        hot.append(t)

hot_total = 0
for h in hot:
    hot_total += h

print("전체 평균:", total / len(temps))
print("고온 개수:",len(hot))
print("고온 평균:",hot_total / len(hot))
