user_input = input("Enter a number (press Enter for default): ")

if user_input == "":
    number = 10   # default value
else:
    number = int(user_input)

print("Value is:", number)
