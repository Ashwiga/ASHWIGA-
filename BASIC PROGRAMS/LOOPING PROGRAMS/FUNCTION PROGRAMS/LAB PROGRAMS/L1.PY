#get the input from the user if the numbers are odd then find the factorial of the number and find the digits of the number using factorialif the number is even then check if the number is palindrome or not


a=int(input("enter the value:"))
if a%2!=0:
    fact=1

    for i in range(1,a+1):
        
        fact=fact*i
    print(fact)
    count=0
    while fact!=0:
        
        r=fact%10
        count=count+1
        fact+fact//10
    print("the number of digits in factorial is:",count)

else:
    
    temp=a
    rev=0
    while(a>0):
        
        
        dig=num%10
        rev=rev*10+dig
        a=a//10
    if temp==rev:
        
        print("palindrome")
    else:
        
        
        print("not an palindrome")
    
