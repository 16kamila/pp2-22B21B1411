import re
str=input("")

#1
res= re.fullmatch("ab*", str)

#2
res = re.fullmatch("ab{2, 3}", str)

#3
res = re.findall("[a-z]+(_[a-z]+)*", str)

#4
res = re.findall("[A-Z][a-z]*", str)
print(res)

#5
match = re.fullmatch("a.*b$", str)

#6
replace=re.sub("[ ,.]", ":", str)
print(str)

#7
convert=re.sub("_(.)", lambda x: x.group(1).upper(),str)

#8
slpit=re.findall("[a-zA-Z][^A-Z]*",str)

#9
spaces =re.sub("(?<!^)(?=[A-Z])", " ",str)

#10
convert =re.sub("([a-z])([A-Z])", r'\1_\2',str).lower()

