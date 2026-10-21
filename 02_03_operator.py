# 연산자
# - 산술, 비교, 논리 연산자

# 산술 연산자
# 형식: +, -, *, /, // (몫), % (나머지), ** (거듭제곱)

# 우선순위
# - 곱셈, 나눗셈 등이 우선, 괄호를 이용하여 변경 가능

# 복합 할당
# 형식: score += 10 <-> score = score + 10
score = 100
score +=10
print(score)
# -=, *=, /= 

# 문자열 연산
# +, * 가능
print("안녕" + "하세요")    # 안녕하세요 -> 이어붙이기
print("-" * 4)      # ---- -> 반복
# 주의) 자료형이 같은 것끼리 연산 할 수 있다


# 실습 1
print("실습 1")
a = 17
b = 5
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b ) 

# 실습 2
print("실습 2")
a = 80
b = 91
c = 90
print((a + b + c) / 3 )
side = 7
print(side ** 2)
print(3 * 4 * 5)

# 실습 3
print("실습 3")
a = 5
b = 3
print(a == b, a != b, a > b, a < b, a >=b, a<=b)

# 비교 연산자
# 형식: == (같다) != (다르다) < > <= >=
print(5 == 5) # True
print( "정상" == "정상") # True
print("A" == "a")  # False

# 논리 연산자
# - and : 모두 참이어야 함, or: 하나만 참이어도 참, not: 반대
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# 실습 4
print("실습 4")
temp = 85
temp_ok = 60 <=temp and temp <=90
print(temp_ok)
pressure = 5
pressure_ok = 3<= pressure and pressure <=7 
print(pressure_ok)
print(temp_ok and pressure_ok)

# 실습 5
print("실습 5")
재고 = 100
print(재고)
재고+=50
print(재고)
재고-=30
print(재고)
재고+=5
print(재고)

# 실습 6
print("실습 6")
total = 500
fault = 23
불량률 = fault / total * 100 
print("불량률",불량률, "%")

operate = 21 
time = 24
가동률 = operate / time * 100
print("가동률", 가동률, "%")

# 실습 7
print("실습 7")
total_time = 500
hours = total_time // 60
minutes = total_time % 60
print(hours, "시간", minutes, "분")
