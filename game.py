#These are the modules I am using
import time, sys
import os
from os import system, name

# Writing Choice For Typewriter Effect
def write(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.03)

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
    print("SORRY, THAT WAS AN INVALID ANSWER. TRY AGAIN.\n")
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
    print("SORRY, THAT WAS AN INVALID ANSWER. TRY AGAIN.\n")
    exit_game()

# Game after the intro (the ordering has to be like this so that the game can run)
def pick():
  choice_1 = input("Should you enter or not?\n")
  if choice_1.strip().lower() == "yes" or "enter":
    clear()
    print("\n\n\n\n\n\n\n\n\n")
    write("Did you know that there are approximately 8 million tonnes of plastic in the ocean.\n")
    write("That number continues to climb. Seeing all that plastic come in with the fish was the tip of the iceberg.\n")
    write("You contemplated this fact while walking into the pitch black cave.\n")
    write("Maybe something in my backpack could help me see.\n")
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
    print("SORRY, THAT WAS AN INVALID ANSWER. TRY AGAIN.\n")
    pick()

# This is the first path of the game
def path_1():
  write("There was a torch and a lighter, which do you choose?\n")
  torch_or_lighter = input()
  if torch_or_lighter.strip().lower() == "torch":
    clear()
    path_1_torch()
  elif torch_or_lighter.strip().lower() == "lighter":
    clear()
    path_1_lighter()
  else:
    clear()
    print("SORRY, THAT WAS AN INVALID ANSWER. TRY AGAIN.\n")
    path_1()

def path_1_torch():
  clear()
  print("""
    ▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓
  ▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓
  ▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓
  ▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓    
  ▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓    
  ▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒  ░░▒▒░░    ▒▒    
    ▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓▓▓▒▒▓▓▓▓                    
    ▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒▓▓                      
    ▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓                        
    ▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒                  ░░    
    ▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒                  ░░    
    ▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▒▒▓▓▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓                          
    ▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                          
    ░░▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒    ▓▓▓▓                    ░░    
      ▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓▓▓▒▒▒▒▓▓▓▓      ▓▓▒▒                    ▒▒    
      ▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓░░    ▓▓██▒▒                          
      ░░▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓      ░░  ▓▓                          
        ▓▓▓▓▓▓▓▓▒▒      ▓▓▓▓▒▒▓▓▒▒          ▓▓                          
        ▒▒██▓▓▓▓        ░░▓▓▓▓▓▓░░                                      
        ▒▒██▓▓▓▓          ▓▓▓▓▓▓                                        
        ▒▒████▓▓          ▒▒▓▓▒▒                                        
        ▒▒▓▓██▒▒          ▒▒▓▓░░                        ▒▒              
        ░░▒▒▓▓▓▓          ▒▒▓▓                          ░░              
              ▓▓          ▒▒▓▓                                          
              ▓▓            ▓▓                          ░░              
              ▓▓            ▓▓                                          
              ▒▒                          ░░                            
              ▓▓                                                        
""")
  write("You turn you light, it flashes on and off. You catch a glimpse of red blood painting the cave walls red.\n")
  write("Another flash and you see a swamp of dead fish in their own blood surrounded by plastics.\n")
  write("You think about why the world had to create such things, it makes life easier, but were they necessary?\n")
  write("You look at your torch and it finally turns on without flashing, you see a bloody path to the left and clean to the right.\n")
  write("Which do you choose?\n")
  left_or_right = input()
  if left_or_right.strip().lower() == "left":
    clear()
    torch_plastic_fight()
  elif left_or_right.strip().lower() == "right":
    clear()
    torch_mother_nature()
  elif left_or_right == "lol no im going straight":
    clear()
    print("Easter Egg")
  else:
    clear()
    print("SORRY, THAT WAS AN INVALID ANSWER. TRY AGAIN.\n")
    path_1_torch()

