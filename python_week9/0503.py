# 0503 
# 함수  

def addthree(temp, temp2):
    return temp + temp2

for i in range(10):
    print(addthree(i, i**2))

def print_hello():
    print('hello')

def printaddthree(num):
    print(num+3)

printaddthree(100) # 호출은 정의 이후에


# 사람이름 2개 입력받고 '안녕 사람1, 안녕 사람2'출력
def hi(p1="배진호", p2="주재석"): # 기본값 설정 가능
    print('hi ',p1)
    print('hi ', p2)
hi()
    
# 숫자 두개 입력받아서 합리턴
def addnum(n1,n2):
    return n1 + n2
print(addnum(16485,3216854))

def mysum(*numbers): # 인자의 개수를 모를때, 배열에서도 사용
    result = 0
    for num in numbers:
        result += num
    return result

print(mysum(1,2,3,4,5,56,7))
lst1 = [11,111,1,1,1,1,1,1,1,11,1,11,1,1,1,1,1]
lst2 = [2,3,4,5,5,3,3,3,23,2,2,2,2,2]
print(mysum(*lst1,*lst2))

def cafe(**keyvalue):
    for key in keyvalue:
        print(key,"", keyvalue[key])

cafe(아메=2000, 라떼=3000, 핫초코=5000)
print('--------------')
cafe(아메=2000, 라떼=3000)
print('--------------')
cafe(아메=2000)

menu = {'아메':2000, '라떼':3000, '핫초코':5000}
cafe(**menu)

# Lambda funtion---------------------------------------------------------------------------------
# 간결함, 함수이름 짓기 싫어서, 수행문이 한줄

def addthree(num):
    return num + 3
print(addthree(100))

print((lambda num : num + 3)(100))

# 숫자를 입력받아서, 10을 곱해서 return lambda
print((lambda num : num *10)(100))


# 숫자를 두개 입력, 두개를 곱해서 return lambda
print((lambda num1, num2 : num1*num2)(100,200))

# map------------------------------------------------------------------------
# map(funtion,[1,2,3,4,5])

print(list(map(addthree,[10,20,30,40,50])))

print(list(map(lambda x : x + 3, [10,20,30,40,50])))

def fi(x):
    return x*5+10 
print(list(map(fi,[1,2,3,4,5,6])))

print(list(map(lambda x : (x*5)+10,[1,2,3,4,5,6])))

ls1 = [10,20,30,40,50]
ls2 = [1,2,3,4,5]

def lstsum(l1, l2):
    return l1+l2
print(list(map(lstsum,ls1,ls2)))
print(list(map(lambda l1, l2 : l1+l2, ls1, ls2)))

# filter 
# 조건을 만족하는가? 만족하면 결과물에 포함, 만족하지 않으면 포함안함
# filter(funtion, list)

def positive(x):
    if x > 0:
        return True
    else:
        return False
def positive(x):
    return x > 0

print(list(filter(positive,[10,-1,30,0,-4,5])))
print(list(filter(lambda x : x > 0 ,[10,-1,30,0,-4,5])))    





