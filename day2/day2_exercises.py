# two_digit_number = input("Type a two digit number: ")
# dig0 = two_digit_number[0]
# dig1 = two_digit_number[1]
# result = int(dig0) + int(dig1)
# print(result)

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# bmi = float(weight) / (float(height) ** 2)
# print(int(bmi))

age = input("What is your current age? ")
till_90 = 90 - int(age)
days = till_90 * 365
weeks = till_90 * 52
months = till_90 * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")