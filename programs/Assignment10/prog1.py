#print the following pattern

#1  4   9
#16 25 36
#49 64 81

rows=int(input("Enter rows"))
num=1
for i in range(rows):
    
    for j in range(rows):
        print(num*num,end=" ")
        num+=1
    print("")    
