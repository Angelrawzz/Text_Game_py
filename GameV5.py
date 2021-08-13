import time
import sys

#####_____Variables_____#####
name = "" # Updated with name = input
#_______________________#

#####_____Quiz List_____#####
my_quiz = {
    1 : {
        "question" : "A detective who was mere days from cracking an international smuggling ring has suddenly gone missing \nWhile inspecting his last-known location, you find a note: '710 57735 34 5508 51 7718'" 
                     "\nCurrently there are 3 suspects: Bill, John, and Todd. \n\nCan you break the detective’s code and find the criminal’s name?",
        "answer" : "Bill"                                   # Bill. If you read the message upside down, you’ll notice that the numbers resemble letters and that those letters form legible sentences. The message is "Bill is boss. He sells oil."
    },
    2 : {
        "question" : "\nImagine that you have been captured by an enemy. You are to be killed," 
                     "\nBut in a moment of mercy, the enemyt has allowed you to pick your own demise."
                     "\nYour first choice is to be drowned in a lake of acid" 
                     "\nYour second choice is to be burned on a fire"
                     "\nYour third choice is to be thrown to a pack of wolves that have not been fed in over a month"
                     "\nYour final choice of fate is to be thrown from the walls of a castle, many hundreds of feet high."
                     "\n\nWhat fate would you be wise to choose?"
                     "(Type 1, 2, 3 or 4 for a decision on your fate",
        "answer" : "3" #Being fed to the wolves - wolves cannot survive for 30 days without food, because they would all be dead
    },
    3 : {
        "question" : "\nA renowned chemist is found dead in his lab. There is no clear evidence except a piece of paper"
                     "\nThe paper is blank other than the name of five elements scrawled accross it hastily"
                     "\nNickel\nCarbon\nOxygen\nLanthanum\nSulfur"
                     "\nThe guard reported that three people visited the chemist that day"
                     "\nHis sister, LAURA; his collegue, NICOLAS; and his wife TESSA."
                     "\n\nThe Criminal was arrested immediately. Who was it?",
        "answer" : "nicolas"
     }
} ### Stores the questions and answers for the mystery quiz

m_quiz = {
    1 : {
        "question" : "What is the most popular lucky number?", # What could we ask I wonder ??? :)
        "answer" : "7"                                   # Change this for the answer
    },
    2 : {
        "question" : "What is 5 squared?",
        "answer" : "25"
    },
    3 : {
        "question" : "What is (10 + 20 + 30 / 5) x 0 ?\nIs it: |  30  |  0  |  60  |  100  |",
        "answer" : "0"
    }, 
     4 : {
         "question" : "Look at this sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...\n What comes after 34?",
         "answer" : "55"
    }
} ### Stores the questions and answers for the maths quiz

#_______________________#



