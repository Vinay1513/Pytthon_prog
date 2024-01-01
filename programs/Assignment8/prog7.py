#7:Check number is Armstrong or not

num=int(input("Enter a number"))
sum=0
n1=len(str(num))
temp=num
while(temp>0):
    rem=temp%10
    sum+=rem**n1
    temp//=10
if(num==sum):
       print(num,'is an Armstong number')
else:
       print(num,'is not a Armstrong number')
