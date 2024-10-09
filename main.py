import random as r
version = "v.1.1"
print("Welcome to the Text Arcade(Press Enter)")
input("")
print("This is a text based Arcade where there is a lot of games to play")
input("")
gamemenu = """
Welcome to the arcade! More games can be found on my github!
Which game would you like to play?
1. Rock Paper Scissors
2. Add A Game
3. Exit
Please choose an option:"""
while True:
  optiongame = input(gamemenu)
  if optiongame == "1":
    print("Welcome to rock paper scissors by Russissmart Prodcutions...(press Enter)")
    input("")
    print("Before starting, please make sure you have (v. 1.1)")
    input("")
    print("Checking version...")
    input("")
    print("Checking for updates...")
    input("")
    print("All Clear!")
    input("")
    print("Starting game...")
    rpschoice = """
    Rock Paper or Scissors?
    1. Rock
    2. Paper
    3. Scissors
    Choose: """
    while True:
      choice = input(rpschoice)
      rps = ["rock", "paper", "scissors"]
      rpsopposition = r.choice(rps)
      if choice == "rock" and rpsopposition == "rock":
        print("You Choose...")
        input("")
        print(choice)
        input("")
        print("The opposing team choose...")
        input("")
        print(rpsopposition)
        print("TIE! You both choose rock!")
      if choice == "paper" and rpsopposition == "paper":
        print("You Choose...")
        input("")
        print(choice)
        input("")
        print("The opposing team choose...")
        input("")
        print(rpsopposition)
        print(f"TIE! You both choose {choice}!")
      if choice == "paper" and rpsopposition == "paper":
        print("You Choose...")
        input("")
        print(choice)
        input("")
        print("The opposing team choose...")
        input("")
        print(rpsopposition)
        print(f"TIE! You both choose {choice}!")
      if choice == "rock" and rpsopposition == "scissors":
        print("You Choose...")
        input("")
        print(choice)
        input("")
        print("The opposing team choose...")
        input("")
        print(rpsopposition)
        print(f"You Win!")
      if choice == "paper" and rpsopposition == "rock":
        print("You Choose...")
        input("")
        print(choice)
        input("")
        print("The opposing team choose...")
        input("")
        print(rpsopposition)
        print(f"You Win!")
      if choice == "scissors" and rpsopposition == "paper":
        print("You Choose...")
        input("")
        print(choice)
        input("")
        print("The opposing team choose...")
        input("")
        print(rpsopposition)
        print(f"You Win!")
      if choice == "scissors" and rpsopposition == "rock":
        print("You Choose...")
        input("")
        print(choice)
        input("")
        print("The opposing team choose...")
        input("")
        print(rpsopposition)
        print(f"You Lose!")
      if choice == "rock" and rpsopposition == "paper":
        print("You Choose...")
        input("")
        print(choice)
        input("")
        print("The opposing team choose...")
        input("")
        print(rpsopposition)
        print(f"You Lose!")
      if choice == "paper" and rpsopposition == "scissors":
        print("You Choose...")
        input("")
        print(choice)
        input("")
        print("The opposing team choose...")
        input("")
        print(rpsopposition)
        print(f"You Lose!")
  if optiongame == "2":
    print("Welcome to the game downloader!")
    print("Please type the code of the game.")
    gamecode = input("Code: ")
    pass
  if optiongame == "3":
    print("Thank you for playing!")
    break
  else:
    print("Invalid option")
      
