def check_user():
  while True:
      username = input("Whats your username?- ")
      password = input("Whats your password?- ")

      if username == "david" and password == "baldies4life":
          break
      else:
          print("you are an imposter try again.")
          continue
  print("Welcome to Replit")