#Leap Year Program
leapyear = int(input("Enter year you want to check : "))
if(leapyear%4 ==0 and leapyear%100!=0 )or( leapyear%400==0):
    print("Year is Leap year")
else:
    print("Not a leap year")
