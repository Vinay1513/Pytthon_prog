#Print the following pattern

# A B C
# D E F
# G H I

rows=int(input("Enter rows"))
n=65
for i in range(rows):
    
    for j in range(rows):
        print(chr(n),end=" ")
        n+=1
    print("")    
