import random
names = input("Enter all names of the persons : ")
listnames = names.split(", ")
num_items = len(listnames)
random_choice = random.randint(0 , num_items-1)
print(random_choice)

