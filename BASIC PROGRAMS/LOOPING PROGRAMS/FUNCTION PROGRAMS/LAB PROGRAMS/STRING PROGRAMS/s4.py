
def reverse(s):
    if len(s)%5 == 0:
        
        return reverse(s[1:]) + s[0]
 
 
s = "kpr institute of engineering and technology"

 
print("The original string is : ", end="")
print(s)
 
print("The reversed string(using recursion) is : ", end="")
print(reverse(s))
print(s.capitalize())