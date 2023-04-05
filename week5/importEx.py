#import random #import 모듈명
'''
from random import randint

print(randint(0,10000000))
for i in range(7):
    print(randint(1,45), end=' ')
'''
#놀이동산 놀이기구 탑승 문제
#총 정원 4명
#정원이 차면, 놀이기구 시작
#조건 : 키150이상
#사람들한테 키를 물어보고 탑승
#150이상 4명이 되면 놀이기구 시작
count = 0
while True:
    height = 0
    height = int(input('키를 입력하세요 >> '))
    if height > 150:
        count +=1
        print('1명 탑승, 현재 인원: ',count)
    else:
        print('키 150이하는 탑승할수 없습니다.')
    if count == 4:
        print('놀이기구 시작 !!')
        break
