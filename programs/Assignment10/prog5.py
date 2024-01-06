#Print the following pattern
# 1 2 9 4
# 5 6 49 8
# 81 10 121 12
# 169 14 225 16

rows=int(input("Enter rows"))
num=1
for i in range(rows):
    for j in range(rows):
        if(num%2==1):
            print(num*num,end=" ")
        else:
            print(num,end=" ")
        num+=1
    print("")
