#Prime number Program by function

def Prime_number(n):
    list = []
    for i in range(2,n+1):
        if(n%i==0):
            list.append(i)
            print(f"{n} is not a prime number")
            break
        else:
            print(f"{n} is a prime number")

prime = int(input("Input number : "))

Prime_number(prime)
