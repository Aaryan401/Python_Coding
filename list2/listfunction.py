l=[20,30,50,60]
print(l)

#These fn remove the data using the index
del l[1]#del removes the data of that index but doesnot return deleted data
print(l)

l.pop(2)#pop() remove the  data from that index and returns the deleted data
print(l)

#These remove the data a/c to the given data
l.remove(20)
print(l)

#To remove all the data on the list
l.clear()
print(l)

l=[20,30,50,60]
print(l)
#Update the list element
l[0]=10#This will update the list data on that index
print(l)

#To insert any data in any index we have
#insert,append,extend

#Count() use to count the no of occurence of any data
l=[10,20,10,50,60,80,80,10,60,40]
print(l.count(10))

#max() use to find the greatest value among the list
print(max(l))

#min() use to find the smallest value among the list
print(min(l))

#sort() use to find the no in ascending order
l.sort()
print(l)
#if we wanna sort into descending order
l.sort(reverse=True)
print(l)
#Reverse() can use to reverse the list
l.reverse()
print(l)

print(l.index(10))#Using index() we can get the index of any data.It return the 1st occrence of that data
