# 기말 정리

# dictionary
# 인덱스가 아니라 키값을 이용

carDict = {'h101':('2020','1600'), 'h102':('1568','5268'),
           'b102':('8745','9456'),'b105':('6666','5784')}

print(carDict.keys())
print(carDict.values())
print(carDict.items())


#h101 ('2020', '1600')
#h102 ('1568', '5268')
#b102 ('8745', '9456')
#b105 ('6666', '5784') 출력

for key in carDict:
    print(f'{key} {carDict[key]}')
for item in carDict.items():
    print(item[0],item[1])

# yearList = [2020, 1568, 8745, 6666]
yearList =[]

for values in carDict.values():
    yearList.append(int(values[0]))
    
print(yearList)
# 몇대인지
year = int(input('생산년도를 입력하세요 >> '))
print( f'{year}년도에 생산된 자동차는 {yearList.count(year)}대 입니다.') 
# for문 사용
count=0
for prod_year in yearList:
    if prod_year == year:
        count+=1

print(f'{count}대 입니다.')

members = {'홍':'1','박':'2','정':'3'}
members['최'] = '5'
members.update({'강':'6'})
members['김']='777'
members.update({'최':'8'})
print(members)

#zip 에 가고싶다.
# list, tuple, string을 합쳐주는것

L1 = [1,2,3,4,5]
L2 = ['a','b','c','d','e']
print(list(zip(L1,L2)))

sport=['축구','야구','농구','배구']
num = [11,9,5,6]
sports = dict(zip(sport,num))
while True:
    name = input('운동종목을 입력하세요>>')
    if name in sports:
        print(sports[name])
    elif name == 'quit':
        print('종료...')
        break
    else:
        print('몰라요')
        continue


# filter, map, lamda
def positive1(x):
    return x>0
list1 = [1,2,3,-5,8,-3,5]
print(list(map(lambda x : x*-1,list1)))
print(list(filter(lambda x : x>3,list1)))


list2 = [2,4,6,8]
list3 = [1,3,5,7]
def sum(x,y):
    return x+y

sum_list1 = list(map(sum,list2,list3))
sum_list = list(map(lambda x,y : x+y,list2,list3))
print(sum_list1)
print(sum_list)

import random
from random import randint as rn

# __name__ 시험에 나옴 
# 프로그램이 처음 시작된 소스에서는 __main__으로 저장되며,
# 불러온 다른 모듈에는 모듈이름이 저장된다.

