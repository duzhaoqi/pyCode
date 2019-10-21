
ls01 = [x for x in range(100000)]

print(ls01.__sizeof__())

#生成器
ls02 = (x for x in range(100000))
print(ls02.__sizeof__())
print(ls02)
#生成器不能使用下标进行访问
#print(ls02[100])


def fun():
    yield 10
    yield 20
    yield 30
    return "Hello World"

result = fun()

# for i in result:
#     print(i)
print(next(result))
print(next(result))
print(next(result))
try:
    print(next(result))
except StopIteration as e:
    print(e)



def fib(times):
    n  = 0
    a, b = 0, 1
    yield a
    yield b

    while n < times:
        n += 1
        a, b = b, a+b
        yield b

for i in fib(5):
    print(i)