#5 WAP to print the first 10 negative numbers  which is less than the given number

n=int(input("Enter a number"))
i=0
neg_num=[]
while(i<10):
    neg_num.append(n-1)
    n=n-1
    i+=1
print(neg_num)



