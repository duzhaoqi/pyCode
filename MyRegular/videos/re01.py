import re

"""
match: 匹配第一个找到的字符串
search: 扫描全部,并匹配到第一个
fullmatch: 完全配置正则
    以上匹配不到会报错,有group()方法
    
findall: 匹配所有正则,并返回列表
split: 按照正则规则切分,返回列表

sub(rex,要替换的字符,要匹配的字符串,从左到右匹配几个): 使用正则替换字符

finditer: 返回迭代器,每一个元素都是match对象
"""
pattern = "hello02"
restr = "Hello02gtglkdshello02rfgthello02tg43"

def my_re(pattern,restr):
    re_get = re.match(pattern,restr,flags=re.I)
    #re_get = re.search(pattern, restr)
    #re_get = re.findall(pattern, restr)
    #re_get = re.sub(pattern,"MM",restr,1)
    #re_get = re.finditer() ##返回迭代器,每一个元素都是match对象
    x = re_get.group()
    print(re_get)
    print(x)

#my_re(pattern,restr)


# rex = re.compile("hello02")
# x = rex.search(restr)
#
# print(x.group())


test = "gehaosd,ferloqeosdfmleeloveexx"
rex = "(l.{2}e).*(l.{2}e)"
try:
    x = re.search(rex,test)
    print(x.group(2))

    result = re.match(r"(?P<hname>)hello(?P=hname)", "hello world hello china")
    print(result.group(), result.group("hname"))
except Exception:
    print("Error!")