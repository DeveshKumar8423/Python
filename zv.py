#Days in Month

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                



def days_in_month(year , month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

year = int(input("Enter year : "))
month = int(input("Enter month : "))
days = days_in_month(year , month)
print(days)