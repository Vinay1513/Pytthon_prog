#5:Count the digits of odd numbers

count=0
n=int(input("Enter a number"))
while(n>0):
    n=n//10
    if(n%2!=0):
        count+=1
print(count)
