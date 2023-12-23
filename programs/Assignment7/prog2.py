
#2 WAP to calculate the sum of the first 10 even numbers

n=int(input("Enter a number"))
i=0
tot=0
while(i<=n+1):
    if(i%2==0):
        tot=tot+i
    i=i+1
print("Sum of first 10 even number is",tot)




