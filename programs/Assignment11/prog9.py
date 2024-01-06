#Program9 : Print the following pattern

# E
# E D
# E D C
# E D C B
# E D C B A

rows=int(input("Enter rows"))
for i in range(rows):
    char=rows+64
    for j in range(i+1):
        print(chr(char),end=" ")
        char=char-1
    print(" ")

