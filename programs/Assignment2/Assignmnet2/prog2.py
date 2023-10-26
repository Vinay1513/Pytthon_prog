
#WAP to determine whether entered angle is right angle or not

Input1=int(input("Enter first angle"))

print("angle1= ",Input1)
Input2=int(input("Enter second angle"))
print("angle2= ",Input2)
Input3=int(input("Enter third angle"))
print("angle3= ",Input3)

if(Input1==90)and(Input2==90)and(Input3==90):
    print("It is a right-angle triangle")

else:
    print("It is not a right-angle triangle")
