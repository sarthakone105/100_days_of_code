exam = input("What is your subject?  ")
max = int(input("What is the maximum score?  "))
score = int(input("What is your score?  "))

percentage = round((score / max) * 100, 2)

if percentage >= 90:
  print("You got", percentage, "% which is an A+")

elif percentage >= 80 and percentage <= 89:
  print("You got", percentage, "% which is an A")

elif percentage >= 70 and percentage <= 79:
  print("You got", percentage, "% which is a B")

elif percentage >= 60 and percentage <= 69:
  print("You got", percentage, "% which is a C")

elif percentage >= 50 and percentage <= 59:
  print("You got", percentage, "% which is a D")

else:
  print("You got", percentage, "% which is a U")
