#importing user defined module
#FOr importing module we have 'import' keyword

import mymodule.user_defined_module as u    #1st way to import any module here also we using alias(as u)
def calculator():
    while True:
        c=input('''Enter 
                + for Addition
                - for Subtraction
                * for Multiplication
                / for Divide
                % for Remainder
                ** for Exponent
                1 for exit
        ''')
        if c!='1':
            x = int(input("Enter 1st no. "))
            y = int(input("Enter 2nd no. "))
        else:
            break

        if c=='+':
            print(u.sum(x,y))

        elif c=='-':
            from mymodule.user_defined_module import substract #2nd way to import module
            #Here we importing 1 function of module but if we wanna importing all the module
            #we can just use import * with the help of this all the module of that fill will be imported
            print(substract(x,y))

        elif c=='*':
            print(u.multiply(x,y))

        elif c=='/':
            if y==0:
                print("Dividing by zero")
            else:
                print(u.divide(x,y))

        elif c=='%':
            print(u.remainder(x,y))

        elif c=='**':
            print(u.exponent(x,y))

        else:
            print("Wrong operator Entered")
            break


#Calling the fn
calculator()

