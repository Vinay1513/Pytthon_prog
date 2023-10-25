
#WAP that determines wheather a given input year is a leap year or no

year=int(input("Enter a year"))

if(year%400==0) and (year%100==0):

    print("{} is a leap year".format(year))

elif(year%4==0) and (year%100!=0):

    print("{} is a leap year".format(year))

else:

    print("{} is not a leap year".format(year))
