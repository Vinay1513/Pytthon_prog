
#WAP that print all positive numbers form a given range

a=int(input("Enter first number"))
b=int(input("ENter second number"))


for i in range(a,b):
    if(i>0):
        print(i,end=" ")
