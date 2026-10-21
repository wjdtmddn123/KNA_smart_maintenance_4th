# 자료형

count = 3       # int 정수
temp = 25.5     # float 실수
name = "센서A"   # str 문자열

ok = True       # bool 불린형 - 참/거짓
no = False

# type() -> 자료형을 알려줌
print(type(25))         # <class 'int'>
print(type("센서A"))    # <class 'str'>
print(type(ok))         # <class 'bool'>

# 자료형마다 다른 동작
print(3 + 5)            # 8  (숫자 더하기 = 계산)
print("3" + "5")        # 35 (글자 더하기 = 이어 붙히기)


# 실습 1
print("실습 1")
count = 5
temp = 20.2
name= "센서 c"
is_ok = True
print(count, temp, name, is_ok)

# 실습 2
print("실습 2")
print(type(count), type(temp), type(name), type(is_ok))

# 실습 3
print("실습 3")
print(type(100))
print(type(100.0))
print(type("100"))

# 실습 4
print("실습 4")
print(1 + 2)
print("1" + "2")
print("12" + "34")

# 실습 5
print("실습 5")
print(3>2)      #true
print(5==5)     #true
print(type(3>2))
print(type(5==5))

# 실습 6
print("실습 6")
count = 8
print(count, type(count))
count= 8.5
print(count, type(count))
count = "8"
print(count, type(count))

# 실습 7
print("실습 7")
device_temp = 23.3
check_count = 4
device_name = "포스코"
is_normal = True
print(device_temp, check_count, device_name, is_normal)
