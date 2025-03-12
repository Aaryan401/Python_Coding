String="Uttaranchal University"
print(String)
print(len(String))#len() is used to give the length of string so that we can perform our task onto string

for n in range(0,len(String)):
    print(String[n])#To pring each letter of the string
print()

#Reverse of string using loop
for n in range(len(String)-1,-1,-1):
    print(String[n])