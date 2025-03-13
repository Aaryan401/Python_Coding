l=[1,5,6,7,8,9]
s=set(l)#set() use to convert any types of collection into set
print(s)

#add() use to add the data in the set
s.add(4)
print(s)

#pop() use to remove the data from the set
print(s.pop())#It randomly delete any data from the set
print(s)

#remove()  use to remove the data from the set
s.remove(9)#It works on value
print(s)

#clear() use to clear all the data that is present in the set
s.clear()
print(s)#After clear the whole set This doesn't give {} it give set() as an output


#update() use to update the data in the set
l1=[2,9,10,15,7,1]
s.update(l1)
print(s)

#It use to remove the data
s.discard(1)
print(s)