#Program7:Print the following pattern
# 1
# 1 2
# 2 3 4
# 4 5 6 7
#7 8 9 10 11

rows=int(input("enter rows"))
n=1
for i in range(rows):
    for j in range(i+1):
        print(n,end=" ")
        n+=1
    n-=1
    
        
        
    print("")

