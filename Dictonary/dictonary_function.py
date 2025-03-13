d={
    'name':'Python',
    'fees':'8k',
    'Duration': '6mnths'
}

print(d.get('name'))#get() use to get any value from the dictonary using key
print(d.get('fees'))
print(d['Duration'])#This is the another way to get the data

#Get all the key with the help of iteration using keys()
for a in d.keys():
    print(a)    #With the help of this we can get all the keys.

#Get all the values with the help of iteration using values()
for a in d.values():
    print(a)    #with the help of this function we can get all the values.

#Get all the items with the help of iteration using items()
for a,b in d.items():
    print(a, b)  #with the help of this fn. we can get all the items i.e.We can get both Keys and values.

#To delete the data in dictonary we have two fn.
#del,pop()
#IN dictonary we can use key's to delete any items because keys are unique
print("delete using del fn")
del d['fees']
print(d)

print("Delete using pop()")
print(d.pop('Duration'))

print(d)

#dict() is used to make a dictonary
d1=dict(name='Java',fees=8000)#we have to pass key's and values in dict()
print(d1)

#update() is used to update the value
d1.update({'fees':100000})
print(d1)


d1.update({'Duration':'3mnths'})#If We wanna we can also update new data
print(d1)


#clear() use to clear the whole dictonary
d.clear()
print(d)

#To add new data in previously defined dictonary
d1['desc']="This is a Java Course" #This will check that the given key exist or not. IF the given key doesn't exist
print(d1)#Then it will make the key and insert the data but if the given key exist then it just update the given value

