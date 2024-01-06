#Print the following pattern

# D4 C3 B2 A1
# D4 C3 B2 A1
# D4 C3 B2 A1
# D4 C3 B2 A1


rows=int(input("Enter rows"))

for i in range(rows):
    char=rows+64
    n=rows
    for j in range(rows):
        print((chr(char))+str(n),end=" ")
        char=char-1
        n=n-1
    print("")


