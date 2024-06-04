#add number up to n by range
last = int(input("Input from 1 to how much you want to sum : "))
sum = 0
for i in range(1 , last+1):
    sum = sum+i
print(sum)