# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height <= 120:
#     print("Allowed!")
# else:
#     print("Not allowed!")

# number = int(input("Which number do you want to check? "))
# if number % 2:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# age = int(input("What is your height age in years? "))

# if height <= 120:
#     print("Allowed!\n")
#     if age <= 12:
#         print("5$!\n")
#     elif age > 12 and age < 18:
#         print("7$!\n")
#     else:
#         print("12$!\n")
# else:
#     print("Not allowed!")

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# bmi = round(weight / (height ** 2))

# statemat = f"Your BMI is {bmi}, you "
# if bmi <= 18.5:
#     statemat += "are underweight"
# elif bmi > 18.5 and bmi <= 25:
#     statemat += "have a normal weight"
# elif bmi > 25 and bmi <= 30:
#     statemat += "are slightly overweight"
# elif bmi > 30 and bmi <= 35:
#     statemat += "are obese"
# elif bmi > 35:
#     statemat += "are clinically obese"

# print(statemat)

# year = int(input("Which year do you want to check? "))

# if year % 4 == 0 or (year % 100 != 0 and year % 400 == 0):
#     print("Leap year.")
# else:
#     print("Not leap year.")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# age = int(input("What is your height age in years? "))

# if height <= 120:
#     print("Allowed!\n")
#     if age <= 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age > 12 and age < 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#     print(f"Your final bill is ${bill}")
# else:
#     print("Not allowed!")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0

# if size == "S":
#     bill += 15
#     if add_pepperoni == "Y":
#         bill += 2
# elif size == "M":
#     bill += 20
#     if add_pepperoni == "Y":
#         bill += 3
# elif size == "L":
#     bill += 25
#     if add_pepperoni == "Y":
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}.")

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# age = int(input("What is your height age in years? "))

# if height <= 120:
#     print("Allowed!\n")
#     if age <= 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age > 12 and age < 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif age >= 45 and age <= 55:
#         print("Free ride!.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#     print(f"Your final bill is ${bill}")
# else:
#     print("Not allowed!")

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

name = name1 + name2

totalT = name.count("t")
totalR = name.count("r")
totalU = name.count("u")
totalE1 = name.count("e")
total1 = str(totalT + totalR + totalU + totalE1)

totalL = name.count("l")
totalO = name.count("o")
totalV = name.count("v")
totalE2 = name.count("e")
total2 = str(totalL + totalO + totalV + totalE2)

score = total1 + total2


if int(score) < 10 or int(score) > 90:
    print("Your score is " + score + ", you go together like coke and mentos.")

elif int(score) >= 40 and int(score) <= 50:
    print("Your score is " + score + ", you are alright together.")

else:
    print("Your score is " + score)