#Tip Calculator
print("Welcome to the tip calculator")

a = input("What was the total bill ?")
b = input("What percentage tip would you like to give ?")
bill = int(a)
tipp = int(b)

percentage_tip = tipp/100
tip = bill * percentage_tip
total_bill = bill + tip
c = input("How many people to split the bill ?")
people = int(c)
each_person_bill = total_bill / people
indi_bill = int(each_person_bill)

print("Each person should pay : " , indi_bill)