def welcome():              # Welcome function that'll ask for user name
    #print("\nHello...What's your name?\n")
    #name = input # Updates the Users name
    time.sleep(1)
    print(f"\nYou awake in a dimly lit and smelly room\n")
    time.sleep(0.5)
    print(f"\nRubbing your eyes your sight becomes clearer, a door is in front of you and some words over the top of it...\n") # Welcome 
    print(f"                                                                                  )                              )                                                                            )                      ")
    print(f"   (          )                   (                        (       (    (      ( /(                           ( /(            (  (         )                            )                  ( /(                      ")
    print(f"   )\      ( /(      )            )\ )                     )\      )\   )\     )\())                  (       )\())    (      )\))(   ' ( /(           (             ( /(     (    (       )\())    (    (       (   ")
    print(f"((((_)(    )\())  ( /(    (      (()/(    (     (       ((((_)(   ((_) ((_)   ((_)\    (    `  )     ))\     ((_)\    ))\    ((_)()\ )  )\())   (      )\     (      )\())   ))\   )(     ((_)\    ))\   )(     ))\  ")
    print(f" )\ _ )\  ((_)\   )(_))   )\ )    ((_))   )\    )\ )     )\ _ )\   _    _      _((_)   )\   /(/(    /((_)   __ ((_)  /((_)   _(())\_)()((_)\    )\    ((_)    )\ )  (_))/   /((_) (()\     _((_)  /((_) (()\   /((_) ")
    print(f" (_)_\(_) | |(_) ((_)_   _(_/(    _| |   ((_)  _(_/(     (_)_\(_) | |  | |    | || |  ((_) ((_)_\  (_))     \ \ / / (_))     \ \((_)/ /| |(_)  ((_)   | __|  _(_/(  | |_   (_))    ((_)   | || | (_))    ((_) (_))   ")
    print(f"  / _ \   | '_ \ / _` | | ' \)) / _` |  / _ \ | ' \))     / _ \   | |  | |    | __ | / _ \ | '_ \) / -_)     \ V /  / -_)     \ \/\/ / | ' \  / _ \   | _|  | ' \)) |  _|  / -_)  | '_|   | __ | / -_)  | '_| / -_)  ")
    print(f" /_/ \_\  |_.__/ \__,_| |_||_|  \__,_|  \___/ |_||_|     /_/ \_\  |_|  |_|    |_||_| \___/ | .__/  \___|      |_|   \___|      \_/\_/  |_||_| \___/   |___| |_||_|   \__|  \___|  |_|     |_||_| \___|  |_|   \___|  ")
    time.sleep(2)
    print("\n\nThat...Doesn't sound good....Either way it's the only place to go...")
    time.sleep(1)
    ##### Put stuff here about how the game starts, a quick story maybe?????
    print("\nYou walk through the door, abandoning all hope I guess?\n")
    time.sleep(1)           # Pauses for 1 second and shows next message
    mystery_room()                  # Menu Function


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


#####_____TEST FUNCTION_____#####
# We'll use this to test all our functions without having to go through the game if we need to
def TEST_FUNCTION():
    print("Test")
#_______________________#


#####_____Mystery Room_____#####
# First room of the game
# If they solve all 3 questions right they will go to Random Dude Room
# If they don't they go to Maze Room

def my_check_ans(question, ans, attempts, score):
    """
    Takes the arguments, and confirms if the answer provided by user is correct.
    Converts all answers to lower case to make sure the quiz is not case sensitive.
    """
    if my_quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True    
    else:
        print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...\n")
        return False

####Need to add path to maze room once created
def mystery_room(): 
    time.sleep(1)
    print(f"As you walk down the corridor you end up in a plan looking room with a metal table and computer straight out of the 1970s")
    print(f"Reading the screen shows you some text, perhaps a riddle? As if this day wasn't confusing already")
    time.sleep(2)
    print(f"\n\n    .__________________________.")
    print(f"    | .___________________. |==|")
    print(f"    | | ................. | |  |")
    print(f"    | | .....Answer...... | |  |")
    print(f"    | | .....These........| |  |")
    print(f"    | | .....Questions... | |  |")
    print(f"    | | .....Three....... | |  |")
    print(f"    | | .....To.......... | |  |")
    print(f"    | | .....Proceed..... | | ,|")
    print(f"    | !___________________! |(c|")#Computer ascii art??
    print(f"    !_______________________!__!")
    print(f"   /                            \ ")
    print(f"  /  [][][][][][][][][][][][][]  \ ")
    print(f" /  [][][][][][][][][][][][][][]  \ ")
    print(f"(  [][][][][____________][][][][]  ) ")
    print(f" \ ------------------------------ / ")
    print(f"  \______________________________/ \n\n")
    time.sleep(2)
    print(f"\n\n    .__________________________.")
    print(f"    | .___________________.  |==|")
    print(f"    | | .................. | |  |")
    print(f"    | | ........Our....... | |  |")
    print(f"    | | .Great Glory is not| |  |")
    print(f"    | | ...in failing......| |  |")
    print(f"    | | ...but in rising.. | |  |")
    print(f"    | | .every time....... | |  |")
    print(f"    | | .....we fall...... | | ,|")
    print(f"    | !___________________! |(c|")#Computer ascii art??
    print(f"    !_______________________!__!")
    print(f"   /                            \ ")
    print(f"  /  [][][][][][][][][][][][][]  \ ")
    print(f" /  [][][][][][][][][][][][][][]  \ ")
    print(f"(  [][][][][____________][][][][]  ) ")
    print(f" \ ------------------------------ / ")
    print(f"  \______________________________/ \n\n")

    time.sleep(2)
    while True:
        score = 0
        for question in my_quiz:
            attempts = 3
            while attempts > 0:
                print(my_quiz[question]['question'])
                answer = input("Enter Answer (To move to the next question, type 'skip') : ")
                if answer == "skip":
                    break
                check = my_check_ans(question, answer, attempts, score)
                if check:
                    score += 1
                    break
                attempts -= 1
                # if score >= 3:
                #     print("Elephant Room")
                # else:
                #     print("Riddle Room")
        break        
    if score == 3:
        time.sleep(1)
        print("THIS WILL TAKE YOU TO RANDOM DUDE")
        stone_choice()
    else:
        time.sleep(1)
        print(f"\nMAZE ROOM\n")





    # score = 0           # Temp Variable for score for this quiz only
    # while True:         # When the user presses any key from before do this
    #     for question in quiz:   # For how many questions there are in our QUIZ list do the following
    #         attempts = 3        # User has 3 attempts to get each question correct
    #         while attempts > 0: # While they have more than 0 attempts print a question and ask their input
    #                         # Can always just have 0 attempts aswell
    #             print(quiz[question]['question'])   # Print the question from the question list
    #             answer = input("Enter Answer (To move to the next question, type 'skip' but you will forfeit any points) : ")
    #             if answer == "skip":   # If the user skips the question break this and go to next question 
    #                 break
    #             check = check_ans(question, answer, attempts, score)
    #             if check:
    #                 score += 1
    #                 break
    #         attempts -= 1
    #     break
    # if score == 3:
    #     time.sleep(1)
    #     print(f"\n'CLever message on why they go to the Random Dude'\n")
    #     stone_choice()
    # else:
    #     time.sleep(1)
    #     print(f"\n'CLever message on why they go to the Maze Room'\n")
            
