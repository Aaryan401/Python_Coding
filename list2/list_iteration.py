#List is mutable in nature
#It can written within [] and data are seprated using ,

list1=[0,1,2,3,4,5]
print(list1[5])

nestedList=[0,1,2,[3,5,6,8]]#This is called nested list i.e. LIst within a list
print(len(nestedList))#It return 4 i.e. 0 is in 0th index,1 is on 1th index 2 is in 2nd index
# And the rest of the data written within a braces are on 3rd index
print(nestedList[3])
#if we wanna nested data then we have to do like this
print(nestedList[3][2])

mixedList=[0,1,2,"Hello",{3,5,6}]
print(mixedList[3].find("l"))#If in list there are String data then We can use string fn on that data
print(mixedList[1::2])#Slicing
#Reverse the list using slicing
print(mixedList[-1::-1])#For itterate the list in decreasing order we have to give the decrement value


#Iteration
l1=[1,2,64,324,887]
for n in range(len(l1)):#Iterate Using range function
    print(l1[n])
print("")
for n in l1:#Without using range fn. here n itterate on the whole list
    print(n)
#But we cannot reverse the list using this if we wanna reverse the list we have to use range()
print("")
#Reverse the list using range()
for n in range(len(l1)-1,-1,-1):
    print(l1[n])


#Zip Function - Iterate Over 2+ Lists at the Same Time
#It will work on the when list have same no element
#If the list don't have same no of element then it ignore the more no element
#Using Zip()
l=[10,20,3,40]
li=[50,60,70,80]
for a,b in zip(l,li):
    print(a,b)
print()
#Using loop and range()
for h in range(len(l)):
    print(l[h],li[h])