from getpass import getpass as input
print("E P I C    🪨  📄 ✂️    B A T T L E")
Point_1 = 0
Point_2 = 0
while True:
  
  player_1 = input("Player 1, choose R, P or S: ")
  player_2 = input("Player 2, choose R, P or S: ")
  
  if Point_1 == 3 or Point_2 == 3:
    if Point_2 == 3:
      print("Player 2 wins!")
    else:
      print("PLayer 1 wins!")
    break
  elif player_1 == "R" and player_2 == "R":
    print("It's a tie!")
  
  elif player_1 == "R" and player_2 == "P":
    Point_2 += 1
  
  elif player_1 == "R" and player_2 == "S":
    Point_1 += 1
    
  elif player_1 == "P" and player_2 == "R":
    Point_1 += 1
    
  elif player_1 == "P" and player_2 == "P":
    print("Its a tie!")
  
  elif player_1 == "S" and player_2 == "R":
    Point_1 += 1
  
  elif player_1 == "R" and player_2 == "P":
    Point_2 += 1
  
  else:
    print("Please use Capital letters")




# from getpass import getpass as input

# print("E P I C    🪨  📄 ✂️    B A T T L E")

# Point_1 = 0
# Point_2 = 0

# while True:
#     player_1 = input("Player 1, choose R, P or S: ")
#     player_2 = input("Player 2, choose R, P or S: ")

#     if player_1 not in ['R', 'P', 'S'] or player_2 not in ['R', 'P', 'S']:
#         print("Please use capital letters R, P, or S only")
#         continue

#     if player_1 == player_2:
#         print("It's a tie!")
#     elif (player_1 == "R" and player_2 == "S") or (player_1 == "P" and player_2 == "R") or (player_1 == "S" and player_2 == "P"):
#         Point_1 += 1
#         print("Player 1 wins this round!")
#     else:
#         Point_2 += 1
#         print("Player 2 wins this round!")

#     print(f"Score: Player 1 = {Point_1}, Player 2 = {Point_2}")

#     if Point_1 == 3 or Point_2 == 3:
#         if Point_2 == 3:
#             print("Player 2 wins the game!")
#         else:
#             print("Player 1 wins the game!")
#         break
