# 각종 예외 상황
# temp = int("스물")      # ValueError: invalid literal for int() with base 10: '스물'
# result = 10 / 0     # ZeroDivisionError: division by zero
# print(undefined_var)    # NameError: name 'undefined_var' is not defined


# try-except 구조
# try:
#     temp = int("스물")      
# except ValueError:
#     print("ValueError")

# try:
#     result = 10 / 0    
# except ZeroDivisionError:
#     print("ZeroDivisionError")

# try:
#     print(undefined_var)
# except NameError:
#     print("NameError")

# # 실습 2
# print("실습 2")
# try:
#     temp = int(input("온도: "))
#     print("온도는 ", temp)
# except ValueError:
#     print("숫자를 입력하세요")
# print("프로그램 계속")

# 여러 except
# row = "P-01,102".split(",")
# try:
#     code_no = int(row[3])
# except ValueError:
#     print("숫자 아님")
# except IndexError:
#     print("칸 부족")

# 실습 3
try:
    number = int(input("숫자를 입력하세요: "))
    print(100 / number)
except ValueError:
    print("숫자 아님")
except ZeroDivisionError:
    print("0으로 나눌 수 없다")
