#print the following pattern

# E D C B A
# E D C B A
# E D C B A
# E D C B A
# E D C B A

rows=int(input("Enter rows"))
for i in range(rows):
    char=rows+64
    for j in range(rows):
        print(chr(char),end=" ")
        char=char-1
    print("")
