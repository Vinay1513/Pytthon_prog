
#Take two character from user if the ascii value of both character are odd the print sum of characters


String1=input("Enter first character")
String2=input("Enter second character")

x=ord(String1)
y=ord(String2)

if(x%2!=0)and(y%2!=0):
    print(x+y)
else:
    print("No output")

