def infinity_dice_roll(side):
  side = int(side)
  import random
  roll = random.randint(1, side + 1)
  return roll


while True:
  
  sides = int(input("How many sides? "))
  roll = infinity_dice_roll(sides)
  print(f"You rolled {roll}")
  prompt = input("Roll again? ")
  if prompt == 'no':
    break

  else:
    continue
  

  
print("Bye Bye")  