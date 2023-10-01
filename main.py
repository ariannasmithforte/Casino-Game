# Arianna Smith-Forte'
# The purpose of this program is to simulate casino games.

'''
•	create a python project and import the random module to generate random numbers.
•	create a function “roulette wheel” that will produce random numbers for the game.
•	create a function for the game, straight up, the user would have to choose game 1.
o	The player will input a number between 1-36.
o	The roulette wheel will produce a random number between 1-36.
o	If the player input = the roulette number, return to the player 35 x 5 in money.
o	Else, return nothing.
•	Create a function for the game, split bet, the user would choose game 2.
o	The player will bet between two adjacent numbers on a table.
o	The roulette wheel will choose an adjacent row of numbers on the wheel.
o	If the player guessed the roulette number or the roulette number + 1 or the roulette number - 1, return 17 x 5 in money.
o	Else, return nothing.
•	Create a function for the game, street, the user would choose game 3.
o	The player will bet on a row on the roulette table.
o	The roulette wheel will guess randomly a number between 1-36.
o	If the player number is <= to the result <= player number +2, return 11 x 5 in money.
o	Else, return nothing.
•	Create a function for the game, top, the user will choose game 4.
o	The player bets that the number will fall on a number 1-18.
o	The roulette wheel will randomly choose a number 1-36.
o	If the bet lands on a number <= 18, return $10.
o	Else, return nothing.
•	Create a function for the game, bottom, the user will choose game 5.
o	The player bets that the number will be between 19-36.
o	The roulette wheel will randomly choose a number 1-36
o	If the bet lands on a number >= 19, return $10.
o	Else, return nothing.
•	Create a function for the game, even and odd, the user will choose game 6.
o	The player is betting the if number will be even or odd.
	Ask for input of Even or Odd.
o	The roulette will choose a number between 1-36.
o	If the player is correct, return $10.
o	Else, return nothing.
•	If the play chooses game 7, the game will quit.
o	Print: “Thank you for playing at Dr ___ Roulette Table! We hope to see you again soon!”
•	create a while loop that will infinitely loop that game so that the player never has to refresh game.
o	create a print statement that says, “Welcome to __ Roulette Table!” and explains the game rules. 
o	create print statements that will describe all the betting options (1-7)
o	create an input that ask user to pick a number 1-7, to choose a game.
o	If the choice is game 7, break the loop.
o	If the choice for a game is bigger than 7 or less than zero, print “Invalid input. Please enter a number 1-7.”
o	create if and else-if statements for every game to calculate the winnings of each game.
	if game == 1: winnings = straight up (input number)
	if game == 2: winnings = split (input number)
	if game == 3: winnings = street (input number)
	if game == 4: winnings = top ()
	if game == 5: winnings= bottom ()
	if game == 6: winnings= even_odd(bet_type)
o	If winnings > $0, print “Congratulations! You won $__ winnings!”
o	Else, print “Sorry, you lost. Better luck next time.”

'''
import random

# Function to simulate the roulette wheel
def roulette_wheel():
    return random.randint(1, 36)

# Function for the Straight Up bet
def straight_up_bet(player_num):
    outcome == roulette_wheel()
    if outcome == player_num:
        return 35 * 5  # 35 times the bet (every game costs $5)
    else:
        return 0

# Function for the Split bet
def split_bet(player_num, outcome):
    if player_num in (1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 35):
        # Calculate possible adjacent numbers based on the player_num
        possible_numbers = [player_num, player_num + 1, player_num + 3, player_num - 3]

        # Check if the outcome is one of the possible adjacent numbers
        if outcome in possible_numbers:
            return 17 * 5  # 17 times the bet (every game costs $5)
    elif player_num in (2, 5, 8, 11, 14 ,17 , 20, 23 , 26, 29, 32, 35):
        possible_numbers1 = [player_num, player_num + 1, player_num - 1, player_num + 3, player_num - 3 ]

        if outcome in possible_numbers1:
          return 17 * 5
    elif player_num in (3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36):
        possible_numbers2 = [player_num, player_num - 1, + player_num + 3, player_num - 3]

        if outcome in possible_numbers2:
          return 17 * 5
    return 0 

