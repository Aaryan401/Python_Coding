string="my nAmE is Aaryan prashar"

print(string.lower())#lower() makes whole string lower
print(string.capitalize())#Capitalize() makes the first letter of the first word capital after that alll the letter is in small
print(string.title())#title() makes first word capital of each word
print(string.upper())#upper() makes whole string in upper case

print(string.find("A"))#It return the index no of the first occurence of data

print(string.find("A",6))#Here we define the start position where find() starts searching

print(string.find("z"))#If the given data is not present in the string then find return -1

print(string.index("a"))#It gives the index of the data
#print(string.index("z")) If the given data is not present in the string then index gives error
#This is the difference between find() and index() that if the data is not present then find() return -1 but index() gives error


print(string.isalpha())#It check that the string contains only alphabet if it contains only alphabet then it return true otherwise false
print(string.isdigit())#It check that the string contains only digit if it contains only digit then it return true otherwise false
print(string.isalnum())#It check that the string contains both alphabet and digit if it contains alphabet and digit then it return true otherwise false
#If space is present then also it return false because space is also a character that is neither alphabet nor digit. It is a special character


x=65
print(chr(x))#chr() convert the ascii value into character and return the crossponding character
print(chr(500))

x="a"
print(ord(x))#ord() convert the character and gives it's ascii value
print(ord("^"))

#format() used to insert anything  between the string
#format() format the specific value and insert them inside the string's placeholder.
#Placeholder is defined using curly brackets{} and the data is stored in runtime.

print("Welcome {} Banglore".format("to"))

print("{0}, Welcome {1} Banglore".format("HI","to"))

print("welcome {b} {a}".format(a="banglore",b="to"))

#IN formatting we can also specify the length of the string
# < It means it can take the specified space from left side
# > It means it can takes the space from the right side
# ^ It means it can takes equal space from both side's

print("{c:<10}welcome {b:>10} {a} {d:^10}{e}".format(a="banglore",b="to",d="OK",c="Hi",e="Bye"))
