
rev=0
n=int(input("enter a number"))
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("Reverse number is ",rev)
