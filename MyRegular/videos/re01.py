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
restr = "hello02gtglkdshello02rfgthello02tg43"

def my_re(pattern,restr):
    #re_get = re.match(pattern,restr)
    #re_get = re.search(pattern, restr)
    #re_get = re.findall(pattern, restr)
    re_get = re.sub(pattern,"MM",restr,1)
    re_get = re.finditer() ##返回迭代器,每一个元素都是match对象
    #x = re_get.group()
    print(re_get)
    #print(x)

my_re(pattern,restr)
