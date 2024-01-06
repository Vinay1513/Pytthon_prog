#Program10: Print the following pattern

# E F G H I
# D E F G
# C D E
# B C
# A

rows=int(input("Enter rows"))
char=rows+64
for i in range(rows):
    char=rows+64-i
    for j in range(rows-i):
        print(chr(char),end=" ")
        char+=1
    print(" ")
