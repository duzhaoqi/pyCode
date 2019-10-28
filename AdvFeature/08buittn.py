from  collections.abc import Iterator
from functools import reduce

def fun(x):
    return x ** x


s1 = map(fun,[1,2,3,4,5])
print(isinstance(s1,Iterator))

for i in s1:
    print(i)


def f(x):
    return x > 0

s2 = filter(f,[7,6,-5,-9,-10,3,0])
print(type(s2),s2)

def fadd(x,y):
    return x + y

s3 = reduce(fadd,[1,2,3,4,5,6,7,8,9])
print(s3)