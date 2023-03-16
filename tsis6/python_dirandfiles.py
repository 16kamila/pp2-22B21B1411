import pathlib
import os
from string import ascii_uppercase
path=r"C:\Users\lenovo\Desktop"

#1
def dirs(p):
    print([x.name for x in os.scandir(path=p) if x.is_dir()])
def files(p):
    print([x.name for x in os.scandir(path=p) if x.is_file()])
def dirsandfiles(p):
    print([x.name for x in os.scandir(path=p)])
dirs(path)
files(path)
dirsandfiles(path)

#2
def check(p):
    exist_status=os.access(path=p, mode=os.F_OK)
    print(f"existance: ",exist_status)
    read_status=os.access(path=p, mode=os.R_OK)
    print(f"readibility: ",read_status)
    write_status=os.access(path=p, mode=os.W_OK)
    print("writability: ",write_status)
    exec_status=os.access(path=p, mode=os.X_OK)
    print(f"executability: ",exec_status)
check(path)

#3
if os.path.exists(path):
    print("filename and directory portion of the given path")
    print(os.path.basename(path))
    print(os.path.dirname(path))
else:
    print("doesnt exist")

#4
file=open(r"C:\Users\lenovo\Documents\tsis6\k_ipalakova.txt")
cnt=0
for lines in file:
    cnt+=1
print("lines:",cnt)

#5
p=open(r"C:\Users\lenovo\Documents\tsis6\k_ipalakova.txt", "a")
a=input("write something: ").split(" ")
for i in a:
    p.write("\n"+i+"\n")

#6
os.chdir(r"C:\Users\lenovo\Documents\tsis6\AZ")
for i in range(26):
    with open(f"{chr(i + 65)}.txt", "w"):
        pass

#7
with open("A.txt","r") as a, open("B.txt","a") as b:
    for line in a:
             b.write(line)

#8
if os.path.exists("toremove.txt"):
    os.remove("toremove.txt")