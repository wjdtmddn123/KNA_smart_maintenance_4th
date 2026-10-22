# 인덱싱 - 위치 번호로 글자 하나 꺼내기
# 형식: 문자열[번호]    (첫 글자 = 0번)

word = 'PYTHON'
print(word[0], word[2], word[5])    # P T N
# 음수 인덱스: 뒤에서부터 -1, -2,...
print(word[-1],word[-2])    # N O

# print(word[6])        # IndexError: string index out of range

# 실습 1
print("실습 1")
word = 'SIGNAL'
print(word[0], word[2], word[5])

# 실습 2
print("실습 2")
word = 'SIGNAL'
print(word[-1], word[-2])

# 슬라이싱 - 구간으로 잘라내기
# 형식: 문자열[시작:끝]    (시작 포함, 끝 제외)
word = 'PYTHON'
print(word[1:4])    # YTH
# 생략 가능
# - 시작 생략 = 처음부터 (0번부터)
# - 끝 생략 = 끝까지
# - 둘다 생략 = 전체
print(word[ :3])    # PYT
print(word[3: ])    # HON
print(word[ : ])    # PYTHON
# 음수
print(word[-3:])    # HON
print(word[:-1])    # PYTHO

# 실습 3
print("===========")
print("실습 3")
word = 'SIGNAL'
print(word[0:3], word[2:5])

# 실습 4
print("실습 4")
word = 'temp_sensor'
print(word[ : 4])

# 실습 5
print("실습 5")
word = 'temp_sensor'
print(word[5: ])

# 실습 6
print("실습 6")
word = 'sensor_01'
print(word[-2: ])

# step 간격 주기
# 형식: 문자열[시작:끝:간격]
print("===========")
word = 'PYTHON'
print(word[::2])        #PTO
print(word[1::3])       #YO

# 실습 7
print("============")
print("실습 7")
word ='SIGNAL'
print(word[::2])

# 실습 8
print("실습 8")
word ='SIGNAL'
print(word[::-1])
