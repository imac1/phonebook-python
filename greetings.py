# "What's your name?"
# "Hello XY, I am your phone book."

name = input("What's your name? \n")
print("Hello " + f'{name}' + ", I am your phone book.")

# "How old are you?"
age = input("How old are you? \n")

# - "You are so young! Life is ahead of you!"
# - "That's a nice age!"
# - "You must be very wise!"
# - "That doesn't seem to be an integer."

if age.isnumeric():
    if int(age) <= 18:
        print("You are so young! Life is ahead of you!")      
    elif int(age) < 40:
        print("That's a nice age!")
    elif int(age) >= 40:
        print("You must be very wise!")
else:
    print("That doesn't seem to be an integer.")
