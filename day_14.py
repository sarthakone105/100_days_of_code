from getpass import getpass as input

player_1 = input("Player 1, choose R, P or S: ")
player_2 = input("Player 2, choose R, P or S: ")

if player_1 == "R" and player_2 == "R":
  print("It's a tie!")

elif player_1 == "R" and player_2 == "P":
  print("Player 2 wins!")

elif player_1 == "R" and player_2 == "S":
  print("Player 1 wins!")

elif player_1 == "P" and player_2 == "R":
  print("Player 1 wins!")

elif player_1 == "P" and player_2 == "P":
  print("Its a tie!")

elif player_1 == "S" and player_2 == "R":
  print("Player 2 wins!")

elif player_1 == "R" and player_2 == "P":
  print("Player 2 wins!")

else:
  print("Please use Capital letters")