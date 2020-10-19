#These are the modules I am using
import time, sys
import os
from os import system, name

# The Typewriter Effect
def write(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.01)

# A clear function for windows and linux using os
def clear():
  #windows
  if name == 'nt':
    _ =  system('cls')
  #linux, mac
  else:
    _ = system('clear')

# The how to play section of the menu
def how_to_play():
  clear()
  print("This a story-based game where choice is the main way to play.\n")
  print("""There may be choices like: (There is a cave in front of you, exploring it could continue 
  your journey but this might be a good time to give up. What do you do?)
  You need to look at key words like 'explore' and 'give up'. Then type them into the game.\n""")
  menu_choice = input("Press E to Exit to the main menu.")
  if menu_choice.lower().strip() == "e":
    clear()
    main_menu()
  else:
    clear()
    print("Sorry, but you entered an invalid choice \n              Try Again.".upper())
    how_to_play()

# The quit button for the menu
def exit_game():
  exit_choice = input("Are you sure you want to exit the game? \nYes or No? \n")
  if exit_choice.lower().strip() == "yes":
    sys.exit
  elif exit_choice.lower().strip() == "no":
    clear()
    main_menu()
  else:
    print("Sorry, but you entered an invalid choice \n              Try Again.".upper())
    exit_game()

# Choice to play the game or not
def pick():
  choice_1 = input("Should you enter or not?\n")
  if choice_1.strip().lower() == "yes" or "enter":
    clear()
    print("\n\n\n\n\n\n\n\n\n")
    write("Did you know that there are approximately 8 million tonnes of plastic in the ocean.\n")
    write("That number continues to climb. Seeing all that plastic come in with the fish was the tip of the iceberg.\n")
    write("You contemplated this fact while walking into the pitch black cave.\n")
    write("Maybe something in my backpack could help me out.\n")
    path_1()
  elif choice_1.strip().lower() == "no":
    clear()
    print("""
    ██████████████████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████████████████
    ████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████████████
    ██████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓████████████████
    ████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████
    ██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████
    ████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████
    ██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░    ░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓
    ████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░              ░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓
    ████████████████████████▓▓▓▓▓▓▒▒░░░░    ░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒
    ██████████████████████████▓▓▓▓▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▓▓▓▓▓▓████████▓▓▓▓██████████
    ████████████████████████▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓████████████████████████
    ████████████████████████████▓▓▓▓▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓██████████████████████████
    ██████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████████████████
    ██████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████████████
    ██████████████████████████████████▓▓▓▓▓▓▓▓████████████████████████████████
    ██████████████████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████████████████
  """)
    write("You thought that you had enough adventure for the day.\n")
    write("And so the adventure concludes abruptly and early.\n")
    write("The beautiful sunset is good enough.\n")
    write("Maybe you could have done something spectacular today.\n")
  else:
    print("Sorry that was an invalid answer. Try again.")
    pick()