# Function for the Street bet
def street_bet(player_num, outcome):
   if player_num in (1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 35):
        # Calculate possible adjacent numbers based on the player_num
        possible_numbers = [player_num, player_num + 1, player_num + 2]

        # Check if the outcome is one of the possible adjacent numbers
        if outcome in possible_numbers:
            return 17 * 5  # 17 times the bet (every game costs $5)
   elif player_num in (2, 5, 8, 11, 14 ,17 , 20, 23 , 26, 29, 32, 35):
        possible_numbers1 = [player_num, player_num + 1, player_num - 1]

        if outcome in possible_numbers1:
          return 17 * 5
   elif player_num in (3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36):
        possible_numbers2 = [player_num, player_num - 1, + player_num - 2]

        if outcome in possible_numbers2:
          return 17 * 5
   return 0 

# Function for the Top bet
def top_bet(outcome):
  
    if 1 <= outcome <= 18:
        return 10  # Fixed payout for Top bet (every game costs $5)
    else:
        return 0

# Function for the Bottom bet
def bottom_bet(outcome):
    if 19 <= outcome<= 36:
        return 10 
    else:
        return 0

# Function for the Even/Odd bet
def even_odd_bet(outcome, even_odd_choice):
    if even_odd_choice == "Even number" and outcome % 2 == 0:
        return 10  
    elif even_odd_choice == "Odd number" and outcome % 2 != 0:
        return 10  
    else:
        return 0

# Display welcome message and rules
print("                        Welcome to Arianna's Roulette Table!")
print("                                    Game Rules:")
print("                               Every bet costs $5.")

i = 1  # Initialize the counter

# main game loop that will run infinetly 
while True:
    print("\nBetting Options:")
    print("1. Straight Up: Single number selection. Potential payout is 35 times the bet.")
    print("2. Split: Single number selection. Covers the chosen number and one adjacent number. Potential payout is 17 times the bet.")
    print("3. Street: Single number selection. Covers the chosen number and the next two numbers in sequence. Potential payout is 11 times the bet.")
    print("4. Top: Any number from 1-18. Potential payout is even money ($10).")
    print("5. Bottom: Any number from 19-36. Potential payout is even money ($10).")
    print("6. Even/Odd: Covers all even or all odd numbers from 1-36. Potential payout is even money ($10).")
    print("7. Quit Game")

    choice = input("Choose your game (1-7): ")

    if choice == "7":
        print("Thank you for playing! Have a great day!")
        break  # Exit the loop if the user chooses to quit

    if choice not in ("1", "2", "3", "4", "5", "6"):
        print("Invalid choice. Please choose a valid option.")
        i += 1  # Increment the counter
        continue

    choice = int(choice)

    if choice in (1, 2, 3):
        player_number = int(input("Enter the number you want to bet on (1-36): "))
        if player_number < 1 or player_number > 36:
            print("Invalid number. Please choose a number between 1 and 36.")
            i += 1  # Increment the counter
            continue

    outcome = roulette_wheel()
    print("..........................................")
    print("........... Spinning the Wheel ...........")
    print("..........................................")


    if choice == 1:
        winnings = straight_up_bet(player_number)
    elif choice == 2:
        winnings = split_bet(player_number, outcome)
    elif choice == 3:
        winnings = street_bet(player_number, outcome)
    elif choice == 4:
        winnings = top_bet(outcome)
    elif choice == 5:
        winnings = bottom_bet(outcome)
    elif choice == 6:
        even_odd_choice = input("Enter 'Even number' or 'Odd number': ")
        if even_odd_choice not in ("Even number", "Odd number"):
            print("Invalid choice. Please enter 'Even number' or 'Odd number'.")
            i += 1  
            continue
        winnings = even_odd_bet(outcome, even_odd_choice)

    if winnings > 0:
        print(f"Result: The rolled number is {outcome}")
        print(f"Congratulations! You won ${winnings}.")
    else:
        print(f"Result: The rolled number is {outcome}")
        print("Sorry, you lost. Better luck next time!")
