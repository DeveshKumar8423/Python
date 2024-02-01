height = int(input("Enter your height in cm : "))
if(height>=120):
    print("You can ride the rollercoaster")
    age = int(input("Enter your age : "))
    if(age>=18):
        print("Pay 5$")
    else:
        print("Pay 2$")
else:
    print("Sorry , you have to grow taller before you ride")