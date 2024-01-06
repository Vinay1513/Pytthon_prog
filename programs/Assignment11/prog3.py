#program3:Print the following pattern
# 1
# 3 5
# 7 9 11
# 13 15 17 19
rows=int(input("Enter rows"))
n=1
for i in range(rows):
    for j in range(i+1):
        print(n,end=" ")
        n+=2
    print("")
