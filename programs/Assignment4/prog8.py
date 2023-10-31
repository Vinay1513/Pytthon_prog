
#WAP to print numbers which are divisible y 3 and 5 both in a given range

x=int(input("Enter Start no : "))
y=int(input("Enter End no : "))

for i in range(x,y):

    if(i%3==0)and(i%5==0):

        print(i,end=" ")
