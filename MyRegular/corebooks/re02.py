import re

# (?:…)符号将更流行；通过使用该符号，可以对部分正则表达式进行分组，但是并不会保
# 存该分组用于后续的检索或者应用。当不想保存今后永远不会使用的多余匹配时，这个符号
# 就非常有用
# 忽略分组内匹配的值

r1 = re.findall(r'http://(?:\w+\.)*(\w+\.com)','http://google.com http://www.google.com http://code.google.com')
r2 = re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})','(800) 555-1212').groupdict()
print(r1)
print(r2)


# ?P 标记分组内的正则匹配的值
# ?= 引用之前?P标记的值

x1 = bool(re.match(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number) 1(?P=areacode)(?P=prefix)(?P=number)','(800) 555-1212 800-555-1212 18005551212'))
x2 = bool(re.match(r'''(?x)
    # match (800) 555-1212, save areacode, prefix, no.
    \((?P<areacode>\d{3})\)[ ](?P<prefix>\d{3})-(?P<number>\d{4})
    
     # space
     [ ]
    
     # match 800-555-1212
     (?P=areacode)-(?P=prefix)-(?P=number)
    
    # space
     [ ]
    
    # match 18005551212
    1(?P=areacode)(?P=prefix)(?P=number)''', '(800) 555-1212 800-555-1212 18005551212'))

print(x1,x2)

