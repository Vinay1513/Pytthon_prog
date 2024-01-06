#program2:print the following pattern
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

rows=int(input("Enter rows"))
for i in range(rows):
    num=rows
    for j in range(i+1):
        print(num,end=" ")
        num=num-1
    print("")
    
