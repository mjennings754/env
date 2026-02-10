# Display the number of letters in the string

letters = "abcdefghijklmnopqrstuvwxyz"
print(len(letters))

# Concatenate two strings together
string1 = "please"
string2 = "explain"
print(string1 + string2)

# Display two strings together, with a space in between
string1 = "please"
string2 = "explain"
print(string1 + " " + string2)

# Use subscripting to display part of a string
print("bazinga"[2:6])


# Take input from the user and display that input back
user_input = input("Type a word: ")
print(user_input)

# Display the input string converted to lower-case letters
print(user_input.lower())

# Take user input and display the number of input characters.
print(len(user_input))

# Return the upper-case first letter entered by the user

first_letter = user_input[0]

print(first_letter.upper())

# Store an integer as a string
number = "6"

# Convert the 'integer' string into an int object using int()
# Multiply the integer by 7 and display the result

print(int(number) * 7)

# Store a floating-point number as a string

float_string = "0.1"

# Convert the 'float' string into a number using float()
# Multiply the number by 7 and display the result

print(float(float_string) * 7)

# Create a string and an int object, then display them together

stre = "mwes"
intobj = 9

print(stre + str(intobj))

# Get two numbers from the user, multiply them,
# and display the result
num1 = int(input("Type a number: "))
num2 = int(input("Type a number: "))

result = num1 * num2
print(result)