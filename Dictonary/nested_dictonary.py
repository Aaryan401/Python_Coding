#Nested Dictonary means putting a dictonary inside another dictonary
#It's a collection of dictonary into one single dictonary


course={
    'php':{'fees':'8k','duration':'3mnths'},
    'Java':{'fees':'10k','duration':'6mnths'},
    'Python':{'fees':'9k','duration':'5mnths'}
}
#Fetch the data of dictonary
print(course)

print(course['php'])
print(course['Java']['fees'])#Get specific data from the nested dictonary

#Iterate on nested dictonary
for a,b in course.items():
   # print(a,b) Either like this or like that we can get the data of nested dictonary
    print(a,b['fees'],b['duration'])