#_______________________#

#####_____Maths_Quiz_____#####

def m_check_ans(question, ans, attempts, score):
    """
    Takes the arguments, and confirms if the answer provided by user is correct.
    Converts all answers to lower case to make sure the quiz is not case sensitive.
    """
    if m_quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True    
    else:
        print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...\n")
        return False


def maths_quiz():
    while True:
        score = 0
        for question in m_quiz:
            attempts = 3
            while attempts > 0:
                print(m_quiz[question]['question'])
                answer = input("Enter Answer (To move to the next question, type 'skip') : ")
                if answer == "skip":
                    break
                check = m_check_ans(question, answer, attempts, score)
                if check:
                    score += 1
                    break
                attempts -= 1
                # if score >= 3:
                #     print("Elephant Room")
                # else:
                #     print("Riddle Room")
        break        
    if score == 3:
        time.sleep(1)
        elephant_room()
    else:
        time.sleep(1)
        print(f"\nNOT SURE\n")
            
#_______________________#


#####_____Stone_choice_____#####
# Second room of game
# Random dude and all that.....
def stone_choice():
    print ("Welcome to the next stage of your mystery path")
    print ("you see a person in the distance")
    print ("He is holding three stones in hes hands , choose one and check if thats you lucky day and your stone  will move you to the next stage")
    time.sleep(0.5)
    print("stone1")
    print("stone2")
    print("stone3")
    time.sleep(0.5)

    t_stone_choice   =  input()

    if t_stone_choice ==  "stone1":
        elephant_room()
    elif t_stone_choice == "stone2":
        maths_quiz()
    elif t_stone_choice == "stone3":
        try_again()
    else:
        print("\nYour choices are \nstone1\nstone2\nstone3\n")
#_______________________#