def torch_mother_nature():
  print("""
                ▓▓▒▒▒▒██▒▒▒▒▒▒▒▒              
          ▒▒▒▒▒▒▒▒██████▒▒▒▒██████          
        ████████▒▒▒▒████████▒▒████████        
      ▒▒████████████▒▒▒▒████▒▒▒▒▒▒████████      
    ▒▒▒▒██████████████▒▒▒▒▒▒▒▒▓▓▒▒██████████    
  ▓▓▒▒██████████████████▒▒▒▒▓▓▓▓▒▒████████▒▒▒▒  
  ▓▓▒▒████████████████████▒▒▓▓▓▓▒▒████▒▒▒▒▒▒██  
▓▓▒▒▒▒████████████████████▒▒▓▓▓▓▒▒▒▒▒▒▒▒████████
▓▓▒▒████████████████████▒▒▒▒▓▓▓▓▓▓▒▒▒▒██████████
▓▓▒▒██████████████████▒▒▒▒▓▓▓▓▓▓▓▓▒▒████████████
▓▓▒▒██████████████▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒████████████
▓▓▒▒████████████▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒████████████
▓▓▒▒██████████▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒████████████
▓▓▒▒▒▒██████▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒████████████
▓▓▓▓▒▒▒▒████████▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒████████████
  ▓▓▒▒██████████████▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒██████  
  ▓▓▒▒▒▒████████████████▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒████  
    ▓▓▒▒██████████████████▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒██    
      ▒▒▒▒████████████████▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒      
        ▒▒▒▒██████████████▒▒▓▓▓▓▓▓▓▓▓▓▓▓        
          ▒▒▒▒██████████▒▒▒▒▓▓▓▓▓▓▓▓▓▓          
                  ▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓              
  """)
  write("You go through a pitch black area, you see the smallest hint of light.\n")
  write("You see stars around you, you turn around and see the Earth.\n")
  write("You stare in awe.\n")
  write("It begins to talk.\n")
  write("I HAVE SEEN WHAT YOU PEOPLE HAVE BEEN DOING TO ME?\n")
  write("WHAT IS YOUR NAME?\n")
  name = input().strip()
  write(name.upper() + ", WHY HAVE YOU BEEN TRASHING MY PLANET?\n")
  write("WHAT DID I EVER DO TO YOU?\n")
  write("THE WORLD WILL BURN FOR THIS, MARK MY WORDS.\n")
  sys.exit

