#BMI Calculator
height = float(input("Enter your height in m : "))
weight = int(input("Enter your weight in kg : "))

bmi = round(weight / float(height) **2)
print(bmi)
if(18.5>bmi):
    print(f"Your bmi is {bmi} , You are underweight")
elif(18.5<=bmi<25):
    print(f"Your bmi is {bmi} , You are normal weight")
elif(25<=bmi<30):
    print(f"Your bmi is {bmi} , You are overweight")
elif(30<=bmi<35):
    print(f"Your bmi is {bmi} , They are obese")
else:
    print(f"Your bmi is {bmi} , You are clinically obese")