#####_____Elephant Room _____#####
def elephant_room():
        print("\nYou hurry through winding corridor which seems to get tighether the more you go")
        print("\nLuckily, I'm not claustraphobic, that'd be awkawrd....")
        time.sleep(1)
        print("\nYou squeeze through a small door to find yourself in a room with, an Elephant?!\n'OK that's just bizarre now, you say with confusion upon your face'\n")
        time.sleep(1)
        print("\n*ELEPHANT NOISES*\n\nOh no....it looks angry better make a decision and fast!")
        print("\nThere's door on the other side, if I'm fast enough I could RUN past the Elephant")
        time.sleep(0.5)
        print("\nOH! and a small hole on the left, maybe I can CRAWL through that")
        print("\nI defintitely shouldn't PET the Elephant not in this state")
        
        while True:
        # Makes sure the user can only enter an Integer, anything else returns an error
            try:
                option = input("\nWhat the heck am I supposed to do now?!\n") # Asks the user this quest and awaits input
                break
            except:
                print("Nope, Can't do that...")     # If user does not enter Integer do this
        if option == "run":
                print("'Player runs around it' Makes it to room: Multiple Choice Quiz")
                ##try_again() #Calls the try again function to ask if they want to restart the game or not
        elif option == "pet":
            print("Maybe I should pet it?\nShow the thing I'm friendly and what not?\n *STOMP*\n")
            time.sleep(1)
            print("The player gets stomped to death")
            try_again()
        elif option == "crawl":
                print("'Player crawls through the hole in the wall' AND makes it to room: Maths Quiz again lol?")
                maths_quiz()
        else:
                time.sleep(1)
                print("\nWrong Option please try again")
                time.sleep(1)   
                elephant_room()



#####_____Maze Room _____#####

def path_choice():
    print ("you are in the maze and you can see two paths from the distance ")
    print ("One is the main path out from the maze  ")
    print ("The other one is a secret path and no one knows where it takes you    ")
    print ("Which way  do you choose ?")
    print("A")
    print("B")


    t_path_choice   =  input()

    if t_path_choice ==  "A":
        print("Main path out  ")
        stone_choice()
    elif t_path_choice == "B":
        print ("Door to the secret room ")
    else:
        print("Something went wrong , please try again ")
        path_choice()

def code():
    print ("Looks like you got off from the main path of the game. You can still go back on it through secret room  ")
    print ("But first you need to open the door to secret room. To do it you need to insert the code  ")
    print ( " The code is : All prime numbers between 1 and 10  ")
    print ("If you stuck you can type 'skip' which will take you back to another path instead")
    
    t_code =  input()

    if t_code ==  "2357":
        print("Code correct .Welcome in secret room  ")
        #secret Room
    elif t_code == "skip":
        stone_choice()
    else:
        print("Something went wrong , please try again ")
        code()

def quiz_choice():
    print ("Welcome to the secret room ")
    print ("From where you can go back to the main path of the game   ")
    print ( "You just need to take a part of our quiz and succesfully  ansewer  the question  ")
    print (" Correct answer will automatically direct you to the main path of the game ")
    time.sleep(1)
    print ("What is the hardest known mineral ? ")
    print ("A     Emerald")
    print ("B     Diamond")
    print ("C     Ruby")
    print ("D     Sapphire")

    quiz_choice1   =  input()

    if quiz_choice1 ==  "B":
        print("Correct answer !  ")
        stone_choice()
    else:
        print("Please try again ! ")
        quiz_choice()

#_______________________#

#####_____Multiple Choice Quiz Room _____#####

def m_quiz_choice():
    print ("What is the name of the preserved bodies of ancient Egypt ")
    print ("A     Daddies")
    print ("B     Mummies")
    print ("C     Aunties")
    print ("D     Grannies")
    t_quiz_choice   =  input()
    if t_quiz_choice ==  "B":
        print("Correct answer !  ")
        print("MAKE Choice Room")   ###Make choice room
    else:
        print("Please try again ! ")
        m_quiz_choice()

#_______________________#


#####_____Choice Room _____#####
# Does the player go to end or do they go back to riddle room first then end?

def choice_room():
    print ("\nYou have 2 choices: Go down a spiral staircase or through a cool looking portal\nWhich do you choose?")
    print("\nChoose carefully....")
    print("\nType 'portal' or 'stairs' for your answer")
    t_choice = input()
    if t_choice == "portal":
        ###send them to riddle room
        print("")
    elif t_choice == "stairs":
        end_game()
        print("")
    else:
        print("wrong input")
        choice_room()

#_______________________#

#####_____Choice Room _____#####
# Does the player go to end or do they go back to riddle room first then end?

def end_game():
    print("Thanks for playing")
    print("Are you sure you there weren't other ways to explore?")
    
    e_input = input()

    if e_input == "end":
        sys.ext()
    elif e_input == "try again":
        welcome()
    else:
        print("wrong input")    

#_______________________#


welcome()