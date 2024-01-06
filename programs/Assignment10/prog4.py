#Print the following pattern
# 2 5 10
# 17 26 37
#50 65 82

rows=int(input("Enter rows"))
n=1
for i in range(rows):
    for j in range(rows):
        print((n*n)+1,end=" ")
        n+=1
    
    print("")

