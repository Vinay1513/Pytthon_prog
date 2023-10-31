#WAP to calculate and print the product of the count of odd numbers within a given range

count=0
product=1
x=int(input("Enter first number"))
y=int(input("Enter second number"))

for i in range(x,y):
    if(i%2!=0):
        
        count=count+1
        product=product*i
    
print(product)
