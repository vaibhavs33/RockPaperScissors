keepPlaying = True

player1 = input("What is player 1's choice? ")

while(player1 != "rock" and player1 !="paper" and player1 != "scissors"):
    player1 = input("Please choose a valid choice (rock,paper, or scissors): ")

# print(player1,"is the right choice")

player2 = input("What is player 2's choice? ")

while(player2 != "rock" and player2 !="paper" and player2 != "scissors"):
    player2 = input("Please choose a valid choice (rock,paper, or scissors): ")

# print(player2,"is the right choice") 

if player1 == player2:
    print("Tie")
elif player1 == 'rock' and player2 == 'scissors':
    print("Player 1 wins.")
elif player1 == 'paper' and player2 == 'rock':
    print("Player 1 wins.")
elif player1 == 'scissors' and player2 == 'paper':
    print("Player 1 wins.")
elif player2 == 'rock' and player1 == 'scissors':
    print("Player 2 wins.")
elif player2 == 'paper' and player1 == 'rock':
    print("Player 2 wins.")
elif player2 == 'scissors' and player1 == 'paper':
    print("Player 2 wins.")
 
choice = input("Would you like to play again?(y/n): ")
if(choice == "n"):
    keepPlaying = False