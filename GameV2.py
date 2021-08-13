import time
import sys

#####_____Variables_____#####
name = "" # Updated with name = input
#_______________________#

#####_____Quiz List_____#####
quiz = {
    1 : {
        "question" : "Question 1?", # What could we ask I wonder ??? :)
        "answer" : "1"                                   # Change this for the answer
    },
    2 : {
        "question" : "Question 2?",
        "answer" : "2"
    },
    3 : {
        "question" : "Question 3",
        "answer" : "3"
    }, # If last question remove ,
    # 4 : {
    #     "question" : "Which avenger is green in color?",
    #     "answer" : "Hulk"
    # },
    # 5 : {
    #     "question" : "Which avenger can change it's size?",
    #     "answer" : "AntMan"
    # },
    # 6 : {
    #     "question" : "Which Avenger is red in color and has mind stone?",
    #     "answer" : "Vision"
    # }
} ### Stores the questions and answers
#_______________________#

#####_____Check Answers Function_____#####
# This takes the arguments for the quiz and confirms if the answer by the user is correct
# We convert the answer to lower case - We do this to prevent as many errors as we can
# So it user does ANTHONY, anthony is also accepted
def check_ans(question, ans, attempts, score):
    
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
        return False
#_______________________#


def welcome():              # Welcome function that'll ask for user name
    #print("\nHello...What's your name?\n")
    #name = input # Updates the Users name
    print(f"\nWelcome to the game\n") # Welcome 
    ##### Put stuff here about how the game starts, a quick story maybe?????
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
def mystery_room(): 
    score = 0           # Temp Variable for score for this quiz only
    while True:         # When the user presses any key from before do this
        for question in quiz:   # For how many questions there are in our QUIZ list do the following
            attempts = 3        # User has 3 attempts to get each question correct
            while attempts >= 0: # While they have more than 0 attempts print a question and ask their input
                            # Can always just have 0 attempts aswell
                print(quiz[question]['question'])   # Print the question from the question list
                answer = input("Enter Answer (To move to the next question, type 'skip') : ")
                if answer == "skip":   # If the user skips the question break this and go to next question 
                    break
                check = check_ans(question, answer, attempts, score)
                if check:
                    score += 1
                    break
            attempts -= 1
        if score == 3:
            time.sleep(1)
            print(f"\n'CLever message on why they go to the Random Dude'\n")
            stone_choice()
        else:
            time.sleep(1)
            print(f"\n'CLever message on why they go to the Maze Room'\n")
        break    
#_______________________#


#####_____Stone_choice_____#####
# Second room of game
# Random dude and all that.....
def stone_choice():
    print ("Welcome to the next stage of your mistery path")
    print ("you see a person in the distance")
    print ("He is holding three stones in hes hands , choose one and check if thats you lucky day and your stone  will move you to the next stage")
    time.sleep(0.5)
    print("stone1")
    print("stone2")
    print("stone3")
    time.sleep(0.5)

    t_stone_choice   =  input()

    if t_stone_choice ==  "stone1":
        print("you made the right choice and you been given a hint ")
    elif t_stone_choice == "stone2":
        print("congratulation, you jumped into next level")
    elif t_stone_choice == "stone3":
        print("you have to restart the game ")
    else:
        print("\nYour choices are \nstone1\nstone2\nstone3\n")
#_______________________#


#####_____Elephant Room _____#####
def elephant_room():
        print("\nQuestion")
        print("\n(1) ")
        print("\n(2) ")
        print("\n(3) ")

        while True:
        # Makes sure the user can only enter an Integer, anything else returns an error
            try:
                option = input("\nHow do you approach this situation?\n") # Asks the user this quest and awaits input
                break
            except:
                print("That's not a valid option!")     # If user does not enter Integer do this
        if option == "run":
                print("player runs around it, makes it to room: Multiple Choice Quiz")
                ##try_again() #Calls the try again function to ask if they want to restart the game or not
        elif option == "pet":
            print("Player gets stomped")
            try_again()
        elif option == "crawl":
                print("Player crawls through the hole in the wall and makes it to room: Riddle")
        else:
                print("\nWrong Option please try again")
                time.sleep(0.5)   
                elephant_room()

#_______________________#





welcome()
