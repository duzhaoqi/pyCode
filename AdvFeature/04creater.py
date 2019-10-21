
ls01 = [x for x in range(100000)]

print(ls01.__sizeof__())

#生成器
ls02 = (x for x in range(100000))
print(ls02.__sizeof__())
print(ls02)
#生成器不能使用下标进行访问
#print(ls02[100])
