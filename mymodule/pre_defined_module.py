import math
import random
import datetime
'''
#***********uses of math module fn's***********************
#ceil() use to give next Integer value
x=eval(input("Enter a no "))
print(math.ceil(x)) #O/P if we give input as 10.3 it gives 11 as output

#fabs() use to give the absolute value i.e. if we give -ve value it return +ve no
x=eval(input("Enter a no "))
print(math.fabs(x)) #O/P if we give input as -10 it gives 10 as output

#factorial() use to give the factorial of any no
#IF we pass 5 Internally it is doing 5*4*3*2*1.JUst we don't need to run loop or do anything this fn. will do all the things internally and give the answer
x=eval(input("Enter a no "))
print(math.factorial(x)) #O/P if we give input as 5 it gives 120 as output

#If we enter float no. then floor() return the Interger value of that no.
x=eval(input("Enter a no "))
print(math.floor(x)) #O/P if i give input as 10.3 it gives 10 as output

#fsum(Iterble) It sum all the data inside any collection and return the answer in float format
l=[]
for n in range(5):
    x=eval(input("Enter a no "))
    l.append(x)
print(math.fsum(l)) 

#sqrt() will give the squareroot of any no
x=eval(input("Enter a no "))
print(math.sqrt(x)) #O/P if i give input as 9 it gives 3 as output


#*****************uses of random module fn's***************
#Random module is use to generate random no.
#No. may b float, int,It can also shuffle the list

#randint() IN randint() we have to pass two value i.e. Value to which we can start and end value where it stops
#returns number b/w start and end.But It include the both the starting no. and ending no.
print(random.randint(5,9))#IT will give any one random no. within the given range

#randrange() we have to pass two value i.e. start and end value
#returns number b/w start and end-1 i.e. It include the only the starting no. and the ending no. will be excluded
print(random.randrange(5,9))#IT will give any one random no. within the given range


#chioce() return any random element from a list
l=["apple",'banana','cherry']
print(random.choice(l))#It will give any one random data from the list

#random() In random module also there is a random()
#That return a random float no. b/w 0 and 1
print(random.random())#give any random float no. b/w 0 and 1

#shuffle() Takes a sequence and return the sequence in a random order
l=[2,9,78,96,75,45,12,16]
random.shuffle(l)
print(l)

#uniform() Returns a random float no. b/w two given parameters
print(random.uniform(1,9))

'''
#******************using datetime module fn.*******************

#datetime.now() in datetime module there is a datetime object.
#in datetime object we have now() it show the current date and time

print(datetime.datetime.now())#It will give current time and date which contains
#year,months,date,hour,minutes,second and milisecond.

#creating date object i.e. we can give any date and it will return in proper format
print(datetime.datetime(2021,5,16))

'''The method is callled strftime() and takes one parameter, format to specift the format to the returned
string:
%b  give Month name in short version     i.e. Mar
%B  give MOnth name in full version     i.e   March
%m  give MOnth as a number               i.e. 12
%y  give Year short version,without century i.e.25
%Y  give Year full version                 i.e. 2018
%H  HOur 00-23 format                       23
%I  Hour 00-12 format                       11
%p  AM/PM                                   PM
 %M Minute 00-59 format                     15
'''
now=datetime.datetime.now()
print(now.strftime("%Y"))#It will return the year