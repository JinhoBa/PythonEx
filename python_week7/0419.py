##0419
'''
l1 = [1,2,3,4]
# tuple 항목의 순서나 내용의 수정이 불가능, 괄호 생략 가능
t1 = (1,2,3,42,2,3,4,5,6,2)
print(l1)
print(t1)
print(t1.count(2))
print(t1.index(2))

#커피숍 프로그램 
menu = '아메리카노','라떼','유자차'
#아이스티 추가
menu1 = list(menu) # 튜플을 리스트로 변환
print(menu1)
menu1.append('아이스티')
print(menu1)
menu = tuple(menu1)
print(menu)
t4 = 10
print(type(t4))
t4 = 10,   # 튜플로 저장
print(type(t4))

lst =[]
lst.sort()
sorted(lst)
print(sorted(t1)) # 튜플은 sorted를 이용해 정렬된 데이터를 출력가능 저장은x

for i in 1,2,3,4,5:  # 튜플 사용
    print(i)

# dictonary ------------------------------------------------------------------------------------
#d = { k1:v1, k2:v2, k3:v3 } # key 값은 중복 불가, 수정 불가
student = {}
d2 = dict()
#dictionary 값 추가 방법 1
student[101] = '홍길동'
student[102] = '김철수'
student[103] = '배진호'
print(student)
print('student[101]: ',student[101])  # dic[key값]
print('student[102]: ',student[102])

# print(student[0]) KeyError []에 index가 아니라 key값을 넣어야함
lec = {}
lec['강좌명'] = '파이썬'
lec['개설년도']= 2023
lec['수강생'] = ['김','이','박']
lec['인원'] = 35
print(lec) # key값의 type은 상관 없다 (list,tuple,dic도가능)
lec['인원'] = 20
print(lec)
#dictionary 값 추가 방법 2
lec.update({'인원':10}) # 같은 key값에 value 변경
print(lec)
lec.update({'강의실':213,'교수':'이희진'}) # key값이 없다면 dic에 추가
print(lec)

# dictionary methods -----------------------------------------------------------------------------------
month = {1:'1월',2:'2월',3:'3월',4:'4월',5:'5월',6:'6월',7:'7월',8:'8월',9:'9월',10:'10월',11:'11월',12:'12월'}
print(month.values())
for key in range(1,13):
    print(month[key], end=' ')
print()

print(month.values()) # value로 구성된 리스트 반환
print(month.keys()) # key로만 구성된 리스트로 반환
print(month.items()) # (key,value)쌍의 튜플이 들어있는 리스트 반환
print('#3')    
for key in month.keys():
    print(key,': ',month[key],end=' ')
print('#4')    
for value in month.values():
    print(value, end=' ')
print()

for item in month.items():
    print("key:   ",item[0])
    print("value: ",item[1])

for key,value in month.items():
    print('{} : {}'.format(key,value))

for item in month:
    print(item) # 키값만 출력

print(month.get(44))  #get(key값) 존재하지 않으면 None출력
#print(month[33]) # KeyError
print(month)
print(month.pop(1))  # key값을 줘야함 , key에 해당하는 value를 반환후 삭제
print(month)
print(month.popitem())  # 맨마지막 삭제, key와 value를 튜플 형태로 반환 
print(month)

#  zip(), enumberate() ----------------------------------------------------------------
l1 = [1,2,3,4,5]
l2 = ['a','b','c']
l3 = [9,8,7,6,5]

l1 = ['한식','일식','중식']
l2 = ['전주식당','전가복','초밥집']
l3 = ['제육','탕수육','연어초밥']  # 가장 작은 개수기준으로 생성
z = zip(l1,l2,l3)
print(type(z))
print(list(z))
# l2 ->> key  l3 ->> value
z1 = zip(l2,l3)
print(dict(z1))

# z1 = zip(l1,l2,l3) 
# print(dict(z1)) ValueError

z2 = zip(l1,zip(l2,l3))
print(dict(z2))

# 1개 리스트를 dictionary로 변경
# enummerate 0부터 시작하는 첨자와 항목 값의 튜플 리스트 생성
l4 = ['제육','탕수육','연어초밥']
print(type(enumerate(l4)))
print(list(enumerate(l4)))
'''
# 문제  
# 과목을 주면 강의실을 알려주는 함수
# 1) dictionary로 변환해서 활용
# 2) 무한루프로 강의실을 알려줘라
# 3) quit 이라는 단어가 들어오면 , 종료
# 4) 다른과목을 물어보면,'몰라요'출력 후 다시 물어보기
# 5) 해당 과목에대한 강의실을 알려줌
subject = ['파이썬','자바','C++','AI','알고리즘']
classroom = [101,102,103,104,105]
d1 = dict(zip(subject,classroom))
'''
while True:
    n = (input('과목명을 입력하세요 >> '))
    if n == 'quit':   # quit 입력 확인
        print('프로그램 종료')
        break
    count = 0
    for i in d1.keys(): 
        if i == n:
            print('강의실 번호: ',d1[i])
            count +=1
    if count == 0:
        print('몰라요~')
        continue
'''
while True:
    n = (input('과목명을 입력하세요 >> '))
    if n == 'quit':   # quit 입력 확인
        print('프로그램 종료')
        break
    if n in d1.keys(): 
        print('강의실 번호: ',d1[n])
    else:
        print('몰라요~')
        continue
        
            
