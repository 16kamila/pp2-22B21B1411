#1
num=int(input("n: "))
def sq(n):
    for i in range(n):
        yield i**2
print(*sq(num))

#2 even numbers
def even(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

num=int(input("n: "))
print(*even(num), sep=",")

#3
num=int(input("n: "))
def f(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
print(*f(num))

#4
a=int(input("a: "))
b=int(input("b: "))
def sq(a, b):
    for i in range(a, b+1):
        yield i**2

print(*sq(a,b))

#5
num=int(input("n: "))
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
print(*countdown(num))
