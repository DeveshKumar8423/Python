#Grading Program
students_score = {"Devesh" : 100 , "Yash" : 80 , "Ankit" : 70 }
students_grades = {}

for student in students_score:
    score = students_score[student]
    if score>90:
        students_grades[student] ="Outstanding"
    elif score>80:
        students_grades[student] ="Excellant"
    elif score>70:
        students_grades[student] ="Good"
    elif score>60:
        students_grades[student] ="Average"
    else:
        students_grades[student] ="Fail"

print(students_grades)

