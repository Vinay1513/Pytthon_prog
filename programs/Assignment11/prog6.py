#program6:Print the following pattern
# 1 0 1 0 1
# 1 0 1 0
# 1 0 1
# 1 0
# 1

rows=int(input("Enter rows"))
for i in range(rows):
    for j in range(1,rows+1-i):
        if(j%2==0):
            print("0",end=" ")
        else:
            print("1",end=" ")
    print(" ")

