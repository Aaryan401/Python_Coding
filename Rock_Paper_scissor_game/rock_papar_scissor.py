import random
print("Welcome to Rock,Paper,scissor game")
while True:
    c=input('''
        Press 1 to play
        Press 2 to exit 
    ''')
    if c=='1':
        l=["rock","paper","scissor"]
        y=random.choice(l)
        x=input('''Please select any one option
            Press 1 for rock
            Press 2 for scissor
            Press 3 for Paper
        ''')
        if x=='1':
            if y == "paper":
                print("Computer select",y)
                print("u win")
            else:
                print("Computer select", y)
                print("Computer win")

        elif x=='2':
            if y=="rock":
                print("Computer select", y)
                print("U win")
            else:
                print("Computer select", y)
                print("Computer win")
        elif x=='3':
            if y=="scissor":
                print("Computer select", y)
                print("U win")
            else:
                print("Computer select", y)
                print("Computer win")
        else:
            print("This option is not avaliable")
    elif c=='2':
        break

    else:
        print("What do u want??")
        print("Please enter a correct option")
