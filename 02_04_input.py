# 입력 (input)
# 주의) 사용자 입력은 항상 "문자열"
# 형식: 변수 = input(" 안내문구: ")
name = input("이름: ")
age = input("나이: ")
print(name)

# 형변환 - int(), float(), str()
# print(age + 1)          # TypeError
print(int(age) + 1)     # int() 형변환 후 실행


# 실습 1
print("실습 1")
birth_year = int(input("태어난 해를 입력하세요: "))
age = 2026 - birth_year + 1
print("나이:",age, "세")

height = float("173.5")     # float() 실수 변환
print(height, type(height))

print("나이:" + str(30))


# 실습 2
print("실습 2")
nation = input("거주 국가를 입력하세요: ")
city = input("거주 도시를 입력하세요: ")
print(nation, "의", city, "에서 거주하시는군요!")

# 실습 3
print("실습 3")
a = int(input("숫자 1을 입력하세요: "))
b = int(input("숫자 2를 입력하세요: "))
print("합: ", a + b)
print("차: ", a - b)
print("곱: ", a * b)
print("나눗셈: ", a / b)

# 실습 4
print("실습 4")
temp = int(input("온도를 입력하세요: "))
print("30 초과?", temp >30)



# 실습 5
print("실습 5")
a = int(input("점수 1을 입력하세요: "))
b = int(input("점수 2를 입력하세요: "))
c = int(input("점수 3을 입력하세요: "))
avg = (a + b + c) / 3
print(" 50 초과", avg > 50)
