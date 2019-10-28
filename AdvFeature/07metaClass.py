
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

#==============================

def move(self):
    print("Move")

AI = type("AI",(object,),{"move":move})

#查询类内部的属性和方法(列表形式)
print(dir(AI))
#字典形式查询类内部的属性和方法(或者使用 dict() )
print(AI.__dict__)

"""
Python在创建NPC类时先不在内存中创建、首先查看NPC中有__metaclass__这个属性吗
如果有，Python会通过__metaclass__创建一个名字为NPC的类(对象)
如果Python没有找到__metaclass__，它会继续在AI（父类）中寻找__metaclass__属性，并尝试做和前面同样的操作。
如果Python在任何父类中都找不到__metaclass__，它就会在模块层次中去寻找__metaclass__，并尝试做同样的操作。
如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象
"""

#利用元类创建新类
## 要求: 属性名为 小写类名+小写属性名

#创建 类创建函数
def designClass(currentclass,parentclassname,attrdict):
    newAttrDict = {}
    for  k, v in attrdict.items():
        if not k.startswith("__"):
            newAttrDict[currentclass.lower()+k.lower()] = v

    return  type(currentclass,(),newAttrDict)

class NPC(metaclass=designClass): #使用metaclass创建类
    speed = 10
    name = "Du"


print(hasattr(NPC,"speed")) #NPC类中不存在speed属性
print(hasattr(NPC,'npcspeed')) #NPC类中存在npcspeed属性