def torch_plastic_fight():
  print("""
          ████                    ██████      
      ██▒▒██                  ████▓▓██      
      ██▒▒██                  ██▒▒████      
      ██▒▒██                  ██▒▒████      
      ██▒▒██                ████▒▒████      
      ██▒▒░░██              ██░░▒▒████      
      ██▒▒░░██              ██░░▒▒██████    
      ██▒▒░░██              ██░░▒▒▒▒██████  
    ████▒▒░░██            ████░░▒▒▒▒██████  
    ████▒▒░░████        ████▓▓░░▒▒▒▒██████  
    ██▒▒▒▒░░██████████████▓▓▓▓░░░░▒▒████████
    ██▒▒░░░░▒▒░░░░▒▒▒▒▒▒▓▓▓▓░░░░░░▒▒▓▓██████
    ██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓██
  ████▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓██
  ████▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓██
  ██▒▒▒▒▒▒▒    ░░░░░░░░░░░░    ░░░▒▒▒▒▓▓▓▓██
  ████▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓████
    ██▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓██  
    ██▒▒░░▒▒ ▒▒░░░░░░░░░░ ░░░░░▒▒▒▒▒▒▓▓██  
    ██▒▒▒▒░░░  ░░░░░░░░  ░░░░░▒▒▒▒▒▒▓▓████  
    ████▒▒▒▒░░         ░░░▒▒▒▒▒▒▒▒▒▒▓▓██    
      ████▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒████    
        ██▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒████      
        ██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████        
            ██████████████████████          
  """)
  write("A plastic bag stares at you with a soulless smile.\n")
  write("DID YOU LIKE MY WORK OF ART?\n")
  write("I THINK THE RED REALLY MAKES THE CAVE POP?\n")
  write("MAYBE SOME OF YOURS CAN MAKE IT LOOK BETTER.\n")
  write("You begin stepping backwards slowly but trip over on a rock.\n")
  write("WHERE ARE YOU GOING?\n")
  write("Out of the bag emerges pipe and a phone. Which do you choose?\n")
  pipe_or_phone =  input()
  if pipe_or_phone.strip().lower() == "pipe": 
    clear()
    fight_pipe()
  elif pipe_or_phone.strip().lower() == "phone":
    clear()
    print("""
        ████                    ██████      
    ██▒▒██                  ████▓▓██      
    ██▒▒██                  ██▒▒████      
    ██▒▒██                  ██▒▒████      
    ██▒▒██                ████▒▒████      
    ██▒▒░░██              ██░░▒▒████      
    ██▒▒░░██              ██░░▒▒██████    
    ██▒▒░░██              ██░░▒▒▒▒██████  
  ████▒▒░░██            ████░░▒▒▒▒██████  
  ████▒▒░░████        ████▓▓░░▒▒▒▒██████  
  ██▒▒▒▒░░██████████████▓▓▓▓░░░░▒▒████████
  ██▒▒░░░░▒▒░░░░▒▒▒▒▒▒▓▓▓▓░░░░░░▒▒▓▓██████
  ██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓██
████▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓██
████▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓██
██▒▒▒▒▒▒▒    ░░░░░░░░░░░░    ░░░▒▒▒▒▓▓▓▓██
████▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓████
  ██▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓██  
  ██▒▒░░▒▒ ▒▒░░░░░░░░░░ ░░░░░▒▒▒▒▒▒▓▓██  
  ██▒▒▒▒░░░  ░░░░░░░░  ░░░░░▒▒▒▒▒▒▓▓████  
  ████▒▒▒▒░░         ░░░▒▒▒▒▒▒▒▒▒▒▓▓██    
    ████▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒████    
      ██▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒████      
      ██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████        
          ██████████████████████     
    """)
    write("Technology couldn't save you this time.")
    sys.exit
  else:
    clear()
    print("SORRY, THAT WAS AN INVALID ANSWER. TRY AGAIN.\n")
    torch_plastic_fight()

def fight_pipe():
  print("""
        ████                    ██████      
      ██▒▒██                  ████▓▓██      
      ██▒▒██                  ██▒▒████      
      ██▒▒██                  ██▒▒████      
      ██▒▒██                ████▒▒████      
      ██▒▒░░██              ██░░▒▒████      
      ██▒▒░░██              ██░░▒▒██████    
      ██▒▒░░██              ██░░▒▒▒▒██████  
    ████▒▒░░██            ████░░▒▒▒▒██████  
    ████▒▒░░████        ████▓▓░░▒▒▒▒██████  
    ██▒▒▒▒░░██████████████▓▓▓▓░░░░▒▒████████
    ██▒▒░░░░▒▒░░░░▒▒▒▒▒▒▓▓▓▓░░░░░░▒▒▓▓██████
    ██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓██
  ████▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓██
  ████▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓██
  ██▒▒▒▒▒▒▒▒░    ░░░░░░░░    ░░░░░▒▒▒▒▓▓▓▓██
  ████▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓████
    ██▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓██  
    ██▒▒░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓██  
    ██▒▒▒▒░░░░               ▒▒▒▒▒▒▓▓████  
    ████▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓██    
      ████▒▒  ░░░░░░░░░         ▒▒▒▒████    
        ██▒▒▒▒▒▒░░░░░░▒       ▒▒▒▒████      
        ██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████        
            ██████████████████████     
""")
  write("The pipe breaks in your hand, what is this plastic made of?")
  write("DID YOU JUST HIT ME WITH A PIPE?\n")
  write("NOW YOU'VE DONE IT. YOU PUT TWO HOLES IN ME.\n")
  write("COME ON HIT ME AGAIN.\n")
  write("I. DARE. YOU.\n")
  write("A pair of scissors and syringe fall out.\n")
  fight_2_choice()
  
