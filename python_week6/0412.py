# 0412
# 리스트 [] , 튜플(), 딕셔너리 {}
'''
리스트 = ['김밥', '떡볶이','돈가스']
튜플 = ('김밥', '떡볶이','돈가스')
{ key1:value1, key2:value2}
'''
# json 형식 - key : value
# 리스트와 튜플의 차이점 : 튜플은 수정이 불가

# 리스트 1. 빈리스트를 만들어서 원소를 추가하는 방식

lst = []
print(type(lst))
lst.append('김밥') # append 마지막 인덱스에 추가
lst.append('햄버거')
lst.append('감자튀김')
lst.append('탕수육')
lst.append('파스타')
lst.insert(0,'돈가스')  # list.insert(index, value) 특정 인덱스에 추가
lst.insert(0,'샌드위치')
lst.append('탕수육')
lst.append('탕수육')
lst.append('탕수육')

print(lst)
print('list에서 3번째에 있는 값 : ',lst[2])
for i in range(len(lst)):
    print('lst[{}] : {}'.format(i,lst[i]))
n = 0
for i in lst:
    print('list[',n,']',i)
    n +=1
print(lst.count('탕수육'), lst.index('탕수육'))
# slicing --------------------------------------------------
print(lst[::])
print(lst[:len(lst):1])
print(lst[0:8:2]) # 샌드위치 김밥 감자튀김 파스타
print(lst[3:7:1]) # 햄버거 감자튀김 탕수육 파스타
print(lst[::-1]) # 역순 출력
print(lst[0:6:2]) # 샌드위치 김밥 감자튀김 
# remove ----------------------------------------------------
lst.remove('김밥')
lst.remove('탕수육') #여러개일때 맨앞의 값 삭제
print(lst)
# lst.remove('커피') -> ValueError
# >> if문을 사용해서 오류 방지
item1 = '커피'
if item1 in lst:
    print('커피 존재함')
    lst.remove(item1)
else:
    print('커피 존재 안함')
# pop ----------------------------------------------------------
print(lst.pop())
print(lst)
print(lst.pop(2))
print(lst)

dessert = ['케잌','커피','우유','와플']
print(dessert)
lst.extend(dessert) # List1 = List1 + List2 
print(sorted(lst))
print(lst)
# 함수 ---------------------------------------------------------
l1 = ['orange','apple','mango','kiwi', 'banana']
print(sorted(l1))
print(l1)
l1.sort()
print('sort()실행'.center(40,'-'))
print(l1)
l1.reverse()
print(l1)
l1.clear() # 빈 리스트 반환
print(l1)

del l1 # 메모리에서 l1을 삭제

# 리스트 컴프리 핸션 ------------------------------------------
# 리스트를 선언할때, 짧게, 빠르게 간결하게 하고싶다.
# 1) 선언
l2 = [0,1,2,3,4,5,6,7,8,9,10]
print(l2)

# 2) for 문으로 append
l3 = []
for i in range(11):
    l3.append(i)
print(l3)

# 3) 리스트 컴프리핸션 [value for item in range(len(list)]
l4 = [i for i in range(11)] #  ':'없음
print(l4)

# 4) 0~10 까지 숫자의 제곱을 리스트에 넣어라
l5 = [i**2 for i in range(11)]
print(l5)
# 5) 0~10 까지 숫자의 3배수를 리스트에 넣어라
l6 = [i*3 for i in range(11)]
print(l6)
# 6) 'hello'를 10번 넣기
l7 = ['hello' for i in range(10)]
print(l7)
# 7) 0~10 까지 짝수들의 제곱을 리스트에 넣어라 0,3,16...
l8 = [i**2 for i in range(0,11,2)]
#  = [i**2 for i in range(11) if i % 2 == 0]
print(l8)
l9 = [i**2 for i in range(11) if i % 2 == 0 if i % 3 == 0]
print(l9)

#중요 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!-------------------------------
# list 복사
a = [0,4,16,36,64,100]
b = a       
# b에 a의 주소값(배열)을 저장 (shallow copy)
print('a: ',a)
print('b: ',b)
a.pop()
print('after pop')
print('a: ',a)
print('b: ',b)
print(a is b) # is -> 메모리값이 같은지 확인  return True or False
b.append('333')
print("after b.append('333')")
print('a: ',a)
print('b: ',b)
# deep copy (새로운 메모리에 배열 복사)
c = a[:]
# c = a.copy() 
# c = list(a)  3개의 방식 모두 deep copy 
print('a:',a)
print('c:',c)
a.pop()
print('after pop')
c.append('777')
print("after c.append('777')")
print('a:',a)
print('b: ',b)
print('c:',c)
print(a is c)

# 시험 범위 챕터6 까지 + git(ppt에 있는거)
