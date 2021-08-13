import time
import sys

####_____Classes_____####
class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer
#_______________________#


####_____Questions_____####
question_prompts = [
     "What color are apples?\n(a) Red/Green\n(b)Orange\n",
     "What color are bananas?\n(a) Red/Green\n(b)Yellow\n",
]

questions = [
     Question(question_prompts[1], "a"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
]
#_______________________#


name = input ("What's your name? ")  # Stores the Users Name


def welcome():              # Welcome function that'll ask for user name
    global name             # Stores this in Variable defined at top
    print(f"\nWelcome to the game", name, "\nPlease choose from an option below\n") # Welcome whoever you are
    time.sleep(1)           # Pauses for 1 second and shows next message
    menu()                  # Menu Function

def menu():
    print("Option1")        # Shows user 3 options to choose from
    print("Option2")
    print("Option3")    

    while True:             # Makes sure the user can only enter an Integer, anything else returns an error
            try:
                option = int(input("\nWhich is your favourite?\n")) # Asks the user this quest and awaits input
                break
            except:
                print("That's not a valid option!")     # If user does not enter Integer do this
    if option == 1:
            print("\nOption1 chosen\n\n")
            time.sleep(0.5)       # IF this option is chosen do something
            first_room(questions)
    elif option == 2:
            print("\nOption2 chosen\n\n")
    elif option == 3:
            print("\nOption3 chosen\n\n")
            time.sleep(1)
    elif option >= 4:
            print("\nError please try again\n") 
            time.sleep(0.5)
            menu()
    else: #option == str(input()):                # If the user enters something other than INT do this
        print("\nError please try again")  
        time.sleep(0.5)
        menu()  
   
def exit():
    print("\nThank you for playing today", name)
    time.sleep(1)       #Makes the system wait 1 second before we continue
    print("\nHave a nice day!")
    sys.exit()          #Closes the program



#####_____Try Again_____#####
# We use this function when the user needs to restart for whatever reason
# Example - They take a wrong turn and die
def try_again():
        t_option = input()
        while True:
                try:
                        t_option = t_option.lower(("\nTry Again?\n"))
                        break
                except:
                        print("\nWrong option do it again!\n")
        if t_option == "y":
                welcome()
        elif t_option =="n":
                sys.ext()
        else:
                print("Wrong option")
#_______________________#


####_____ ONE VERSION OF DOING THIS____####
# NOt sure how to prevent user input from wrong and skipping to next question
def first_room(questions):
     i = 0
     #________     
     for question in questions:
          answer = input(question.prompt)   # Stores the user answer as 'answer'
          if answer == question.answer:
               i += 1
          else:
                print("incorrect input")
        #   if answer != input(str()):
        #            print("Nope try again")
        #            i == 0
        #            break
        #   else:
        #           return Choice1()

#      print("you got", i, "out of", len(questions))

#      if i >= 3:
#              print("\nSuccess!!!\n Move onto the next room")
#      else:               
#               time.sleep(0.5)
#               try_again()

def first_rooma():
    
    
    
    print("")


welcome()   

