#Highest score in class (maximum)
list = []
max = 0
rough = 0
marks = int(input("Input how many marks do you want to enter :"))
for i in range(marks):
    mark = int(input("ENter marks :"))
    list.append(mark)

for i in list:
    if i>max:
        max = i
print(f"The highest score in class is {max}")


    