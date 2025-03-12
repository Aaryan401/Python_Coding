range(5) #Range is a function that use to itterate
#range(5) mns it
#starts from 0
#condition<5
#increment 1

range(1,6)
#here we can give the starting and condition within range fn.
#starts from 1
#condition < 6
#increment 1

range(1,6,2)
#here range(start,condition,increment) we have given alll the value then the range fn. can run through this

for n in range(5):
    print(n)
print()
for n1 in range(1,5):
    print(n1)
print()
for n2 in range(1,5,2):
    print(n2)

#Print table of 18

for table in range(1,11):
    print("18 *",table,"=",table*18)