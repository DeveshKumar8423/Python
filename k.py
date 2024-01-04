#how many time you have left program
age = input("Input your age : ")
int_age = int(age)
remaning_age = 100 - int_age
years = remaning_age
months = remaning_age * 12
weeks = remaning_age * 52
days = remaning_age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"You have {years} years or {months} months {weeks} weeks or {days} days or  {hours} hours or {minutes} minutes or {seconds} seconds left")