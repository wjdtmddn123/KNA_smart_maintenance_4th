# 모듈 / 패키지 / 라이브러리
# - 모듈: 기능을 모아둔 .py 파일 하나
# - 패키지: 모듈을 모아둔 폴더
# - 라이브러리: 위에 사항들을 통칭

# import 방식
# 형식: import 모듈 / from 모듈 import 기능 / import 모듈명 as 별칭
import math                 # math 라는 모듈을 통째로 불러옴
print(math.sqrt(16))        # 4.0
from math import sqrt, ceil         # 일부만 불러옴 -> 모듈명 없이 바로 사용
print(sqrt(16), ceil(4.2))          # ceil 은 올림 함수

import math as m
print(m.sqrt(16))

# 실습 1
print("실습 1")
import math
print(math.sqrt(16), math.ceil(4.2))        # 1단계: 모듈명.기능()
from math import sqrt, ceil       
print(sqrt(16), ceil(4.2))                  # 2단계: from 모듈 import 기능
import math as su 
print(su.sqrt(16), su.ceil(4.2))            # 3단계 : import 모듈 as 별명.기능()              


# 표준 라이브러리 - math / random / datetime
# - 파이썬 설치 시 함께 깔리는 검증된 모듈들
import random
import datetime

print(random.randint(1,100))
print(datetime.datetime.now())

print("==================")
# 실습 2
print("실습 2")
import random
import math
value = random.randint(1,1000)

print(value)

print(math.sqrt(value))


# ///////////////
# 경로와 os 모듈
# - 파일을 다루려면 어디에 있는지 경로를 알아야 한다
# 1) 절대경로
#   - 최상위부터 전체 주소      ex) C:\Users\wjdtm\OneDrive\바탕 화면\posco
# 2) 상대경로
#   - 지금 실행중인 위치를 기준으로 한 주소

import os 
print("현재 실행 위치(절대경로):", os.getcwd())

# 폴더 유무 확인
print(os.path.exists("data"))   # True

# 폴더 목록 확인
files = os.listdir("data")
print(files)            # ['08_press.csv']


print("========================")
# 실습 3
print("실습 3")
import os
print(os.getcwd())              # 현재 작업 폴더
files = os.listdir("data")      
for file in files:
    print(file)

print("-----------------------------")
for file in files:
    if file.endswith(".csv"):
        print(file)

print("-----------------------------")
# 폴더명 + 파일명 -> 경로
path = os.path.join("data", "08_press.csv")

if os.path.exists(path):
    print("파일 경로:", path)


print("=============================")
# 실습 4
print("실습 4")
import os 
path = os.path.join("data","test.txt")
print(os.path.exists(path))         # True

if os.path.exists(path):
    print("파일 있음")
else:
    print("파일 없음")


# 실습 5
print("실습 5")
import os
import datetime

files = os.listdir("data")
now = datetime.datetime.now()

print(f'파일 {len(files)}개, 점검 시각 {now}')


# 실습 6
print("실습 6")
import os
files = os.listdir("data")

csvs = []
for n in files:
    if n.endswith(".csv"):
        csvs.append(n)

print("[CSV]")
for n in csvs:
    path = os.path.join("data", n)
    print(" - ", path)
