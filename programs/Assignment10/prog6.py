#Print the following pattern
# 1 4 7 10
# 2 5 8 11
# 3 6 9 12
# 4 7 10 13

rows=int(input("Enter rows"))
for i in range(rows):
    num=i+1
    for j in range(rows):
        print(num,end=" ")
        num+=3
    print("")
