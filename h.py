#BMI Calculator
height = (input("Enter your height in m : "))
weight = (input("Enter your weight in kg : "))

bmi = weight / float(height) **2
print(bmi)
int_bmi = int(bmi)