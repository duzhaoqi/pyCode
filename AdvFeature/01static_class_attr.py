"""
类与对象区别
类实例与对象实例区别
"""
class AI(object):
    """
    AI父类
    """
    # AI有是否存活类属性
    isAlive = False
    def __init__(self, _hp, _mp):
        # AI 有血量和魔法值实例属性
        self.hp = _hp
        self.mp = _mp


if __name__ == "__main__":
    # 实例a1、a2中hp、mp属性不同
    a1 = AI(100, 50)
    a2 = AI(60, 120)

    print(a1.mp, a2.mp)
    print(a1.isAlive, a2.isAlive)

    # 实例可以调类属性
    print(AI.isAlive)
    # 类名不可以调实例属性错误
    #print(AI.mp)