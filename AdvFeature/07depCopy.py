import  copy
ls01 = [1,2,3,4,[5,6,7]]
ls02 = ls01

# "=" 对于列表来说就相当于引用
ls02[2] = 4
print(ls01)
print(ls02)

"""
列表对象自带的copy方法,是一种浅拷贝,不会改变一维数据,但是二维级高维数据已经会被改变
"""
# ls03 = ls01.copy()
ls03 = copy.deepcopy(ls01)
ls03[1] = 99
ls03[4][1] = 33

print(ls01)
print(ls03)


