#Program1:Print the following pattern
#1
#2 2
#3 3 3
#4 4 4 4

rows=int(input("Enter rows"))
num=1
for i in range(rows):
    for j in range(i+1):
        print(num,end=" ")
    print("")
    num+=1