# This is the first path of the game
def path_1():
  write("There was a torch and a lighter, which do you choose?\n")
  torch_or_lighter = input()
  if torch_or_lighter.strip().lower() == "torch":
    print("""
    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓██▓▓▓▓▓▓██████████
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▒▒▒▒▓▓▒▒░░░░▒▒▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████▓▓██▓▓█████████████████
    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▒▒▒▒░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓████████▓▓▓▓▓▓██▓▓█████████████████
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓██▓▓▓▓████▓▓██▓▓▓▓▓▓████████████████
    ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒░░░░░░░░░░▒▒░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓████▓▓▓▓██████▓▓██████▓▓▓▓▓▓▓▓███████████
    ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░▒▒░░░░░░  ░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓██████████████▓▓████▓▓██▓▓██▓▓▓▓█████████████████
    ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████▓▓░░░░░░▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓██████████████▓▓███████
    ██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▓▓▓▓██▓▓▓▓▓▓██▓▓████▓▓▓▓▓▓▓▓▓▓██████▓▓██▓▓▓▓██████████▓▓▓▓████
    ██████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██░░  ░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▓▓██▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓▓▓██▓▓████▓▓▓▓▓▓████████▓█
    ████████▓▓██▓▓██▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░  ░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒████████████████████▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓████▓▓▓▓▓▓██▓▓██▓█
    ▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓▒▒░░░░    ░░          ░░░░░░░░░░░░░░░░░░          ░░▒▒▓▓██████████▓▓██████▓▓▓▓▓▓▓▓██▓▓██████▓▓███████
    ██▓▓██████████▓▓▓▓▓▓██▓▓▓▓██████▓▓▓▓▓▓▓▓░░                ░░  ░░░░░░░░░░░░░░░░░░    ░░░░░░░░░░░░▒▒▒▒▓▓▓▓████████████████████████▓▓████▓▓▓▓██
    ██████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████▓▓▒▒░░                  ░░        ░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░▒▒▒▒▓▓██████████▓▓██████████████████
    ██████████▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▒▒░░░░              ░░░░░░░░  ░░░░░░░░░░░░░░░░░░▒▒░░░░▒▒░░▒▒░░░░░░░░░░░░▒▒▓▓████████████████████████████
    ████████▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓░░░░░░                ░░░░░░░░░░░░░░░░░░      ░░░░  ░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓██████████████████████████
    ▓▓▓▓▓▓▓▓██▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░  ░░░░          ░░░░░░░░░░░░░░░░  ░░  ░░░░    ░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓██████████████████████████
    ▓▓▓██▓▓██▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░        ░░░░░░▒▒░░░░░░▒▒░░░░░░░░          ░░      ░░░░░░▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓███████████████████████
    ▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░          ░░░░░░░░  ░░░░░░░░            ░░      ░░░░░░▒▒▒▒░░░░░░░░░░▓▓▓▓█████████████████████
    ▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▒▒░░░░░░░░░░░░░░░░░░                                            ░░░░░░░░░░░░░░░░░░▒▒░░░░░░▒▒▒▒▒▒█████████████████
    ███▓▓████▓▓██▓▓▓▓▓▓██████▓▓▒▒░░▒▒░░░░░░░░                                      ░░░░░░    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓███████████████
    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▒▒▒▒▒▒▒▒▒▒░░░░                            ░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░▒▒▒▒▒▒░░▒▒░░▒▒░░░░▒▒░░▒▒▒▒▒▒▒▒▓▓████████████
    ▓▓▓▓▓▓▓██▓▓▓▓████████▓▓▒▒▒▒▒▒░░░░░░                          ░░░░░░░░░░▒▒▒▒▒▒░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░▒▒▓▓▓▓▓▓▓▓█████████
    ▓██▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓▒▒▒▒▒▒▒▒░░░░░░                    ░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░░░▓▓▓▓▓▓▓▓▓▓███████
    ▓▓▓▓██▓▓▓▓▓▓██████▒▒▒▒▒▒░░▒▒▒▒▒▒░░░░░░░░░░░░░░                ░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓██
    ██▓▓██▓▓▓▓██████▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░                    ░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒██
    ████▓▓▓▓████████▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░                ░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
    ████▓▓▓▓████████▓▓▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░░░░░░░                        ░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░                    ░░░░▒▒░░▒▒▒▒▒▒▓▓▓▓▒▒▒▒░░
    ▓▓▓▓▓▓▓▓██████▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░                          ░░░░░░              ░░░░                  ░░░░░░░░░░░░▒▒▒▒░░▒▒▒▒░░░░
    ███▓▓▓▓██▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░▒▒░░░░░░░░░░░░            ░░                              ░░  ░░░░░░░░░░              ░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░░░░░░░░░                              ░░      ░░░░░░░░░░░░░░░░░░░░      ░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ██▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░                                  ░░░░░░░░░░░░░░░░░░░░░░  ░░  ░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒
    ████████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░                                ░░░░░░░░░░  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ██▓▓██▓▓▒▒▓▓▒▒▒▒▒▒░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░                                ░░    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒
    ██▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒░░▒▒░░░░  ░░░░░░░░░░░░░░                        ░░              ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒
    ██▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░░░░░░░                          ░░      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒
    """)
    path_1_torch()
    print("see a river of plastics leading to something.")
  elif torch_or_lighter.strip().lower() == "lighter":
    print("""
    ████████████████████████▓▓████████████████████████████
    ██████████████████████████████████████████████████████
    ████████████████████████▓▓████████▒▒▓▓████████████████
    ████████████████████████▓▓▓▓██████▓▓▒▒▒▒██████████████
    ████████████████████████▓▓▓▓░░████▓▓░░░░▓▓████████████
    ████████████████████████▒▒░░▒▒████▒▒▒▒░░▒▒████████████
    ██████████████████████▓▓░░░░░░▒▒▒▒▓▓▓▓██▒▒████████████
    ████████████████████▓▓░░▒▒░░░░▒▒▓▓▓▓▒▒██▒▒████████████
    ██████████████████████░░░░░░░░▓▓▓▓▒▒▒▒▓▓▒▒▒▒▓▓▒▒██████
    ████████████████████▓▓▒▒▒▒▒▒░░▒▒░░░░▓▓▒▒░░░░▒▒████████
    ████████████████████▓▓▓▓▒▒▒▒░░▓▓▒▒▓▓▒▒░░░░▒▒██████████
    ████████████████████▓▓▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░▒▒████████████
    ██████████████████▓▓░░░░░░▒▒░░▒▒▒▒░░░░░░▒▒████████████
    ████████████████▓▓▒▒▒▒░░░░▒▒░░▒▒▒▒▒▒░░▒▒▓▓░░▓▓████████
    ████████████████▒▒▒▒▓▓░░▒▒░░▒▒▒▒░░▒▒░░████▓▓██████████
    ██████████████▓▓▒▒▓▓▒▒▒▒▒▒░░▒▒▓▓░░░░▒▒▒▒▒▒████████████
    ████████████████▒▒▒▒░░░░▒▒░░▓▓░░░░▒▒░░░░▒▒████████████
    ████████████████▓▓░░░░▒▒▒▒░░▒▒░░░░▒▒░░▒▒▓▓██▓▓▒▒██████
    ████████████████░░░░░░▓▓▒▒░░░░░░░░▓▓▒▒▒▒▒▒██▓▓░░▓▓████
    ██████████████▓▓░░░░▒▒▒▒░░░░░░░░░░██▒▒░░▒▒████▒▒▒▒████
    ██████▓▓██▒▒▓▓▒▒░░░░░░▒▒░░░░░░░░  ██▓▓░░░░████░░▓▓████
    ██████▓▓░░▒▒▒▒▓▓░░░░░░░░░░░░░░░░░░██▒▒░░▓▓██▓▓  ██████
    ██████▒▒░░▒▒▒▒██░░░░░░░░░░▒▒░░░░▒▒▓▓░░▓▓░░▒▒░░░░▓▓████
    ██████░░  ░░░░▒▒░░  ▒▒    ░░▒▒░░░░▒▒▒▒▒▒▓▓░░  ░░▓▓████
    ██████    ░░  ▒▒░░░░░░▓▓░░▒▒░░▓▓▒▒░░▒▒▒▒▒▒  ░░░░▒▒████
    ██▓▓▒▒    ░░░░  ▓▓▓▓▒▒▓▓░░▓▓▒▒▓▓▓▓▒▒▓▓▒▒░░░░░░░░░░▒▒██
    ██▒▒░░  ░░    ▒▒████████▓▓██▓▓██▓▓▓▓▓▓▓▓▒▒░░░░      ▓▓
    ██▓▓░░░░░░░░░░▓▓██▓▓████████████████░░▓▓░░▒▒▒▒  ░░░░▒▒
    ██▓▓▒▒▒▒██▓▓▓▓▒▒▓▓▓▓▒▒██████████████▒▒██▓▓▒▒▓▓  ▒▒░░██
    ██▒▒▓▓██████░░▓▓▒▒██░░██████████████▓▓██▒▒▒▒▓▓▒▒░░████
    ████████████▓▓▓▓▒▒▓▓▒▒▓▓████████████▓▓██▓▓██▒▒▒▒▒▒████
    """)
    print('burn plastics that begin burning the water')
    path_1_lighter()
  else:
    clear()
    print("Sorry, you pressed an invalid value. Try again.\n")
    path_1()


