import types
"""
python的动态处理
1.动态添加实例属性
2.动态添加类属性


"""


class Persion(object):

    """
        用于限制实例可以存在或者动态添加的属性,
        除此之外,无法添加其他属性(不限制类属性)
    """
    __slots__ = ("_hp","mp")
    def __init__(self,hp) -> None:
        self._hp = hp

    def show_info(self):
        print(self._hp)


du = Persion(32)
du.show_info()

#通过类名,动态的添加类属性
Persion.name = "DuZhaoqi"

print(du.name,Persion.name)

#通过实例,动态添加实例属性
du.mp = 100
print(du.mp)

#===================================================
"""
动态添加实例方法
"""

class Dog(object):
    """这是为测试添加类方法而添加的"""
    def __init__(self,name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name

er = Dog("Husky")

print(er.name)

def set_name(self,d_name):
    self._name = d_name

#动态添加实例方法需要使用types模块
er.set_name = types.MethodType(set_name,er)
er.set_name("TOM")

print(er.name)

#==========================================================
#动态添加类方法

@classmethod
def get_cls_info(cls):
    return cls.__doc__

Dog.get_cls_info = get_cls_info

info = Dog.get_cls_info()
print(info)

info2 = er.get_cls_info()
print(info2)


#============================================================

"""动态添加静态方法"""

@staticmethod
def dog_info():
    print("This is a class of dog;")

Dog.dog_info = dog_info

#类访问静态方法
Dog.dog_info()

#实例访问方法
er.dog_info()