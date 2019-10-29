import os
from multiprocessing import Process

# pid = os.fork()
# print("do")
# if pid == 0:
#     print("child process pid %d" % pid)
# else:
#     print("parent process pid %d" % pid)

# pid = os.fork()
# print("do")
# if pid == 0:
#     # print("child process id %d" % pid)
#     print("current child process pid %d parent pid %d" % (os.getpid(), os.getppid()))
# else:
#     # print("parent process id %d" % pid)
#     print("current parent process pid %d child pid %d" % (os.getpid(), pid))

num = 10

returncode = os.fork()
print(num)
if returncode == 0:
    #child process
    num = 100
else:
    #parent process
    num = 300

if returncode == 0:
    print("child",num)
else:
    print("parent",num)