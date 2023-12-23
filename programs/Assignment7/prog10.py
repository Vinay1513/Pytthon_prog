
#10 WAP to print a cube of odd numbers up to n in reverse order.


n=int(input('Enter a number'))
i=1
while(n>=i):
    if(n%2==1):
        print(n**3,end= " ")
    n=n-1



