import csv
import yaml
import sys
import hello_world
class MyFirstClass:
    o_string_r = r"""The first try
                of the Class of Python's \n script"""
    o_string = """The first try
            of the Class of Python's \n script"""
    print(o_string_r)
    print(o_string)
    r=3.14159
    i=-1.7

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def f(self):
        return "hello World"

x = MyFirstClass(3.1415926, -0.3333)
print("Debug1: ", x.f())
print("Debug2: ", x.f)
print("Debug3:", x.r, x.i)
class MySecondClass(MyFirstClass):
    list=[1,2,3,4]
    it = iter(list)
    def f(self):
        return "hello China"

class AClass:
    def A_f(self):
        return "hello A"
class BClass:
    def B_f(self):
        return "hello B"
x = MySecondClass(250.0,-350.0)
print("Debug1: ", x.f())
print("Debug2: ", x.f)
print("Debug3:", x.r, x.i)
from allpairspy import AllPairs
parameters = [
["Brand X", "Brand Y"],
["98", "NT", "2000", "XP"],
["Internal", "Modem"],
["Salaried", "Hourly", "Part-Time", "Contr."],
[6, 10, 15, 30, 60],
]
print("PAIRWISE:")
for i, pairs in enumerate(AllPairs(parameters)):
    print("{:2d}: {}".format(i, pairs))
class MyThirdClass(MySecondClass, MyFirstClass, AClass, BClass):
    def g(self):
        return "hello HuBei"
x = MyThirdClass(250.1,-21)
print("Debug1: ", x.f())
print("Debug2: ", x.f)
print("Debug3:", x.r, x.i)
print("Debug4: ", x.g())
print("Debug5:", x.A_f())
print("Debug6:", x.B_f())
print("Debug7:")
for i in x.it:
    print (i, end=" ")
    print("\nDebug8:")
for i in x.list:
    print (i, end=" ")
it_2 = iter(x.list)
print("\nDebug9:", next(it_2))
while True:
    try:
        print (next(it_2))
    except:
        break
def fibonacci(n):
    a,b,counter = 0,1,0
    while True:
        if (counter > n):
            return
        yield a
        a,b = b,a+b
        counter += 1
f = fibonacci(10)
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        break
x.list.append(5)
x.list.insert(0,0)
print("\n",x.list)
x.list.reverse()
print(x.list)
dir_a = dir(csv)
print("Debug10:", dir_a)
s = "Hello, Wuhan"
print(str(s))
print(repr(s))
print(str(1/7))
print("debug",1/7)
f = open("hello_world.py", "r")
str_s = f.read()
print(str_s)
f.close()
f = open("hello_world.py", "r")
str_s = f.readlines()
print(str_s)
f.close()
f = open("hello_world.py", "r")
str_s = f.readline()
while len(str_s) != 0:
    str_s = f.readline()
    print(str_s)
f.close()
f = open("hello_world.py", "r")
for line in f:
    print(line, end='')
f.close()
#while True:
#    try:
#        x = int(input("Please input a number: "))
#        break
#    except ValueError:
#        print("Your input is not a number, please try again!")
a = 7
try:
    a = 3/0
except:
    print("The operation is not correct")
else:
    print("Debug11:", int(a))
finally:
    print("Debug12:", int(a))
with open("hello_world.py", "r") as f:
    print(f.read())
print(str(f.closed))
import os
os.system('echo Hello GuangGu！')
import glob
glob_s = glob.glob('*.py')
print(glob_s)
print(type(glob_s))
import re
import math
math_s = math.sin(math.pi)
print(math_s)
print(type(math_s))
import random
random_s = random.randrange(1000)
print(random_s)
print(type(random_s))
import smtplib
#server = smtplib.SMTP('localhost')
#server.sendmail('guanfenglin@163.com',
#'Test from python Idle'
#)
#server.quit()
from datetime import date
now = date.today()
print(now)
print(type(now))
from timeit import Timer
import _thread
import time
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
    count += 1
    print ("%s: %s" % ( threadName, time.ctime(time.time())))
#try:
_thread.start_new_thread(print_time, ("Thread-1",2,))
_thread.start_new_thread(print_time, ("Thread-2",3,))
#except:
print ("Error: can not start new thread!")
#else:
print("Thread mark")
#finally:
print("Thread done???")
import threading
exitFlag = 0
class myThread(threading.Thread):
    def init(self, threadID, name, delay):
        threading.Thread.init(self)
        self.threadID = threadID
        self.name     = name
        self.delay    = delay
    def run(self):
        print("start thread: " + self.name)
        print_time(self.name, self.delay, 2)
        print ("Exit from thread" + self.name)

    def print_time(threadName, delay, counter):
        while counter:
            if exitFlag:
                threadName.exit()
            time.sleep(delay)
            print ("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1

#thread1 = myThread(None, 1, "Thread-1", 1)
#thread2 = myThread(None, 2, "Thread-2", 2)
#thread1.start()
#thread2.start()
#thread1.join()
#thread2.join()
print("exit from main thread")
import queue
hash_s = hash('test')
print(hash_s)
print(type(hash_s))