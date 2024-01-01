#4:count the even digits of the given number

count=0
n=int(input("Enter a number"))
while(n>0):
    n=n//10
    if(n%2==0):
        count+=1
print(count)
