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