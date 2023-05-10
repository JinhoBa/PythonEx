# 0510

import random
print('random number : ',random.randint(10,100))

import math as m
print(m.fsum([1,1,1,1,1,1]))

n = m.pow(random.randint(1,100),3)
print(n)

from math import pow as p
# from math import pow,fsum 가능
p(10,3)

# 모듈을 만들어 사용가능
# helloya 호출시 ya파일 실행
# python 파일만 import 가능

import module_y.AI.ya as selected # from moudule_y.AI import ya as selected
selected.hello10()

print(__name__)
# __name__ 해당 파일에서 실행할때 return __main__

