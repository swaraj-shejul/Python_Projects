#number guessing game
import getpass # this module allows us to hide the input of the user, so that the other player cannot see the number that is being entered.

number_of_players = int(input("Enter the number of players more than one : "))
players= []
selected_numbers = {}

# this loop is used to get the names of the players and store them in a list called count. 
# The number of players is determined by the user input at the beginning of the program.
# The names of the players are then used to prompt them to enter their selected numbers, 
# which are stored in a dictionary called selected_numbers with the player's name as the key and the selected number as the value.

for i in range(number_of_players):
    name = input(f"Enter player{i+1} name: ")
    players.append(name)


print("Welcome to the number guessing game, " + ", ".join(players) + "!")

# this loop is used to get the selected numbers from each player and store them in the selected_numbers dictionary. 
# The getpass.getpass() function is used to hide the input of the user, so that the other player cannot see the number that is being entered.

for i in players:
    number = int(getpass.getpass(i +"Enter number between 1 and 20: "))
    selected_numbers[i] = number

# this loop is used to allow each player to take turns guessing the numbers selected by the other players.

while True:
    for i in players:
        player_turn = int(input(f"{i}, guess a number :"))
        if player_turn in selected_numbers.values():
            keys = [k for k, v in selected_numbers.items() if v == player_turn]
            print("player has won: " + ", ".join(keys))
            exit() 


