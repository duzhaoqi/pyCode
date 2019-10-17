
"""
类方法: 使用@classmethod修饰,能够访问类的各种内置内容
实例方法: 访问实例属性,所做操作属于该实例
静态方法: 使用@staticmethod进行修饰,一般用于创建的工具类里面,而非作为实例类中

"""
class Ai:
    def __init__(self,speed) -> None:
        self.speed = speed


    """实例方法"""
    def run(self):
        print("My speed is {}".format(self.speed))



class Persion(Ai):
    """这是一个描述机器人的说明"""
    def __init__(self, speed) -> None:
        super().__init__(speed)

    def run(self):
        super().run()

    @staticmethod
    def status():
        print("The persion is dead")

    @classmethod
    def show(cls):
        print(cls.__doc__)


du = Persion(32)
du.run()


#实例,类,都可以访问类方法
du.show()


"""
类与对象区别
类方法 静态方法 实例方法
"""
class AI(object):
    """
    AI类
    """
    def __init__(self, _speed):
        self.speed = _speed
    # 声明类方法run
    def run(self):
        print("run速度为%d" % self.speed)
    # 声明静态方法
    @staticmethod
    def dead():
        print("AI死亡")
    # 声明类方法
    @classmethod
    def printclassinfo(cls):
        print("类文档%s" % cls.__doc__)

if __name__ == "__main__":
    a1 = AI(50)
    a1.run()
    a1.dead()
    a1.printclassinfo()
    AI.dead()


"""
为什么要使用类属性、类方法
为了减少多个类实例所产生的内存空间
类方法与类属性属于类，而不属于某个实例
"""