# This is the intro to the game which includes it's first choice
def play_game():
  print("""
          ██████            ██████████                                                          
      ██▓▓░░░░████    ████░░░░░░░░░░████                                                      
      ██  ▓▓░░▒▒▒▒▓▓▓▓▒▒▒▒▒▒░░░░░░░░▒▒▒▒▓▓██                                                  
      ░░██░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░▒▒▒▒░░░░░░██                                                
          ▓▓  ▓▓▓▓▒▒▒▒░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒                                              
            ██      ▒▒▒▒░░▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒                                              
              ▓▓      ░░░░░░░░░░░░░░░░░░░░░░░░▒▒████                                          
                ██      ░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒████                                      
                ██        ░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓████                                  
                  ▓▓        ▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░▒▒▒▒▓▓████                            
                    ██      ▒▒░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░▒▒▒▒▒▒██▓▓                        
        ▒▒▒▒          ▓▓    ██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓██                    
        ▒▒░░▒▒          ██  ██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░██                  
          ▒▒▒▒            ████▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                
                            ██░░░░░░░░▒▒    ▒▒░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░██              
                              ▓▓░░░░░░░░      ░░░░░░░░░░░░░░░░░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒▓▓            
                              ██░░▒▒░░▒▒██    ░░░░░░░░░░░░░░░░░░░░████████████████            
                                ██░░░░░░████    ▒▒░░░░░░░░░░░░░░▒▒██                          
                                ██▒▒▒▒▒▒██  ██    ▒▒░░░░░░░░░░░░░░██            ▒▒▒▒          
                  ▒▒▒▒            ██░░▒▒██    ██  ▒▒░░░░░░░░░░░░░░██          ▒▒░░▒▒          
                  ▒▒░░▒▒            ██▒▒██          ▒▒░░░░░░░░░░░░██          ▒▒▒▒            
                    ▒▒▒▒              ████      ██  ░░░░░░░░░░░░▒▒██                          
                            ▒▒▒▒                  ██  ░░░░░░▒▒▒▒░░██    ▒▒▒▒                  
                        ░░░░▒▒░░▒▒    ░░░░▒▒▒▒░░▒▒▓▓░░▒▒▒▒▒▒▒▒▒▒▒▒██  ▒▒░░▒▒                  
                        ░░  ░░▒▒░░▒▒░░    ▒▒░░▒▒▒▒░░██  ▒▒░░▒▒▒▒▒▒██▒▒░░▒▒                    
                        ▒▒▒▒                ▒▒░░░░░░░░██  ░░▒▒░░▒▒██░░░░▒▒                    
                        ▒▒░░▒▒              ▒▒░░░░░░░░░░██  ▒▒░░░░██░░░░▒▒                    
                                  ▒▒      ▒▒░░░░░░▒▒░░▒▒░░██  ░░░░▒▒██░░░░▒▒    ▒▒▒▒          
                                ▒▒░░▒▒  ▒▒░░░░░░▒▒░░▒▒░░░░░░██  ░░▒▒██░░░░░░▒▒  ▒▒░░▒▒        
                              ▒▒░░░░░░▒▒░░░░░░░░▒▒░░▒▒░░░░░░██  ▒▒▒▒██▒▒░░░░░░▒▒░░░░░░▒▒    ▒▒
                            ▒▒░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░▒▒██░░▒▒██░░▒▒░░░░░░░░░░░░░░▒▒▒▒░░
          ▒▒▒▒            ▒▒░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░██░░▒▒██░░░░▒▒░░░░░░░░░░░░░░░░░░
        ▒▒░░░░▒▒▒▒      ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░▒▒████░░░░▒▒░░░░▒▒░░░░░░░░░░
  ▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒░░░░░░▒▒░░░░░░░░░░▓▓▒▒▒▒░░░░▒▒░░▓▓▓▓░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒░░░░░░▒▒░░░░░░░░██░░░░▒▒▒▒░░▒▒░░▒▒▒▒██▒▒░░░░░░▒▒▒▒░░░░
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒░░░░▒▒░░░░░░░░██░░░░▒▒▒▒░░▒▒▒▒░░▒▒▒▒░░██░░░░░░░░░░░░░░
  ░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░▒▒░░░░▒▒░░▒▒░░░░░░░░██▒▒▒▒▒▒░░░░▒▒▒▒░░▒▒░░▒▒░░██░░░░░░░░░░▒▒░░         
  """)
  time.sleep(1)
  write("You are near the sea; standing atop the rocks.\n")
  write("A beautiful dolphin jumps out from the ocean horizon. Casting it's silhouette across the sun.\n")
  write("But, soon after, a flow of plastic floods towards your shoes.\n")
  write("Followed by the plastic-filled bodies of dead fish.\n")
  write("A shocking realisation of what our world has become.\n")
  input("Press Enter to continue...")
  clear()
  print("""
  ██████████████████████████▒▒████████████████████████████████████████▓▓█████████████████████████████████████████
  ████████████████████████▓▓    ░░  ░░░░▒▒██░░▓▓▓▓██▒▒░░░░  ░░░░          ░░▒▒▒▒▓▓███████████████████████████████
  ████████████████████▓▓▓▓▓▓░░                                            ░░░░░░░░░░▒▒▒▒▓▓███████████████████████
  ██████████████████▓▓▓▓▓▓▒▒░░                                          ░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓█████████████████
  ████████████████▓▓▓▓▓▓▓▓▒▒░░                                        ░░▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓█████████
  ████████████████▓▓▓▓▓▓▒▒▒▒░░░░░░                                    ░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓█████████
  ██████████████▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░░░                              ░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░▒▒▒▒▒▒▓▓██▓▓█████
  ████████████▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░                      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓█████
  ████████████▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓█████
  ██████████▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓█████
  ████████▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓███
  ████████▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓█
  ████▓▓██▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓█
  ████▓▓██▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓█
  ██▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓█
  ██████▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓
  ██████▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
  ████████▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  ▓▓████████▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  ▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓
  ▓▓██████▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓
  ▓▓████████▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓█
  ▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓
  ██████▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓█
  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
  ██▒▒▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▒▒▒▒░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓█
  ▓▓████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███
  ██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▒▒░░▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████
  """)
  write("You stand on those rocks, thinking about what the world has come to.\n")
  write("While you gaze across the horizon, a cave near the sea attracts your attention.\n")
  pick()


# This is the introduction of the game and comes prior to the main menu
print("*-------------------------------------------*\n")
print("Welcome to your journey about plastic.")
print("Throughout this game you will learn about the effects plastic has in us. ")
print("This is a choose your own adventure game where your choice can change the outcomes of the story.")
print("Have fun. \n")

# The main menu set up
def main_menu():
  print("*--------------------- Main Menu ----------------------*")
  game_choice = input("""
  A: Play Game
  B: How To Play
  Q: Exit Game

  Please Make Your Choice To Continue
  """)

  if game_choice.lower().strip() == "a":
    clear()
    play_game()
  elif game_choice.lower().strip() == "b":
    how_to_play()
  elif game_choice.lower().strip() == "q":
    exit_game()
  else:
    clear()
    print("Sorry, but you entered an invalid choice \n              Try Again.".upper())
    main_menu()

# The call for the main menu function so taht the game can begin.
main_menu()