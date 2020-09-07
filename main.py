def convert(temp_f):
  # this is a helper function that takes the input of temp F  and calculates the output which is temp C
    return ((int(temp_f) - 32) * 5) / 9


# I ask for the user to input the data i request
user_input = input(
    "Enter the Fahrenheit temperature you want to convert to Celsius: ")

# this will go into an infinite loop of input validation
while user_input.isdigit() == False:
    print("Your input was not a number. Please try again.")
    user_input = input(
        "Enter the Fahrenheit temperature you want to convert to Celsius: ")
    continue

# this is where the answer will be printed, that means that the user_input was a number
print('The conversion is:  {} Celcius'.format(convert(user_input)))
