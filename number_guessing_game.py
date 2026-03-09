#number guessing game
import getpass # this module allows us to hide the input of the user, so that the other player cannot see the number that is being entered.

player1 = input("Player 1, please enter your name: ")
player2 = input("Player 2, please enter your name: ")

print("Welcome to the number guessing game, " + player1 + " and " + player2 + "!")

player1_number = int(getpass.getpass(player1 +"Enter number between 1 and 20: ")) 
player2_number = int(getpass.getpass(player2 +"Enter number between 1 and 20: "))

def check_winner(num1, num2):
    while True:
        player1_turn = int(input(f"{player1}, guess a number :"))
        if player1_turn == num2:
            print(player2 + " wins!" + "you cuted the number of " + player2 + " is " + str(num2))
            break
        else:
            player2_turn = int(input(f"{player2}, guess a number :"))
            if player2_turn == num1:
                print(player1 + " wins!" + "you cuted the number of " + player1 + " is " + str(num1))
                break

check_winner(player1_number, player2_number)



