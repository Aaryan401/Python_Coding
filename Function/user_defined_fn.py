#Function can be created using 'def' keyword

def add():
    a=int(input("Enter 1st no "))
    b=int(input("Enter 2nd no "))
    c=a+b
    print(c)

add()#calling add fn.


#fn. with arguments

def greatest(a,b,c):
    if a>b and a>c:
        print(a,"is greatest")

    elif b>c:
        print(b, "is greatest")

    else:
        print(c,"is greatest")

greatest(9,89,52)


#fn. with return type

def smallest(a,b,c):
    if a<b and a<c:
        return a

    elif b<c:
        return b

    else:
        return c

x=int(input("Enter 1st no. "))#THis is used to take the input from the user
y=int(input("Enter 2nd no. "))#and send as an argument in the fn call
z=int(input("Enter 3rd no "))
print(smallest(x,y,z),"is smallest")#Here fn. is calling and also receving the the value from the return
#And  we can print the value that we get through return
