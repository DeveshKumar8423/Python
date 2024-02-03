#add even number up to n by range
last = int(input("Input from 1 to how much you want to sum : "))
sum = 0
for i in range(0 , last+1 , 2):
        sum = sum+i
print(sum)