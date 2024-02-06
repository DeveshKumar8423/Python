#how many cans you will need to paint a wall 
import math

def area_calculated(h , w):
    cans = math.ceil((h * w)/c)
    print(f"You will need {cans} cans ")

h = float(input("Input height in m : "))
w = float(input("Input width in m : "))
c = 5

area_calculated(h,w)