#Program8:Print the following pattern
# 1
# 3 2
# 6 5 4
# 10 9 8 7

rows=int(input("Enter rows"))
n=1
a=3
for i in range(rows):
    for j in range(i+1):
        print(n,end=" ")
        n-=1
    n=j+i+a
    a+=1
    
        
    print("")
