# replace - 바꾸기/지우기
# 형식: 문자열.replace('바꿀것','새것')
# - 모두 바꾸기, 결과 저장 필요

print('정 상 가 동'.replace(' ',''))            # 정상가동
print('010-1234-5678'.replace('-',''))          # 01012345675
print('3,000'.replace(',',''))                  # 3000
# 체이닝 활용 가능 -> 여러 종류 문자 대체 차례대로 변경

# split - 구분자로 나누기 (결과 -> 리스트)
# 형식 : 문자열.split('구분자') (구분자 생략 = 공백 기준)
print('A1 A2 A3'.split())           # ['A1', 'A2', 'A3']
print('사과,배,감'.split(','))       # ['사과', '배', '감']

print("=============")
# 실습 1
print("실습 1")
a = '설비 정상 가동'
print(a.replace('정상','점검'))

# 실습 2
print("실습 2")
b = 'PUMP A 03'
print(b.split())

# 실습 3
print("실습 3")
c = 'a,b,c,d'
print(c.split(','))

# 실습 4
print("실습 4")
d = 'a,b,c,d'
print(d.split(',',1))

print("==================")
# join - 합치기 (리스트 -> 문자열)
# 형식: '구분자'.join(리스트)   (구분자가 앞에 옴)
print('-'.join(['2025','01','15']))     # 2025-01-15

# split + join
# - split: 문자열 -> 리스트
# - join: 리스트 -> 문자열
raw = '사과, 배, 감'
p = raw. split(',')
print(p)                # ['사과', ' 배', ' 감']
print('/'.join(p))      # 사과/ 배/ 감
print('/'.join([p[0].strip(),p[1].strip(),p[2].strip()]))   # 사과/배/감

print("======================")
# 실습 5
print("실습 5")
text = ['2025','01', '15']
print('-'.join(text))

# 실습 6
print("실습 6")
print('2025', '01', '15',sep='-')
print('2025', '01', '15',sep=',')

# 실습 7
print("실습 7")
txt = '2025/01/15'
txt_a = txt.split('/')
print('-'.join(txt_a))
      
# 실습 8
print("실습 8")
csv = '1, NORMAL, 25.3'
csv_a = csv.split(',')
csv_b = csv_a[1].strip().lower()
print(csv_b)
