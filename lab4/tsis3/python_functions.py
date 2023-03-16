#1
ounces = int(input("How many ounces you need to convert into grams? "))
def oz_to_gr(x):
    return(x*28.3495231)
print(ounces, " ounces is ", oz_to_gr(ounces), " grams")

#2
farenheit = int(input("enter Farenheit value: "))
def f_to_c(x):
    x=(5 / 9) * (farenheit-32)
    return(x)
print(f_to_c(farenheit))

#3
numheads=int(input("num of heads: "))
numlegs=int(input("num of legs: "))
total=numlegs+numheads
def solve(numheads, numlegs):
    if numlegs-(numheads*2)>0:
        numlegs = numlegs-(2*numheads)
    rabbits = numlegs/2
    chicken=numheads-rabbits
    print("rabbits: ", int(rabbits),", chicken: ", int(chicken))
solve(numheads, numlegs)

#4
def filter_prime():
    def prime(x):
        if x<=1:
            return False
        for i in range(2, x):
            if x%i==0:
                return False
        return True

    nums=input("enter list: ").split()
    nums = list(map (int, nums))
    primes = list(filter(prime, nums))
    return primes
primes=filter_prime()
print(primes)

#5
from itertools import permutations

s = input("enter : ")
def strpermutations(s):
    str = permutations(s)
    for perm in str:
        print(''.join(perm))
strpermutations(s)

#6
s = input("enter str: ").split()
# split()
def reverse(str):
    s.reverse()
    print(' '.join(s))
reverse(s)

#7
num_list = list(map(int, input("enter list : ").split()))
def has33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
print(has33(num_list))

#9 - volume of sphere
#import math
radius=int(input("enter radius: "))
def volume(radius):
    rad_sq=pow(radius, 3)
    pi=3.14159
    vol=(4/3)*pi*rad_sq
    print(vol)
volume(radius)

#10 - unique elements in new list
elems=list(map(int, input("enter list: ").split()))
def unique(elems):
    unique_elems=[]
    for x in elems:
        if x not in unique_elems:
            unique_elems.append(x)
    print(unique_elems)
unique(elems)

#11 - palindrom
str=input("enter str: ")
def palindrom(str):
    str=str.lower().replace(' ','')
    strrev=str[::-1]
    if strrev==str:
        return True
    return Falce

#12
nums=list(map(int, input("enter list: ").split()))
def histogram(nums):
    for num in nums:
        print('*'*num)
histogram(nums)

#13 guess the num
import random

random_num=random.randint(1, 20)

name=input("hello whats your name: ")
num=int(input("hello, " + name + ". enter number from 1 to 20: "))

def guessing(num):
    while num!=random_num:
        if num < random_num:
            print("too low")
            num = int(input("new num: "))
        elif num > random_num:
            print("too high")
            num = int(input("new num: "))
    num= print("good!")
guessing(num)
