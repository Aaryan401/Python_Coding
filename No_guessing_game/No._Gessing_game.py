import random
x=int(input("Enter a no. b/w 1-100"))
y=random.randint(1,100)

if x>y:
    print("U'r guess no is greater ")
    print("Computer no",y)

elif x<y:
    print("U'r guess no is smaller no.")
    print("Computer no",y)

else:
    print("U'r guess no. is equal")
    print("Computer no",y)