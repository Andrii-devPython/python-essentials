#COMMENT ALL - CMD K - CMD D -- UNC CMD K - CMD U
#2² control + command + space


# Variable = a container for a value (string, float, boolean, integer)
# A variable behaves as if it was the value it contains

# region
# Strings

# messageOnTg = "Hey mom, thanks for that"
# heardAfterThanks = "You are welcome"

# Integers

# sumOfGoals = 5
# yourAge = 21

# Floats

# priceOfToken = 10.99
# gpa = 3.2

# Booleans

# isStudent = True
# forSale = False
# endregion



# Typecasting = the process of converting a variable from one data type to another
# str(), int(), float(), bool() 

# region

#name = "Bro Code"
#age = 25
#gpa = 3.2
#isStudent = True

#gpa = int(gpa)

# print(gpa)

# endregion



# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

# region

# myName = input("What is your name?: ")
# myAge = input("How old are you?: ")

# myAge = myAge + 1

# print(f"Hello {myName}!")
# print("HAPPY BIRTHDAY")
# print(f"I am {myAge} years old!!!")

# endregion


# Exercise 1 Rectangle Area Calc

#length = float(input("Input length: "))
#width = float(input("Input width: "))
#areaCalc = length * width
#print(f"Rectangle Area Calc is: {areaCalc}cm²")

# Exercise 2 Shopping Cart Program

#item = input("What item would you like to buy?: ")
#price = float(input("What is the price?: "))
#quantity = int(input("How many would you like?: "))
#total = price * quantity

#print(f"You have bought {quantity} x {item}'s")
#print(f"Your total is: ${total}")

# Madlibs game

#adjective1 = input("Enter an adjective (description): ")
#noun1 = input("Enter a noun (person, place, thing): ")
#adjective2 = input("Enter an adjective (description): ")
#verb1 = input("Enter a verb ending with 'ing: ")
#adjective3 = input("Enter an adjective (description): ")

#print(f"Today I went to a {adjective1} zoo.")
#print(f"In an exhibit, I saw a {noun1}")
#print(f"{noun1} was {adjective2} and {verb1}")
#print(f"I was {adjective3}!")


# Python weight converter

#weight = float(input("Enter your weight: "))
#unit = input("Kilograms or Pounds? (K or L?): ")

#if unit == "K":
#    weight = weight / 2.205
#    unit = "Kgs."
#elif unit == "L":
#    weight = weight * 2.205
#    unit = "Lbs."
#else:
#    print(f"{unit} was not valid")
    
#print (f"Your weight is: {round(weight, 2)} {unit}")


# logical operators = evaluate multiple conditions (or, and, not)
#               or = at least one condition must be true
#               and = both conditions must be true
#               not = inverts the condition (not False, not True)


# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

