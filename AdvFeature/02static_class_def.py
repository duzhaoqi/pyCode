
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
