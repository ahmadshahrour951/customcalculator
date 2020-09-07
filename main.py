def convert_to_c(temp_f):
  # this is a helper function that takes the input of temp F  and calculates the output which is temp C
    return ((int(temp_f) - 32) * 5) / 9


def convert_to_f(temp_c):
  # this is a helper function that takes the input of temp C  and calculates the output which is temp F
    return ((temp_c * 9) / 5) + 32


print("Hey there! it's super difficult to convert Celsius to Fahrenheit and vice versa. That's why you came to me instead of the incumbent Google..hehe")

# I ask for the user the temperature unit output required
temp_choice = input("Would you like to enter Celsius or Fahrenheit?")

# I validate user input for the temperature unit choice using a while loop
while temp_choice != 'Celsius' and temp_choice != 'Fahrenheit':
    print("Your input was incorrect. Please try again.")
    temp_choice = input(
        "Would you like to enter Celsius or Fahrenheit?")
    continue

# I ask for the user the temperature
user_input = input(
    "Enter the temperature in " + temp_choice +)

# this will go into an infinite loop of input validation
while user_input.isdigit() == False:
    print("Your input was not a number. Please try again.")
    user_input = input(
        "Enter the Fahrenheit temperature you want to convert to Celsius: ")
    continue

# this is where the answer will be printed, that means that the user_input was a number
if temp_choice == 'Celsius':
    print("The answer is: " + str(convert_to_f(user_input)) + " " + temp_choice)
else:
    print("The answer is: " + str(convert_to_c(user_input)) + " " + temp_choice)

print("Thank you for using my service!")
