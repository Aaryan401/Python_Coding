print('''
+ for Add
- for subtract
* for multiply
/ for divide
% for remainder
** for finding exponent
''')



num1=eval(input("Enter the value "))
num2=eval(input("Enter the value "))
oper=input("Enter the operator ")

if oper=="+":
    print("Addition of",num1,"and",num2,"=",num1+num2)
elif oper=="-":
    print("Subtract of",num1,"and",num2,"=",num1-num2)
elif oper=="*":
    print("Multiply of",num1,"and",num2,"=",num1*num2)
elif oper=="/":
    print("Division of",num1,"and",num2,"=",num1/num2)
elif oper=="%":
    print("Remainder of",num1,"and",num2,"=",num1%num2)
elif oper=="**":
    print("Exponent of",num1,"and",num2,"=",num1**num2)
else:
    print("Wrong operator entered")