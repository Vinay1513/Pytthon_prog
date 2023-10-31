
#WAP to print all te character values of the given  ASCII value range from the user

x=int(input("Enter the start of range : "))
y=int(input("Enter end of range :"))

if(x<0)or(y<0):
    print("Wrong input")

else:

    for i in range(x,y):

        print("The chracter of ASCII value",i,"is ",chr(i))

