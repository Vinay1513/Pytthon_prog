#Program5:Print the following pattern
# 1 2 3 4
# 1 2 3
# 1 2
# 1

rows=int(input("Enter rows"))
for i in range(rows):
    for j in range(rows-i):
        print(j+1,end=" ")
    print(" ")
