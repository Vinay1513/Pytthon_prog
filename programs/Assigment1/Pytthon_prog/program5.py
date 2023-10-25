
#write a program to take an integer ranging from 0 to 6 and print corresponding weekday(starting from monday)

a=int(input("Enter a integer"))
if(a<=6):

        if(a==0):
            print("Monday")
        elif(a==1):
            print("Tuesday")
        elif(a==2):
            print("Wednesday")
        elif(a==3):
            print("Thursday")
        elif(a==4):
            print("Friday")
        elif(a==5):
            print("Saturday")
        elif(a==6):
            print("Sunday")
        else:
            print("no weekday")
else:
      print("Invalid integer")
            
