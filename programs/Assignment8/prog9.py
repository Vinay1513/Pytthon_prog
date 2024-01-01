#9:Check number is strong or not

sum=0
num=int(input("Enter a number"))
temp=num
while(temp>0):
    n=1
    fact=1
    rem=num%10
    while(n<=rem):
        fact=fact*n
        n+=1
    sum=sum+fact
    num//=10
if(sum==temp):
    print(str(temp)+'is a strong number')
else:
    print(str(temp)+'is not a strong number')
