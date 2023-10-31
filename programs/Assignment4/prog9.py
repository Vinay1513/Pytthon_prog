
#WAP to print the count of all negative no. from a given range

count=0

x=int(input("Enter first no. : "))
y=int(input("Enter second no : "))

for i in range(x,y):
    if(i<0):
        count=count+1
print(count)
