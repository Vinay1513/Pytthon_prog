#2:check prime or not

cnt=0
n=int(input("Enter"))
i=1
while(i<=n):
    if(i%n):
        cnt+=1
    i+=1
if(cnt==2):
    print(n,"is not a prime")
else:
    print(n,"is a prime")
    
 

