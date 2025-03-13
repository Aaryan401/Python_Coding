#tuple can be created using parenthesis i.e.()
#It's data can be seperated using comma
#It is immutable in nature i.e. ONce tuple is created it's data cannot be modified after that
#Beacuse of this Insert and delete fn. can't be done on tuple
#It is ordered collection so we can done indexing
#It's index start's from 0

#If we write a single value in the parenthesis then it's not a tuple
#i.e. t1=(5) This is not a tuple


t=(1,2,3,4,5)
print(t)

#Iterate using loop on tuple
for a in range(len(t)):
    print(t[a])

print()

for a in t:
    print(a)