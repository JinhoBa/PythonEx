#0405
#문자열
str = '파이썬수업 c수업 자바수업 파이썬수업 파이썬수업'
str2 = '파이썬수업,c수업,자바수업,파이썬수업,파이썬수업'
print(str.replace('파이썬', '자바',3))
print(str.count('파이썬'))

#find, index
print(str.find('파이썬'))
print(str.index('파이썬'))
print(str.find('Vue'))#find 없는단어일때-1반환

#split
print(str.split())
print(str2.split(','))
print(str2.split('업'))

#join
print('*'.join(str))

#format
print(3,'+',4,'=',7)
print('{} + {} = {}'.format(3,4,7))
print('{1} + {0} = {2}, {2} {2} {2}'.format(3,4,7))
print('{0:10d} + {1:10.1f} = {2:10.3f}, {2} {2} {2}'.format(3,4,7))

#bool
print(type(True),type(False))
a = 'hello'
print(bool(a),bool(0),bool(''),bool(-2))
print(int(True),int(False),str(True),str(False))

#조건문
hour = 14
if hour < 12:
    print('오전')
elif hour <18:
    print('오후')
else :
    print('저녁')

lunch = input("밥 먹을래?")
if lunch == 'yes':
    print('밥을 먹고싶군요.')
    cafeteria = input('학식?')
    if cafeteria == 'yes':
        print('학식먹으러 ㄱㄱ')
    else :
        print('그럼뭐먹을래?')
        menu = input('제육:1 , 돈까스:2')
        if menu == 1:
            print('전식 제육을 먹자')
        else :
            print('돈까스를 먹으러 가자')
else:
    print('오늘은 다이어트 ㅠㅠ')

#for,while(반복문)

for i in '파이썬':
    print(i)

for i in range(2,20,2):
    print('i: ',i)

for i in range(20):
    print('i: ',i+1)

#1~10의 합 구하기
sum = 0
for i in range(1,11):
    sum += i
    print('i : {}, sum : {} '.format(i,sum))
else:
    print('for문이 정상종료 하였습니다.')
    print('1~10합은 : ',sum)

#while
sum = 0
n = 0
while n < 11:
    sum += n
    print(n,end=' ')
    n += 1
    
else:
    print('sum: ',sum) 
i = 0;
while True:
    i +=1
    print('i:',i)
    if i > 5:
        print('end')
        break
else:
    print('while end') #실행x

#단어입력을 무한 루프로 받고 
#그 글자를 3번 써줌
#exit을 입력하면 루프를 끝내고 종료
#apple을 입력하면 3번 안쓰고 다시 입력받기
while True:
    str = input('단어 입력: ')
    if str == 'exit':
        print('프로그램 종료')
        break
        print('프로그램 종료후 출력')#출력x
    elif str == 'apple':
        continue
    else:
        #print('{0} {0} {0}'.format(str))
        for i in range(3):
            print(str, end=' ')


