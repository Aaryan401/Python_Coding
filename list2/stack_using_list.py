l=[]
while True:
    c=int(input('''Enter 
                1 for Push ELements
                2 for Pop ELements
                3 for Peek ELements
                4 for Display stack
                5 for Exit
    '''))
    if c==1:
        n=input("Enter the value")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty stack")

        else:
            p=l.pop()
            print(p)
            print(l)

    elif c==3:
        if len(l)==0:
            print("Empty stack")
        else:
            print(l[-1])
    elif c==4:
        print(l)

    elif c==5:
        break

    else:
        print("Invalid Operator")