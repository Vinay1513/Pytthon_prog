#Print the following pattern

# $ = $ =
# $ = $ =
# $ = $ =
# $ = $ =

rows=int(input("enter rows"))
num=1
for i in range(rows):
    for j in range(rows):
        if(num%2==0):
            print("=",end=" ")
        else:
            print("$",end=" ")
        num+=1

    print("")
