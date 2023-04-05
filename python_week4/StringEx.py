#문자열
'''
a = 'python'
print(a[0], a[1], '...', a[5])
print('python'[0], 'python'[1], '...', 'python'[5])
str = 'Hello python!'
n = len(str)
print('문자열 ',str,' 길이 ', n)
print(a[0:3])
print(a[0:len(a)])
print(str[-5:-1])
print(str[-9:])
#step
print(str[::1])
print(str[::-1]) #역순
print(str[2:9:3])   

school = '동양미래대학교-컴퓨터소프트웨어공학과'
print(school[::])
print(school[::2])
print(school[8::2])
print(school[:15:4])
print(school[::-1])
'''
''' escape sequence characters
\\ 역슬래시
\' 작은 따옴표
\" 큰 따옴표
\n 새 줄
\t 수평 탭
\v 수직 탭
\b Backspace, 지우기

print('\\ \' \" \t hello\b \v ooo')
'''
# funtion 독립적으로 동작 method 클래스에 종속 
# ex)str클래스에서만 사용하는 replace(),find()
str_a = '하하하'
str_b = str_a.replace('하','호',1)
print(str_a.replace('하','호'))
print(str_b)
str_c = '파이썬 수업입니다.파이썬.파이썬.파이썬.파이썬.파이썬.파이썬.파이썬.파이썬.파이썬.파이썬.파이썬.'
print(str_c.replace('파이썬','자바',5))

n = (input('6자리 실수 입력 : '))
n = n.replace('.','')

sum = 0
print('sum : ',int(n[0])+int(n[1])+int(n[2])+int(n[3])+int(n[4])+int(n[5]))
for i in range(6):
    sum += int(n[i])


