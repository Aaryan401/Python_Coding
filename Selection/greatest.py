a=eval(input("Enter 1st no"))#eval can handle any type of data
b=eval(input("Enter 2nd no"))
c=eval(input("Enter 3rd no"))
if a>b and b>c:
    print(a,"is greatest")
elif b>c:
    print(b,"is greatest")  #In Python elseif is elif
else:
    print(c,"is greatest")
