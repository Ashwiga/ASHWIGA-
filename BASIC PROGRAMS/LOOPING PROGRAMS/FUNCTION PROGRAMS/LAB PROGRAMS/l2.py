str1=input("enter the str1=")
str2=input("enter the str2=")
str1=list(str1)
str2=list(str2)
for char in str2:
    if char in str2:
        str1.remove(char)
if len(str1)==0:
    print("no")
else:
    print("yes")
