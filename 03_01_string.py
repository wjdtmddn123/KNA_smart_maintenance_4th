# 문자열
# - "", '' 감싸서 표현

# 여러줄 문자열
# 형식: 삼중 따옴표 """ 적을 내용.. """
notice = """
설비 점검 안내
1. 전원 확인
2. 센서 점검
"""
print(notice)

# 이스케이프 : \n(줄바꿈), \t(탭)
print("이름\t상태")
print("첫줄\n둘째 줄")


# 실습 1
print("실습 1")
Notice = """
가동 점검표
1. 온도 확인
2. 압력 확인
"""
print(Notice)

print("가동 점검표\n1. 온도 확인\n2. 압력 확인")

# 실습 2 
print("실습 2,3")
code = "PUMP_A"
state = "정상"
date = "2025-01-15"

print(code + "/" +state + "/" + date)

# 실습 3
hours = 1200
card = "설비: " + code + "\n상태: " + state + "\n가동시간: " + str(hours) + "\n점검일자: " + date
print(card)


