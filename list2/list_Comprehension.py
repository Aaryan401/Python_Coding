#It is compact and faster
#It ia an elegant way to define and create list based on exixting list

#Syntax
#[expression for items in list]


#This is the nrml way to create the list
l=[]
for a in range(1,101):
    l.append(a)
print(l)

#Using List_COmprehension
n=[m for m in range(1,101)]# here both the variable within [] must be same then the loop will be created
print(n)

n = [m for m in range(1, 101) if m%2==0] #We can also give our custom condition for making list
print(n)


s="hello"
d=[m for m in s]
print(d)