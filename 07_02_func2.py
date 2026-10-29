# 매개변수와 반환값

# 매개변수와 인자
# 형식:
# def 함수이름(매개변수):
#   ....
# 호출
# 함수이름(인자)

def check(name):                # name = 매개변수
    print(name + " 점검을 시작합니다.")

check("압축기1")                # "압축기1" = 인자
check("펌프1")
# check()     # TypeError: check() missing 1 required positional argument: 'name'
# check("A", "B")     # TypeError: check() takes 1 positional argument but 2 were given

# 실습 2
print("실습 2")
def report(name, temp):
    print(name, temp,"도" )
report("모터", 78)
report("펌프", 92)
report(92,"펌프")       # 인자 순서

report(temp =78, name="펌프")

# 실습 3
print("실습 3")
def report(name, temp):
    print(name,temp)
report("모터", 78)
report( temp = 92, name = "펌프")
# report(name="모터",78)      # SyntaxError: positional argument follows keyword argument
report("펌프", temp = 92)

# return
# - print: 사람이 확인할 수 있게 출력 / return: 값을 프로그램에게 돌려줘서 이어 쓸 수 있게 한다
def add(a, b):
    return a+b
    print("실행 안 됨")       # return을 만나면 즉시 함수 종류 -> 그 아래 코드는 실행 X

total = add(3, 4)
print(total)

print("==========================")
# 실습 4
print("실습 4")
def cal_avg(a, b):
    return (a + b) / 2
avg = cal_avg(80, 90)
print(avg)
print(avg + 5)      # 담은 값을 이어 씀

# 여러 값 반환 / 언패킹
# - 쉼표로 여러 값을 return 하면 튜플로 묶여서 돌아옴 -> 언패킹 가능
def min_max(values):
    return min(values), max(values)
print(min_max([75, 10, 100]))       # (10, 100)
low, high = min_max([75, 10, 100])
print(low, high)                    # 10 100

none = report("펌프", 10)
print(none)         # None -> return 값이 없는 함수 호출해서 변수를 받을 경우 None

print("===========================")
# 실습 5
print("실습 5")
def stats(v):
    return min(v), max(v), sum(v) / len(v)

lo, hi, avg = stats([78,92,85])
print(lo, hi, avg)
