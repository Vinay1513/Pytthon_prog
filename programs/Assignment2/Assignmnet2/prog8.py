
#Take single character from user if the ascii value of character is even then print character

string=input("Enter a character")

x=ord(string)

if(x%2==0):
    print(string)
else:
    print("No output")

