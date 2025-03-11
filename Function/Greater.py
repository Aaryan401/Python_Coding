def greater(a,b,c):
    if a>b:
        if a>c:
            print("a is greatest")
        else:
            print("c is Greatest") 
    else:
        if b>c:
            print("b is greatest")
        else:
            print("c is greatest") 
            
a=(int(input("Enter 1st no")))
b=(int(input("Enter 2nd no"))) 
c=(int(input("Enter 3rd no")))  
greater(a,b,c)        