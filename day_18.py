number = int(input("Enter a number; 1 to 1000: "))

while True:
  guess = int(input("Guess the number: "))

  if guess == number:
    print("You guessed it!")
    break

  elif guess >= (number + 100) or guess <= (number - 100):
    print("Hundreds off!")
    print("Guess again!")
    continue

  elif guess >= (number + 50) or guess <= (number - 50):
    print("Half a century far")
    print("Guess again!")
    continue

  elif guess >= (number + 25) or guess <= (number - 25):
    print("Quarter century far")
    print("Guess again!")
    continue

  elif guess >= (number + 10) or guess <= (number - 10):
    print("Hot hot hot, only 10 paces off")
    print("Guess again! Almost there")
    continue

print("Good job")


# number = int(input("Enter a number; 1 to 1000: "))

# while True:
#     guess = int(input("Guess the number: "))

#     if guess == number:
#         print("You guessed it!")
#         break

#     elif abs(guess - number) >= 100:
#         print("Hundreds off!")
#         print("Guess again!")

#     elif abs(guess - number) >= 50:
#         print("Half a century far")
#         print("Guess again!")

#     elif abs(guess - number) >= 25:
#         print("Quarter century far")
#         print("Guess again!")

#     elif abs(guess - number) >= 10:
#         print("Hot hot hot, only 10 paces off")
#         print("Guess again! Almost there")

# print("Good job")
