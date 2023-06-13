import random


# coin = random.randint(0,1)
# if coin == 0:
#     tossed = "Tails"
# else:
#     tossed = "Heads"

# print(tossed)

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# size = len(names)
# rand = random.randint(0, size)
# print(f"{names[rand]} is going to buy the meal today!")

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
column = int(position[0]) - 1
row = int(position[1]) - 1
map[row][column] = 'X'

print(f"{row1}\n{row2}\n{row3}")

