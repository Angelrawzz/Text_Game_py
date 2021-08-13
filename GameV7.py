import time
import sys

#####_____Variables_____#####
name = "" # Updated with name = input
#_______________________#

#####_____Quiz List_____#####
my_quiz = {
    1 : {
        "question" : "A detective who was mere days from cracking an international smuggling ring has suddenly gone missing \nWhile inspecting his last-known location, you find a note: '710 57735 34 5508 51 7718'" 
                     "\nCurrently there are 3 suspects: Bill, John, and Todd. \n\nCan you break the detective’s code and find the criminal’s name?(Hint: Maybe look at this from a different perspective(upside down perhaps?))",
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
        print("\nTry Again?\n")
        print("\nType 'y' or 'n' for your decision\n")
        t_option = input()
        if t_option == "y":
                welcome()
        elif t_option =="n":
                sys.exit()
        else:
                print("Wrong option")
                try_again()
                
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

def mystery_room(): 
    time.sleep(1)
    print(f"As you walk down the corridor you end up in a plain looking room with a metal table and computer straight out of the 1970s")
    print(f"Reading the screen shows you some text, perhaps a riddle? As if this day wasn't confusing already")
    time.sleep(2)
    print(f"\n\n   .__________________________.")
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
    if score >= 3:
        time.sleep(1)
        stone_choice()
    else:
        time.sleep(1)
        path_choice()
            
#_______________________#

#####_____Maths_Quiz_____#####

def m_check_ans(question, ans, attempts, score):
    #Takes the arguments, and confirms if the answer provided by user is correct.
    # Converts all answers to lower case to make sure the quiz is not case sensitive.
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
        break        
    if score >= 3:
        time.sleep(1)
        elephant_room()
    else:
        time.sleep(1)
        m_quiz_choice()
            
#_______________________#


#####_____Stone_choice_____#####
# Second room of game
# Random dude and all that.....
def stone_choice():
    print ("Welcome to the next stage of your mystery path")
    print ("you see a person in the distance")
    print ("He is holding three stones in hes hands , choose one and check if thats you lucky day and your stone  will move you to the next stage")
    time.sleep(0.5)
    print("stone1\nston2stone3\n")
    time.sleep(0.5)

    t_stone_choice   =  input()

    if t_stone_choice ==  "stone1":
        elephant_room()
    elif t_stone_choice == "stone2":
        maths_quiz()
    elif t_stone_choice == "stone3":
        print("You have chosen the wrong stone *death sounds*")
        time.sleep(1)
        try_again()
    else:
        print("Incorrect Input, Try Again")        
        stone_choice()
#_______________________#


#####_____Elephant Room _____#####
# Needs to have story wrote
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
                m_quiz_choice()
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
        path_choice()
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
        choice_room()
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
        question1()
        print("")
    elif t_choice == "stairs":
        end_game()
        print("")
    else:
        print("wrong input")
        choice_room()

#_______________________#

#####_____Riddle Room _____#####
## player will go here if they go through the portal

def question1():
    print("         _             ")
    time.sleep(0.2)
    print("      _-'_'-_ ")
    time.sleep(0.2)
    print("   _-' _____ '-_ ")
    time.sleep(0.2)
    print("_-' ___________ '-_ ")
    time.sleep(0.2)
    print(" |___|||||||||___| ")
    time.sleep(0.2)
    print(" |___|||||||||___| ")
    time.sleep(0.2)
    print(" |___|||||||o|___| ")
    time.sleep(0.2)
    print(" |___|||||||||___| ")
    time.sleep(0.2)
    print(" |___|||||||||___| ")
    time.sleep(0.2)
    print(" |___|||||||||___| ")
    time.sleep(0.2)
    print("You stumble though a door into a room with 3 pillers,its fairly dark,there is some light but you arent sure where from, the room feels cold, and damp.\n"
    "There appears to be an outline of a door at the far end of the room")
    time.sleep(1.5)
    print("1 Do you inspect the pillers?")
    print("2 Do you walk towards the door?")
    answer=input(" ")
    if answer=="1":
        print(" oOOO() ")
        time.sleep(0.2)
        print(" /  _)  ")
        time.sleep(0.2)
        print(" |  (  ")
        time.sleep(0.2)
        print(" \__)  ()OOOo")
        time.sleep(0.2)
        print("       (_  \ ")
        time.sleep(0.2)
        print("         )  |")
        time.sleep(0.2)
        print(" oOOO()  (__/")
        time.sleep(0.2)
        print(" /  _)")
        time.sleep(0.2)
        print(" |  (")
        time.sleep(0.2)
        print(" \__)  ()OOOo")
        time.sleep(0.2)
        print("You walk over to the pillers and look closly and notice 1 markings on each, you go to touch one and it moves and water starts to fil the room as the door slams shut") 
        question2()
    elif answer=="2":
        print("You step on a floor tile that sinks under your weight, the door slams shut and water starts to pour in ")
        question2()
    else:
        print("invaild input")
        question1()
def question2():
    print("You have 2 choices to survive")
    time.sleep(1.5)
    print("1 Do you run to the door to escape?") 
    print("2 Or grab the pillers and try to climb?")
    answer=input(" ")
    if answer =="1":
        print("oOOO() ")
        time.sleep(0.1)
        print("/  _)  ")
        time.sleep(0.1)
        print("|  (   ()OOOo ")
        time.sleep(0.1)
        print("\__)    (_  \ ")
        time.sleep(0.1)
        print("         )  | ")
        time.sleep(0.1)
        print("         (__/ ")
        time.sleep(0.1)
        print("In your panic to set of you trip and fall over the other bodies on the floor you didn't see,you hurt your ankle,the water fills up around you,\n"
        "you cant stay afloat in the water and you slowly drown in the room to sink on top of the other bodies") 
        print("\n ")
        time.sleep(1.5)
        question1()
    elif answer =="2":
        print("you grab the first piller and notice finger marks, you quickly start to climb you use the water to help you get to the top")
        question3()
    else:
        print("invaild input")
        question2()
def question3():
    print("upon climbing the piller you see a small light from the top of one of the pillers, this must of been the light from when you walked in,it seems to small to fit though")
    time.sleep(1.5)
    print("1 Do you swim to the light? ")
    print("2 Do you try to dive down for the door?")
    answer=input(" ")
    if answer=="1":
        print("Upon swimming to the light you manage to push your hand thought the gap and after feeling around for a few seconds you feel a chain")
        question4()
    elif answer=="2":
        print("You make it to the door, you fiddle with it,,,,its locked!!\n"
        "You turn to swim away, but your pants leg is caught on the handle, in your panic you fail to release yourself, you drown and sink on top of the other bodies")
        print("\n ")
        question1()
    else:
        print("invaild input")
        question3()
def question4():
    print("You are treading water holding on to a piller and the chain,")
    time.sleep(1.5)
    print("1 Do you pull the chain")
    print("2 You dont pull the chain")
    answer4=input(" ")
    if answer4=="1":
        print("you pull the chain and the its stuck, you yank on the chain,\n "
        "the chain falls with you as it does the roof comes with it, a big boulder pushed up down and you lay stuck to drown on the bodies.\n"
        "seriouly stop just pulling random chains")
        print("\n ")
        question1()
    elif answer4=="2":
        print("you stay holding the chain wondering what to do as pulling it doesnt seem right,\n"
        "just as you think all is losed the weight of the water forces the door open\n"
        "you ride the wave down and land just at the door entrance ready to walk out ")
    else:
        print("invaild input")
        question4()

#####_____End Room _____#####
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