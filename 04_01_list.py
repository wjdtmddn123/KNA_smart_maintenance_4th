# 리스트
# 형식: 이름 = [값1, 값2, ...]
# - 리스트는 여러 값을 '순서대로' 한 이름에 담는다.

temps = [25, 26, 24, 28, 27]    # 숫자 리스트
machines = ["펌프", "모터", "압축기"]   
mixed = ["펌프", 87, True]      # 종류가 달라도 한 리스트에 담을 수 있음

print(len(temps))   # 5
print(len([]))      # 0

# 실습 1
print("실습 1")
temp = [25, 26, 24, 27, 26]
print(temp)
print(len(temp))
s = []
print(s)
print(len(s))

# 실습 2
print("실습 2")
tem = [26, 22, 27, 25, 21, 20]
print(tem[0])
print(tem[2])
print(tem[-1])

# 실습 3
print("실습 3")
line = [222, 100, 150, 250, 210, 229]
a = line[0]
b = line[-1]
print(a + b)
print((a + b)/2)

# 실습 4
print("실습 4")
mea = [21, 15, 13, 8, 5, 22, 31, 25, 28, 30]
print(mea[:3])
print(mea[-3:])
print(len(mea[:3]))

# 실습 5
print("실습 5")
save = [5, 8, 9, 45, 65, 7, 123, 21, 27, 29, 12, 2]
first = save[:6]
print(first)
second = save[6:]
print(second)
print(len(first))
print(len(second))

print("=================")
# 값 바꾸기 / in 존재 확인
# 형식: 리스트[번호] = 새 값 /값 in 리스트
nums =[25, 26, 24, 28, 27]
nums[2] = 99
print(nums)    # [25, 26, 99, 28, 27]
print("모터" in machines)


# 값 추가 - append, insert, extend
# 형식: 리스트.append(값) / 리스트.insert(위치, 값) / 리스트.extend(다른 리스트)
data = [ 25, 26, 24]
data.append(28)                 # [25, 26, 24, 28]
data.insert(1,99)               # [25, 99, 26, 24, 28]
data.extend([30,31])            # [25, 99, 26, 24, 28, 30, 31]
print(data)

# 실습 6
print("실습 6")
temp_list = [25, 26, 240, 28, 27]
print(240 in temp_list)
i = temp_list.index(240)
temp_list[i]=24
print(temp_list)
print(240 in temp_list)

# 실습 7
print("실습 7")
database = []
print(database)
database = [30]
print(database)
database.insert(0,28)
print(database)
database.extend([31,32])
print(database)

print("======================")
# 값 삭제 - remove, pop, del
# 형식: 리스트.remove(값) / 꺼낸 값 = 리스트.pop(위치) / del 리스트[위치]
d = [25, 26, 24, 28, 27]
d.remove(24)
print(d)                # [25, 26, 28, 27]
got = d.pop(1)
print(got, d)           # 26 [25, 28, 27]
del d[0]
print(d)                # [28, 27]

print("=======================")
# 정렬, 탐색 - sort, reverse / count, index
# 형식: 리스트.sort() / .reverse() / .count(값) / .index(값)
l = [27, 24, 30, 22, 26]
# l.sort()
# print(l)        # [22, 24, 26, 27, 30]
# l.sort(reverse =True)   
# print(l)        # [30, 27, 26, 24, 22]
l.reverse()       # [26, 22, 30, 24, 27]
print(l)

r = ["정상", "이상", "정상", "정상", "이상"]
print(r.count("정상"), r.index("이상"))         # 3 1

# 실습 8
print("실습 8")
k = [25, 26, 999, 24, 28, 26]
k.remove(999)
print(k)
god = k.pop(1)
print("꺼낸 값",god)
del k[0]
print(k)

# 실습 9
print("실습 9")
t = [ 24, 26, 22, 24, 30, 28, 27]
t.sort()
print(t)
t.reverse()
print(t)
print(t.count(24), t.index(24))
