#where you want to dig hole
row1 = ["X","X","X"]
row2 = ["X","X","X"]
row3 = ["X","X","X"]
row= [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")

pos = input("Where you want to dig hole ? ")
horizontal = int(pos[0])
vertical = int(pos[1])

row[vertical-1][horizontal - 1] = "*"

print(f"{row1}\n{row2}\n{row3}") 