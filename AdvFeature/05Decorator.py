import  time

def dd_time(func):
    def add_time(*args,**kwargs):
        print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
        func(*args,**kwargs)

    return add_time

@dd_time
def get_info(name,**kwargs):
    print("{}独自去上班了".format(name))


get_info("小明")



#=====================================

def login(func):
    def user_login():
        username = input("username: ")
        if username == "duzhaoqi":
            func()
        else:
            print("登录失败")
    return user_login


@login
def showlist():
    print("您的订单有:")
    for i in range(1,11):
        print("订单:{}".format(str(i)))

def showmoney():
    print("您的余额还有{}$".format(10000))

def showdiscount():
    print("你又优惠券100,200,300,500")




showlist()





