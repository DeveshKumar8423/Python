height = int(input("Enter your height in cm : "))
age = int(input("Enter your age : "))
if(height>=120):
    if(age>=18):
        print("You can ride")
    else:
        print("You cannot ride")
else:
    print("You cannot ride")