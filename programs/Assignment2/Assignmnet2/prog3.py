
#Take two numbers from users and print sum of those numbers is the sum is even

num1=int(input("Enter first number"))
num2=int(input("Enter second number"))

sum=num1+num2
if(sum%2==0):
    print(sum,"is Even")

else:
    print("No output")
