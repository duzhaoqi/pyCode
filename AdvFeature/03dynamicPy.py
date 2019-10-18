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