def fight_2_choice():
  write("Do you use the scissors or the syringe?\n")
  fight_2 = input()
  if fight_2.strip().lower() == "scissors":
    clear()
    print("Final fight section")
    fight_scissors()
  elif fight_2.strip().lower() == "syringe":
    clear()
    print("Final fight section")
    fight_syringe()
  else:
    clear()
    print("SORRY, THAT WAS AN INVALID ANSWER. TRY AGAIN.\n")
    fight_pipe()

def fight_scissors():
  print("""
                              ██████      
                               ████▓▓██      
                              ██▒▒████      
                              ██▒▒████      
                            ████▒▒████      
                            ██░░▒▒████      
                            ██░░▒▒██████    
                            ██░░  ▒▒██████  
                          ████░░▒▒▒▒██████  
    ████▒▒░░████        ████▓▓░░▒▒▒▒██████  
    ██▒▒▒▒░░████████ ██████▓▓▓▓░░    ▒▒████████
    ██▒▒░░░░▒▒░░░░▒▒ ▒▒▒▒▓▓▓▓░░░░░░▒▒▓▓██████
    ██▒▒░░░░       ░ ░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓██
  ████▒▒▒▒░░░░░░░░░░ ░░       ░░░░░▒▒▒▒▓▓▓▓██
  ████▒▒▒▒▒▒░░░░░░░░░ ░░░░░░░░░░░░░▒▒▒▒▓▓▓▓██
  ██▒▒▒▒▒▒▒▒░    ░░░░░ ░░░    ░░░░░▒▒▒▒▓▓▓▓██
  ████▒▒▒▒▒▒▒▒░░░░░░░░░ ░░░░░░░░░░░▒▒▒▒▓▓████
    ██▒▒▒▒▒▒▒▒░░░░░░░░░░ ░░░░░░░░▒▒▒▒▒▒▓▓██  
    ██▒▒░░▒▒▒▒▒▒░░░░░░░░░ ░░░░░░░▒▒▒▒▒▒▓▓██  
    ██▒▒▒▒░░░░                ▒▒▒▒▒▒▓▓████  
    ████▒▒▒▒░░░░░░░░░░░░░░▒ ▒▒▒▒▒▒▒▒▒▓▓██    
      ████▒▒  ░░░░░░░░░          ▒▒▒▒████    
        ██▒▒▒▒▒▒░░░░░░▒        ▒▒▒▒████      
        ██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ▒▒████        
            ███████████████████ ███ 
  """)
  write("You defeated the plastic bag.")
  write("Trash spills out from within as the evil life it had seeps out.")
  write("A split through the middle.")
  write("You decide to pick the rubbish up and throw it in a nearby bin outside the cave.")
  write("Well that was a weird day.")
  sys.exit

def fight_syringe():
  print("""
          ████                    ██████      
      ██▒▒██                  ████▓▓██      
      ██▒▒██                  ██▒▒████      
      ██  ██                  ██▒▒████      
      ██▒▒██                      
      ██▒▒░░██              ██░░▒▒████      
                            ██░░▒▒██████    
      ██▒▒░░██              ██░░▒▒▒▒██████  
    ████▒▒░░██            ████░░▒▒▒▒██████  
    ████▒▒░░████        ████▓▓░░▒▒▒▒██████  
    ██▒▒▒▒░░██████████████▓▓▓▓░░░░▒▒████████
    ██▒▒░░░░▒▒░░░░▒▒▒▒▒▒▓▓▓▓░░░░░░▒▒▓▓██████
    █ ▒▒░░░░░    ░░░░    ░░░░░░░░░▒▒▓ ▓ ▓██
  ████▒▒▒▒░░░░   ░░░░    ░░░   ░░░▒▒▒▒▓▓▓▓██
  ████▒▒▒ ▒▒░░░░░░░░░░░░░░░░░░░░░  ▒▒▒▓ ▓▓██
  ██▒    ▒▒▒▒░    ░░░░░░░░    ░  ░░▒▒▒▒▓▓▓▓██
  ████▒▒▒▒▒▒▒▒░░░░░  ░░░░░░░░░ ░░░░▒▒ ▒▓ ████
    ██▒▒▒ ▒▒▒▒    ░░░░░░░    ░ ░░▒▒▒▒▒▒▓▓██  
    ██▒▒░░▒▒▒▒▒▒░░░░░░░░░░░░░░ ░▒▒▒▒▒▒▓▓██  
    ██▒▒▒▒░░░░               ▒ ▒▒▒▒▓▓████  
    ████▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓██    
      ████▒▒  ░░░    ░░         ▒▒▒▒████    
        ██▒▒▒▒▒▒░    ░▒       ▒▒▒▒████      
        ██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████        
            ██████████████████████ 
  """)
  write("Trash spilling out from the holes made by the syringe.")
  write("You didn't know when to stop so you kept on stabbing.")
  write("The bag then collapses.")
  write("What a day. You fought a plastic bag.")
  write("Who's stupid idea was to add this to this world.")
  sys.exit

