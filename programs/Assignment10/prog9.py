
#Print the following pattern

# A b C
# d E f
# G h I

rows=int(input("Enter rows"))
n=1
for i in range(rows):
    c=rows+95
    char=rows+62
    for j in range(rows):
        if(n%2==0):
            print(chr(c),end=" ")
            c+=2

        else:
            print(chr(char),end=" ")
            char+=2
        
    n+=1
        
    print("")

