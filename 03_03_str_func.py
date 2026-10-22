# 문자열 연산과 검색
# - 문자열 연결(+), 반복(*)

# len() - 글자 수
# 형식: len(문자열)
print(len('PYTHON'))            # 6
print(len('AI 분석'))           # 5 (공백도 글자 수에 포함)
print(len(''))                  # 0 (빈 문자열)


# in / not in - 포함 / 불포함 여부 (결과 bool)
# 형식: '찾을 것' in 문자열
print('고장' in '설비 고장 발생')   # True
print('정상' not in '고장 발생')    # True

# count
# 형식: 문자열.count('x') -> 개수
print('banana'.count('a'))          # 3
# find
# 형식: 문자열.find('x') -> 처음 나오는 위치
print('banana'.find('a'))           # 1
print('banana'.find('t'))           # -1 (못 찾을 경우)


# 실습 1
print("====================")
print("실습 1")
number = '01012345678'
print(len(number))

# 실습 2
print("실습 2")
message = '설비 고장 발생'
print('고장' in message)
print('정상' in message)

# 실습 3
print("실습 3")
word = 'sensor-01-temp'
print(word.count('-'))

# 실습 4
print("실습 4")
temp = 'temp_2024'
print(temp.find('_'))
print(temp.find('9'))


print("==================")
# index
# 주의) 위치를 반환하지만 없으면 오류
email = 'hong@company.com'
at = email.index('@')
print(at)
print(email[:at])       # hong

# startswith / endswith
# 형식: 문자열.startswith('x') -> bool
print('EQP-001'.startswith('EQP'))      # True
print('cmapss.csv'.endswith('csv'))     # True

print("================")

# 실습 5
print("실습 5")
sensor = 'sensor_log.csv'
print(sensor.startswith('sensor'))
print(sensor.endswith('.csv'))

# 실습 6
print("실습 6")
label = 'WARING'
print(label == 'WARING')
print(label == 'waring')