def path_1_lighter():
  print("""
  █████████████████████████████████▓▓██████████████████
  ███████████████████████████████▓▓▒▒██████████████████
  ███████████████████████████████▒▒▒▒▓▓████████████████
  █████████████████████████████▓▓▒▒  ▓▓████████████████
  █████████████████████████████▓▓▒▒  ▓▓████████████████
  █████████████████████████████▓▓▒▒  ▓▓████████████████
  █████████████████████████████▓▓▒▒  ▓▓████████████████
  █████████████████████████████▒▒▒▒░░▒▒████████████████
  █████████████████████▓▓██████▒▒░░░░▒▒████████████████
  ███████████████████████████▓▓░░  ▒▒▓▓████████████████
  ███████████████████▓▓▓▓██▓▓▒▒░░  ░░██████████████████
  ███████████████████▓▓▒▒██▓▓▒▒░░░░▒▒▓▓████████████████
  █████████████████▓▓▒▒▒▒██▒▒▒▒  ░░▓▓▓▓████████████████
  █████████████████▒▒▒▒▓▓██▒▒░░    ▒▒▓▓████████████████
  ███████████████▓▓▒▒░░▒▒▓▓░░░░    ░░▓▓████████████████
  ███████████████▒▒░░░░░░▒▒░░    ░░░░▓▓████████████████
  █████████████▓▓░░░░░░▒▒░░░░    ░░░░▓▓████████████████
  █████████████▓▓░░  ░░▒▒░░░░    ░░░░▒▒████████████████
  ███████████▓▓▒▒░░  ░░▒▒  ░░    ░░░░▒▒████████████████
  ███████████▓▓░░      ░░  ░░    ░░░░▓▓████████████████
  ███████████▒▒░░      ░░  ░░    ░░░░▓▓████████████████
  ███████████▒▒░░      ░░  ░░    ░░░░▓▓████████████████
  ███████▓▓██▓▓░░      ░░░░      ░░░░▒▒████████████████
  ███████▓▓▒▒██░░        ░░      ▒▒░░▒▒██▓▓▓▓██████████
  █████████▓▓░░░░        ░░      ░░░░▒▒▒▒░░████████████
  █████████▓▓░░░░░░                ░░░░░░▒▒████████████
  ███████████▒▒░░░░          ░░░░░░░░░░▒▒██████████████
  █████████████░░▒▒▒▒▒▒▒▒░░  ░░░░▒▒▓▓██████████████████
  █████████████▓▓▓▓████████░░░░▒▒▓▓████████████████████
  █████████████████████████▓▓██████████████████████████
  """)
  write("You drop the lighter, a small spark of light showing the blood before it disappears.\n")
  write("A slow burning smell creeps up on you.\n")
  write("The whispers of the burning begins to burn your eyes.\n")
  write("Following the smell could lead somewhere, but escaping would be a better idea.\n")
  write("Should you escape or follow?\n")
  escape_or_follow = input()
  if escape_or_follow.lower().strip() == "escape":
    clear()
    lighter_escape()
  elif escape_or_follow.lower().strip() == "follow":
    clear()
    lighter_follow()
  else:
    clear()
    print("SORRY, THAT WAS AN INVALID ANSWER. TRY AGAIN.\n")
    path_1_lighter()

