''''#List can be created using[]
a=[1,2,4,5,6]


#print the list using print() function
print(a)

#Access using index using a[0],a[1],a[2]
print(a[2])

#we can assign new value using '=' operator
a[2]=70
print(a[2])
print(a)

'''
#In one List we store different datatype values

Differlistvalues=[10,"Ram",'Rohan',50,True]

"""print(Differlistvalues)
print(Differlistvalues[3])
"""

'''LIst Slicing
Slicing:-Slicing is used to get a certain part of the string 

'''
friends=[22,"Ram","Rohan","Mohan","Ravi",98]
print(friends[1:6:2])
print(friends[:4])#(if we can't give the index no of starting value it starts from 0th index)
print(friends[0:-5])#(if we can't give the index no of end value then it automatically take the last index no)
print(friends[:]) #(if we can't give the start or end index no then it automatically take the first and last index no)
print(friends[::2])


