#Fizz-Buzz Game 
last = int(input("Input from 1 to how much you want to sum : "))
for i in range(1 , last+1):
    if((i%3==0) and (i%5==0)):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)