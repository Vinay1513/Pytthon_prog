#4 WAP to calculate he factorial of a given number.

n=int(input("Enter a number"))
fact=1
while(n>=1):
    fact*=n
    n=n-1
print("Factorial of 5 is",fact)
