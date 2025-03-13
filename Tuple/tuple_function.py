t1=(100,852,963,741,5210,852,8521,687743,7866)
print(t1)

#min() use to find the minimum value in tuple
print(min(t1))

#max() use to find the maximum value in tuple
print(max(t1))

#count() use count the no. of occurence of the given data in the tuple
print(t1.count(852))

#index() use to print the index of the given data
print(t1.index(852))

#sum() use to sum all of the data present in tuple
#It only work when tuple have only on no. or floating no.
print(sum(t1))

print(sum(t1,100))#We can also give the default value to add with the sum of the tuple