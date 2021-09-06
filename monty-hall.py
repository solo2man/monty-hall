# This program is intended to provide the user with three choices, one of those choices represents the "winner"
#  The user has the ability to change their selection to one of the other options after learning which option was not the "winner"
#  At the end, the user is informed if their last choice was the winner or not.

# Select the winning location
import random
# Selects a number between 1 and 3 (1 included, 4 not included)
winning_location = int(random.randrange(1, 4))

# Collect a number from the user
while True:
    try:
        usr_number = int(input("Please enter a number from 1 to 3: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    if usr_number > 3:
        print("The number entered:", usr_number, "is greater than 3. Please try again.")
    else:
        # Valid input received
        print("Your selected number is ", usr_number)
        break

# Select a number which is not either the user selected value or the winning location
while True:
    try:
        losing_location = int(random.randrange(1, 4))
    except ValueError:
    if (losing_location == usr_number):
        continue
    if (losing_location == winning_location):
        continue
    else:
        break

# Find the number which is not the losing number, and not the user number. This will be the change-to option
while True:
    try:
        change_to = int(random.randrange(1, 4))
    except ValueError:
    if (change_to == usr_number):
        continue
    else:
        break

# Present the user with a losing location. Ask for a change.
while True:
    try:
        usr_change = input("Location ", losing_location, "is not the winner. Would you like to change to ",change_to,"? (y/n)")
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    if (usr_change == "y"):
        print("Changing your selection from ",usr_number," to ",change_to)
        changed = " and changed your number"
        usr_number = change_to

# Determine the winner
print("The winning number was ",winning_location,", you selected ",usr_number,changed,".")
