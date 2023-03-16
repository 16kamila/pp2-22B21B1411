import functools
import re
import time
import math
import datetime
now=datetime.datetime.now()

#1
nums=[2,10,50]
def mult():
    a=1
    for i in nums:
        a=a*i
    return a
print(mult(nums))

#2
str=input("str: ")
upper=0
lower=0
def idk(lower, upper):
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            lower += 1
        else:
            upper += 1
    print(upper, " ", lower)
(idk(lower,upper))

#3
str=input("")
def palindrom(str):
    s=str[::-1]
    if str==s:
        return("palindrom")
    else:
        return("not palindrom")
print(palindrom(str))

#4
n=int(input("num:"))
ms=int(input("miliseconds: "))
def sqrt(n,ms):
    time.sleep(ms/1000)
    print("Square root of ",n," after",ms," milliseconds is", math.sqrt(n))
    # print(time.time())
sqrt(n,ms)

#5
t=(1,2,3,4,5)
def tupl(tuple):
    x=all(tuple)
    return x
print(tupl(t))

#6
