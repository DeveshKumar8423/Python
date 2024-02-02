#calculate average
list = []
sum = count = 0
marks = int(input("Input how many marks do you want to enter :"))
for i in range(marks):
    mark = int(input("ENter marks :"))
    list.append(mark)
    sum = sum + mark
    count+=1

average = sum / count
print(f"The average of all marks are : {average}")
