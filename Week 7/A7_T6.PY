import random
random.seed(1234)

NAMES = ("rock", "paper", "scissors")
ART = (r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
LINE = "#" * 25
BOT = "RPS-3PO"

print("Program starting.")
print("Welcome to the rock-paper-scissors game!")
name = input("Insert player name: ")
print(f"Welcome {name}!")
print(f"Your opponent is {BOT}.")
print("Game starts...")
wins = losses = draws = 0
while True:
    print("\nOptions:\n1 - Rock\n2 - Paper\n3 - Scissors\n0 - Quit game")
    try:
        choice = int(input("Your choice: "))
    except ValueError:
        print("Please enter a number.")
        continue
    if choice == 0:
        break
    if choice not in (1, 2, 3):
        print("Invalid choice.")
        continue
    bot = random.randint(1, 3)
    print("Rock! Paper! Scissors! Shoot!\n")
    print(LINE)
    print(f"{name} chose {NAMES[choice - 1]}.")
    print(ART[choice - 1])
    print(LINE)
    print(f"{BOT} chose {NAMES[bot - 1]}.")
    print(ART[bot - 1])
    print(LINE)
    print()
    if choice == bot:
        print(f"Draw! Both players chose {NAMES[choice - 1]}.")
        draws += 1
    elif (choice - bot) % 3 == 1:
        print(f"{name} {NAMES[choice - 1]} beats {BOT} {NAMES[bot - 1]}.")
        wins += 1
    else:
        print(f"{BOT} {NAMES[bot - 1]} beats {name} {NAMES[choice - 1]}.")
        losses += 1
print("\nResults:")
print(f"{name} - wins ({wins}), losses ({losses}), draws ({draws})")
print(f"{BOT} - wins ({losses}), losses ({wins}), draws ({draws})")
print("\nProgram ending.")