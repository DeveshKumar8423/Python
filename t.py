#pizza order practice
print("Welcome to the Pizza Delieveries \n")
bill = 0
#size of pizza
size = input("What size of pizza do you want S , M , L : ")
addpep = input("Do you want peproni Y or N: ")
addcheese = input("Do you want extra cheese Y or N: ")

if(size=="S"):
    bill+=15
elif(size == "M"):
    bill+=20
else:
    bill+=25

#add peproni

if(addpep == 'Y'):
    if(size == 'S'):
        bill+=2
    else:
        bill +=3

#addcheese
if(addcheese == 'Y'):
    bill +=1

print(f"Your bill is {bill}")




