
"""
元类
，使用type创建Persion类
"""

#创建类对象
Ps = type("Persion",(object,),{"name":"du","age":25})

#创建对象
p1 = Ps()
print(p1.__class__)
print(Ps.__class__) #都是查看对象所在的类(在python中，类 也是对象)

Stu = type("Student",(Ps,),{"Stunum":1001})

print(Stu.__name__) #查看对应的名字
print(Stu.__class__)

#查看父类对象
print(Stu.__bases__)
print(Ps.__bases__)

print("+="*20)
#------------------------------------

@classmethod
def sleep(cls):
    print(cls)

@staticmethod
def eat():
    print("I am eating something!!")

def study(self):
    print("I love Learning")

Human = type("Human",(object,),{"sleep":sleep,"eat":eat,"study":study})

du = Human()
du.study()
Human.eat()
Human.sleep()

print("+="* 20)

