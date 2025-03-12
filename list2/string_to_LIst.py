n=input("Enter the value ")
print(n)
print(type(n))

#We can convert any string into list with the help of split()
l=n.split()
print(l)
print(type(l))

#If we wanna to give multipe data then we can use loop
l=[]
for a in range(1,4):
    n=input("Enter the data "+str(a) +":-")
    l.append(n)
print(l)