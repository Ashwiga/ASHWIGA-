n=int(input("enter the elements of the list:"))
num[]
for i in range(n):
    x=int(input())
    num.append(x)
print("list=",num)
a=int(input("enter the element to find="))
def index(num,a):
    pindex=[]
    nindex=[]
    ncount=0
    c=len(num)
for i in range(0,c):
    if num[i]==a:
        pindex.append(i)
        nindex.append(-c+i)
        ncount=ncount+1
    return(pindex,nindex,ncount)
print(index(num,a))

