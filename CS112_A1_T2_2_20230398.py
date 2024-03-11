# File: CS112_A1_T2_2_20230398
# Purpose: The first player to gather 3 numbers that add up to 15 wins. If nobody did so, it's a draw.
# Author: Mariam Muhammad Youssef Othman Sharnoubi
# ID: 20230398

# Explaining the game.
print("***NUMBER SCRABBLE***""\nThis game is played with a list of numbers between 1 and 9. Each player takes"
      "\nturns picking a number from the list. Once a number has been picked, it cannot be picked"
      "\nagain. If a player has picked three numbers that add up to 15, that player wins the game."
      "\nHowever, if all the numbers are used and no player gets exactly 15, the game is a draw.\n" + "_" * 90)

winner = 0  # 0 : Draw ||| 1 : Player 1 is the winner ||| 2 : Player 2 is the winner
available_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # The user can choose one of these numbers.
player1_numbers = set()  # When player1 chooses a number, it'll be removed from available_numbers and added here.
player2_numbers = set()  # When player2 chooses a number, it'll be removed from available_numbers and added here.
# All possible combinations of 3 numbers that add up to 15.
possible_numbers = [{1, 9, 5}, {1, 8, 6}, {2, 9, 4}, {2, 8, 5}, {2, 7, 6}, {3, 8, 4}, {3, 7, 5}, {4, 6, 5}]


# Displays numbers gathered by player 1, numbers gathered by player 2 and available numbers.
def display_numbers():
    if player1_numbers:  # Display numbers gathered by player 1.
        print("Player 1 gathered:  ", end="")
        for number in player1_numbers:
            print(number, end="\t")
        print()

    if player2_numbers:  # Display numbers gathered by player 2.
        print("Player 2 gathered:  ", end="")
        for number in player2_numbers:
            print(number, end="\t")
        print("\n" + "_" * 45)

    print("Available numbers are:  ", end="")
    for number in available_numbers:  # Display available numbers.
        print(number, end="\t")


def get_number(player):  # Takes a valid number from available_numbers from the user.
    choice = input(f"\n{player}, choose an available number: ")
    while True:
        try:
            choice = int(choice)
            if choice in available_numbers:
                break
            else:  # The user entered an integer, but it wasn't in the available numbers.
                choice = input(f"\n{player}, choose an available number: ")
        except ValueError:  # The user didn't enter an integer.
            choice = input(f"\n{player}, choose an available number: ")
    return choice


# True as long as there is no winner and the list(available_numbers) isn't empty(there are numbers to pick).
while available_numbers and winner == 0:
    display_numbers()
    player1_choice = get_number("Player 1")
    player1_numbers.add(player1_choice)
    available_numbers.remove(player1_choice)
    print("_" * 45)

    for possibility in possible_numbers:  # Checks if player 1 gathered 3 numbers that add up to 15.
        if possibility.issubset(player1_numbers):
            winner = 1
            numbers = list(possibility)

            break

    if not available_numbers or winner != 0:  # Checks if there is any number left in available_numbers.
        break

    display_numbers()
    player2_choice = get_number("Player 2")
    player2_numbers.add(player2_choice)
    available_numbers.remove(player2_choice)
    print("_" * 45)

    for possibility in possible_numbers:  # Checks if player 2 gathered 3 numbers that add up to 15.
        if possibility.issubset(player2_numbers):
            winner = 2
            numbers = list(possibility)
            break

if winner == 0:
    print("\nIt's a draw. Nobody gathered 3 numbers that add up to 15.")
elif winner == 1:
    print(f"\nPlayer 1 is the winner. The sum of {numbers[0]}, {numbers[1]} and {numbers[2]} is 15.")
else:
    print(f"\nPlayer 2 is the winner. The sum of {numbers[0]}, {numbers[1]} and {numbers[2]} is 15.")

# Exit the game.
leave = input("Type exit or e to exit: ").strip().lower()
while leave != "exit" and leave != "e":
    leave = input("Type exit or e to exit: ").strip().lower()
