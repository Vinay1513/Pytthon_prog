#program 4:print the following pattern
# 1 1 1 1
# 2 2 2
# 3 3
# 4

rows=int(input("Enter rows"))
n=1
for i in range(rows):
    for j in range(rows-i):
        print(n,end=" ")
    n+=1
    print("")

