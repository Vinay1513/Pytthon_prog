
#6.Check number is palindome or not

n=int(input('enter a number'))
temp=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(temp==rev):
    print("number is a Palindrome")
else:
    print("number is not palindrome")
