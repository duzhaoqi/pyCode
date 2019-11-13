import re
m = re.match('foo', 'foo') # 模式匹配字符串
if m is not None: # 如果匹配成功，就输出匹配内容
    print(m)
    print(m.group())

m = re.match('foo', 'bar')# 模式并不能匹配字符串
if m is not None: print(m.group())

m = re.match('foo', 'food on the table') # 匹配成功
print(m.group())

m = re.search('foo2', 'seafoo2d') # 使用 search() 代替
if m is not None: print(m.group())