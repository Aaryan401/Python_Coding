l=[]
while True:
    c=int(input('''Enter 
                1 for Enqueue(Add item)
                2 for Dequeue(Remove item)
                3 for Front(Get front item)
                4 for Rear(Get last item)
                5 Display Queue
                6 for Exit
    '''))
    if c==1:
        n=input("Enter the item")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty Queue")
        else:
            del l[0]
            print(l)

    elif c==3:
        if len(l)==0:
            print("Empty Queue")
        else:
            print(l[0])
    elif c==4:
        if len(l)==0:
            print("Empty Queue")
        else:
            print(l[-1])

    elif c==5:
        print(l)

    elif c==6:
        break

    else:
        print("Invalid Operator")