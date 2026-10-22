# 메서드 - 점(.) 문법
# 형식: 문자열.메서드이름()  (--> 꼭 괄호를 붙여야 실행)
word = 'python'
# upper() : 모두 대문자 / lower() : 모두 소문자
print(word.upper())             # PYTHON
print(word.count('p'))          # 1
print(word)                     # python (원본 값 그대로)

print('NORMAL'.lower())         # normal
print('python is'.capitalize()) # Python is
print('hong gil'.title())       # Hong Gil

print("=================")
# 실습 1
print("실습 1")
posco = 'ready'
print(posco.upper())

# 실습 2
print("실습 2")
method = 'WARING'
print(method.lower())

# 실습 3
print("실습 3")
name = 'kim chul soo'
print(name.title())

# 실습 4
print("실습 4")
a = 'Fault'
b = 'FAULT'
print(a == b)
print(a.lower() == b.lower())

print("=============")
# 확인 메서드 : is*** 메서드는 참/거짓 변환
print('ABC'.isupper(), 'abc'.islower())         # True True

# 공백 정리 - strip
# 형식: .strip() = 앞뒤 공백 제거
raw = '  정상  '
print('[' + raw + ']')                          # [  정상  ]
print('[' + raw.strip() + ']')                  # [정상]

# .lstrip() -> 왼쪽 공백 제거 /.rstrip() -> 오른쪽 공백 제거
# 주의) strip은 '앞뒤' 공백만 제거, 가운데 공백 제거x
# strip() 으로 특정 문자 제거 -> strip('문자')
s = "###정상###"
print(s.strip("#"))

print("==================")
# 실습 5
print("실습 5")
text_A = 'ABC'
text_B = 'abc'
text_C = 'Abc'
print(text_A.isupper())
print(text_B.islower())
print(text_C.isupper())

# 실습 6
print("실습 6")
text_d = 'Sensor_LOG.CSV'
text_e = text_d.lower()
print(text_e.startswith('sensor'))
print(text_e.endswith('.csv'))

# 실습 7
print("실습 7")
work = ' 가동중 '
print("[" + work.strip() + "]")

# 실습 8
print("실습 8")
wait = ' 대기 '
print("[" + wait.lstrip() + "]")
print("["+ wait.rstrip() + "]")

# 실습 9
print("실습 9")
save = '***경고***'
print(save.strip("*"))

print("==============")
# 체이닝 -메서드 이어 붙이기
# 형식: 문자열.strip().lower() -> 왼쪽부터 차례로 적용
clean = '  NORMAL  '.strip().lower()
print(clean)                        #normal

# 실습 10
print("실습 10")
test = ' WARING '
print(test.strip().lower())

# 실습 11
print("실습 11")
fame = ' 경보 '
fame.strip()
print("[" + fame + "]")

fame = fame.strip()
print("[" + fame + "]")