def lighter_escape():
  print("""                                                     
                                          ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓██      
                                      ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████    
                                    ██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓████  
                                  ██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
                                ▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▒▒██
                              ██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██      ▓▓██
                            ██▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░██            
                          ██▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░██              
                        ██▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░██              
                      ██▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░██                
                    ██▓▓▒▒▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░██                
                  ██▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░██                  
                ██▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░████                  
            ▓▓██▓▓▒▒▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░██                    
        ▓▓▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░██▓▓                  
    ▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░████▓▓                
████▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████ \n""")
  write("You slowly make your way towards the entrance.\n")
  write("Holding the cave walls to stay upright.\n")
  write("A rumble in the ground pushes you over, a wave nearing you through the entrance.\n")
  write("A wave to end the cave, maybe exploring would've been a better plan.\n")
  sys.exit

def lighter_follow():
  print("""
                              ▒▒▓▓▓▓████▓▓▓▓                            
                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                        
                      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                      
                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                    
                  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                  
                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░                
                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                
              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                
              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██              
              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓              
            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓              
            ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            
            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██            
            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒          
          ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██          
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          
        ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        
        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██        
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██        
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      
      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██      
      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      
      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      
      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  
  """)
  write("You enter a massive area in the cave, it's dark and damp.\n")
  write("You see a pile of dead corpses of dead sea animals that floated from around the world.\n")
  write("They pile together in a tombstone-like shape that reaches saddening heights.\n")
  write("You see a trail of plastic can holders, plastic bags and plastic bottles.\n")
  write("Which do you choose?\n")
  plastic_choice =  input()
  if plastic_choice().strip().lower() == "plasticcanholders":
    clear()
    penguin()
  elif plastic_choice().strip().lower() == "plasticbags":
    clear()
    seagull()
  elif plastic_choice().strip().lower() == "plasticbottles":
    clear()
    seal()
  else:
    clear()
    print("SORRY, THAT WAS AN INVALID ANSWER. TRY AGAIN.\n")
    lighter_follow()

def penguin():
  clear()
  print("\n\n\n\n\n\n\n\n\n")
  write("Every year, so many penguins die from being choked by a plastic can holder.\n")
  write("They wrap around an innocent penguins neck until they stop breathing.\n")
  write("Humans are responsible for this.\n")
  write("You look at the body of the penguin. Wondering what you could have done.\n")
  input("Press Enter to continue...")
  the_final_choice()

def seagull():
  clear()
  print("\n\n\n\n\n\n\n\n\n")
  write("Every year, so many seagulls die from plastic bags stopping their air flow.\n")
  write("They think that the plastic bags are food, but that gets caught in their throat.\n")
  write("We all could have helped this animal just by recycling.\n")
  input("Press Enter to continue...")
  the_final_choice()

def seal():
  clear()
  print("\n\n\n\n\n\n\n\n\n")
  write("Every year, so many seals die from consuming the remnants of plastic bottles.\n")
  write("The shards are eaten by the seal and they begin to intoxicate its body.\n")
  write("Recycling could've helped this animal.\n")
  input("Press Enter to continue...")
  the_final_choice()

def the_final_choice():
  helping = input("\n\nAre you willing to help the world to get rid of unnecessary plastics?")
  if helping.strip().lower() == "yes":
    clear()
    write("Good job, go out there and save the world!")
    sys.exit
  elif helping.strip().lower() == "no":
    clear()
    write("Well, feels bad. The world really need your help.")
    sys.exit
  else:
    clear()
    print("SORRY, THAT WAS AN INVALID ANSWER. TRY AGAIN.\n")
    the_final_choice()

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
    clear()
    how_to_play()
  elif game_choice.lower().strip() == "q":
    exit_game()
  else:
    clear()
    print("Sorry, but you entered an invalid choice \n              Try Again.".upper())
    main_menu()

# The call for the main menu function so that the game can begin.
main_menu()