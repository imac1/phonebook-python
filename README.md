# Phonebook

## Story

You just moved to a new town, and you'd like to get new friends as soon as possible.
You've decided to create a phone book application, or at least some parts of it first.

While you were experimenting with a friendly user interface, you attended a cool office party
where you collected a few phone numbers. Later on you realized that many numbers are
incorrect (maybe the party was too good), so you decided to write a program that selects the
good ones, and also checks for their area codes.

## What are you going to learn?

- Get user input.
- Concatenate strings.
- Write strings to the console.
- Use lists.
- Use conditional statements.
- Count items.

## Tasks

1. Ask for the user's name in `greetings.py`, and print out a friendly, personalized message.
    - The program asks for the user's name.
    - After the input, the program greets the user by the given name like this: `Hello XY, I am your phone book.`

2. Still in in `greetings.py`, ask for the user's age, and print a polite message based on the answer. Only integers should be accepted.
    - If the input is not an integer, the following message is displayed: `That doesn't seem to be an integer.`
    - If the user is 18 or younger, the following message is displayed: `You are so young! Life is ahead of you!`
    - If the user is older than 18, but younger than 40, the following message is displayed: `That's a nice age!`
    - If the user is at least 40, the program prints out the following message: `You must be very wise!`

3. You found a few numbers in your phonebook (see `phonebook.py`) that are shorter than the others so they are possibly wrong numbers. A valid number looks like `nn-nnn-nnn`. Your task is to separate the good ones from the wrong ones, and print the two lists after each other. The formatting does not matter here.
    - The program selects and indicates the wrong numbers by any means.
    - The program prints out the good phone numbers first, then the list of the wrong ones.

4. Print out the list or area codes and the list of phone numbers separately.
    - The area codes are printed as a separate list.
    - The phone numbers are printed without the area codes separately.
    - Both lists contain pieces of completely valid phone numbers.

5. Collect the unique area codes from the list.
    - The program prints out the list of area codes without duplicates.
    - The list contains area codes of completely valid phone numbers.

6. Count how many (valid) phone numbers belong to the given area codes.
    - The program counts (without hardcoding the results) the phone numbers belonging to the three given area codes (98, 34, 72) and prints the results.
    - The counter only counts valid phone numbers.

## General requirements

None

## Hints

- Please use the given list of phone numbers, and do not modify it.
- For number validation you can use the `isnumeric()` method on strings. You can read about it in the background materials.
- The area number is the first two digits of the (valid) phone number.
- You should use f-strings when printing, it makes your life easier.
- You can either remove the invalid numbers from the list, or just create a new list for the valid ones.

## Background materials

- <i class="far fa-exclamation"></i> [Strings]
- <i class="far fa-exclamation"></i> [User input]
- <i class="far fa-exclamation"></i> [Control structures]
- <i class="far fa-candy-cane"></i> [Conditional Statements in Python](https://realpython.com/python-conditional-statements/)
- <i class="far fa-candy-cane"></i> [Isnumeric built-in function](https://www.w3schools.com/python/ref_string_isnumeric.asp)
