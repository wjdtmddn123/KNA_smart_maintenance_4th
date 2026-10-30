import os 
import csv



# 파일 입출력
# open()
# 형식: open(파일명, 모드, encoding)
# - 모드: r=읽기, w=새로쓰기, a=이어쓰기
# - encoding = "utf-8" => 한글이 깨지지 않도록 하는 것

FILE = "data/08_press.csv"

# f = open(FILE, "r", encoding="utf-8")
# lines = f.readlines()
# print(type(lines), len(lines))          # <class 'list'> 13
# f.close()           # 파일을 열고 난 후 닫기까지


# # with open - 불록이 끝나면 자동 닫힘
# with open(FILE, "r", encoding="utf-8")as f:
#     for line in f:
#         print(line)


# # write()
# with open("data/test.txt", "w", encoding="utf-8")as f:
#     f.write("쓰기 테스트")


# # 실습 2
# print("실습 2")
# with open("data/test.txt", "w", encoding="utf-8")as f:
#     f.write("2026년 10월 30일\n")
#     f.write("이상 없음\n")

# with open("data/test.txt", "r", encoding="utf-8")as f:
#     print(f.read())

# # 실습 3
# print("실습 3")
# with open("data/test.txt", "w", encoding="utf-8")as f:
#     f.write("2026년 10월 30일\n")
#     f.write("이상 없음\n")

# with open("data/test.txt", "a", encoding="utf-8")as f:
#     f.write("안녕하세요\n")
#     f.write("감사합니다\n")

# with open("data/test.txt", "r", encoding="utf-8")as f:
#     print(f.read())


# csv.reader
# with open(FILE, "r", encoding="utf-8")as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# 실습 4
# print("실습 4")
# with open(FILE, "r",encoding="utf-8")as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


# csv.writer  & 실습 5
with open("data/08_summary.csv", "w", encoding="utf-8", newline="")as f:
    writer = csv.writer(f)
    writer.writerow(["설비ID","상태"])      # 헤더
    writer.writerow(["PRESS-01", 1])
    writer.writerow(["PRESS-02", 1])

with open("data/08_summary.csv", "r", encoding="utf-8")as f:
    print(f.read())
