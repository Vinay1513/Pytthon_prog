#8:Check number is perfect or not

sum=0
num=int(input("Enter a number"))
n=1
while(n<num):
    if(num%n==0):
        sum=sum+n
    n+=1
if(sum==num):
    print(num,"is perfect number")
else:
    print(num,"is not a perfect")
