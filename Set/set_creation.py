#set is unordered datatype
#it is Unindexed i.e. data is not present in the Sequence manner
#It doesn't allow duplicate i.e we can store only unique data in set
#If we store duplicate data it will ignore the 2nd occurence of data
#It is mutable in nature We can insert or delete the data present in the set
# we can't get or change the any data that is present on set
#It written within curly braces{} or by using set() and seperated using comma
#Set and dictonary both written using curly braces
#But the difference is there is key,value pair is present in dictonary
#and in set there is only data is present

s={10,20,30,40,50,10,10,20}
print(s)# This will ignore the duplicate data present in s

#Iterate in set
for a in s:
    print(a)
