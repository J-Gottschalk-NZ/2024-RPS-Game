# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


# Displays instructions
def instruction():
    print('''

**** Instructions ****

To begin, choose the number of rounds (or press <enter> for 
infinite mode).

Then play against the computer.  You need to choose R (rock),
P (paper) or S (scissors).

The rules are as follows:
o	Paper beats rock
o	Rock beats scissors
o	Scissors beats paper

Press <xxx> to end the game at anytime.

Good Luck!
    ''')


# Main routine
print()
print("💎📰✂ Rock / Paper / Scissors Game ✂📰💎")
print()

# ask user if they want to see the instructions and display
# them if requested
want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

print("program continues")
