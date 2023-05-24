# simple interest
def simple_interest(p,r,t):
    print("principal amount is:",p)
    print("rated amount is:",r)
    print("time taken to pay:",t)

    si=(p*r*t)/100
    print("the simple interst is:",si)
    return si
simple_interest(10,5,7)
