#!/usr/bin/python3
import sys

#普通函数
def feibonaci(n):
    a, b, counter = 0, 1, 0
    while (counter < n):
        yield a
        a, b = b, a+b
        counter += 1

#带默认参数的函数
def printme(x, y = 3):
    print(x,y)
    return x+y

#匿名函数
sum = lambda arg1, arg2: arg1+arg2

#参数不定函数，以元组形式传入
def printinfo(x, *argv):
    print(x)
    print(argv)

#参数不定函数，以字典形式传入
def printinfodict(x, **argv):
    print(x)
    print(argv)

f = feibonaci(10)

printme(y=1, x=2)
print(printme(2))
printinfo(1,2,3)
printinfodict(1,a=2, b=3)
print(sum(9, 10))

while True:
    try:
        print(next(f), end = " ")
    except StopAsyncIteration:
        sys.exit()
