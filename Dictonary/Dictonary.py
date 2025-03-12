#It works on key-value pair
#It written within curly baraces{} sperated with comma
# dictionary is a collection which is ordered, mutable and do not allow duplicates keys but value may be duplicate.
#keys can’t be repeated and must be immutable.
#Dictionary keys are case sensitive
#Keys must be unique
#In Python 3.7, dictionaries are ordered. Before that dictionaries are unordered
d={
    'name':'Python',
    'fees': 80000,
    'duration': '2 mnths'
}
print(d) #Print the whole dictonary
print(d['fees'])#To Print the specific key data

print()
#Also by Using loop we can iterate to all the values
for a in d:
    print(d[a])