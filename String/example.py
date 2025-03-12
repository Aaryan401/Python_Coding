#We can write string in either single qoute ' ' or double quote " " or triple quote ''' '''
#String is Immutable data type
#It is a collection of one or more character
#It is a ordered sequence
s="Hello@123"
print(s,type(s))#type fn. can return the datatype of the variable

s='''
        Hello
        MY Name is Aaryan
'''

print(s,type(s))#If we write anythng in triple quote then it will print same way as we have written
#Triple quote can be used to represent multiline strings

"""Index of string
positive index starts from 0 i.e. 0,1,2,3,4,
negative index starts from -1 i.e. -1,-2,-3,-4,-5
"""

w="My Name is Aaryan"
#String Indexing
print(w[5])#with the help of index no we can get the value that present on given index
print(w[-9])#we can also use negative index to search the required data from the index

#String Slicing
print(w[0:5:])#Here it starts from 0 an goes to index no. 4 with the increment of 1
print(w[11:])#Here it starts from index no 11 and goes to last

#Reverse a string using slicing
string="My Name is Aaryan Prashar"
print(string[-1::-1])#Here it starts from -1 i.e. r and goes to the first data with the decrement of -1
