#BMI Calculator
height = int(input("Enter your height in m : "))
weight = int(input("Enter your weight in kg : "))

bmi = weight / float(height) **2
print(bmi)
int_bmi = int(bmi)