x = 3
y = 5
z = x + y
print(z)

# two_digit_number = input("type a two digit number")
#
# input("enter a two digit number")
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
# two_digit_number = first_digit + second_digit
# print(two_digit_number)

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
#
# bmi = int(weight) / float(height) ** 2
# bmi_as_int = int(bmi)
# print(bmi_as_int)


# score = 0
# height = 1.8
# weight = 80
# isWinning = True
# print(f"your score is {score}age = {height}, your weight is {weight}, you are winning is {True}")


# age = input("what is your current age")
# days = input("numbers of day left")
# weeks = input("numbers of weeks left")
# months = input("numbers of months left")
# print(f"your age is {age}, numbers of day left is {days}, numbers of weeks left is {weeks}, numbers of month left is{months}")


# age = input("what is your current age")
#
# age_as_int = int(age)
#
# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12
# print(f"you have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left")

print("welcome to the tip of calculator !")
bill = float(input("what was the total bill? $"))
tip = int(input("how much tip wound you like to give? 10, 12, or 15? "))
people = int(input("how mny people to split the bill?"))
bills_with_tip = tip /100 * bill + bill
print(bills_with_tip)
