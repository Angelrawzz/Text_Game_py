import sys
import time

# # # def welcome():              # Welcome function that'll ask for user name
# # #     #print("\nHello...What's your name?\n")
# # #     #name = input # Updates the Users name
# # #     print(f"\nWelcome to the game\n") # Welcome 
# # #     ##### Put stuff here about how the game starts, a quick story maybe?????
# # #     time.sleep(1)           # Pauses for 1 second and shows next message
# # #     #mystery_room()                  # Menu Function




# # # #####_____Try Again_____#####
# # # # We use this function when the user needs to restart for whatever reason
# # # # Example - They take a wrong turn and die
# # # def try_again():
# # #         t_option = input()
# # #         while True:
# # #                 try:
# # #                         t_option = t_option.lower(("\nTry Again?\n"))
# # #                         break
# # #                 except:
# # #                         print("\nWrong option do it again!\n")
# # #         if t_option == "y":
# # #                 welcome()
# # #         elif t_option =="n":
# # #                 sys.ext()
# # #         else:
# # #                 print("Wrong option")
# # # #_______________________#

# # # try_again()




# # # def quiz_choice():
# # #         print ("What is the name of the preserved bodies of ancient Egypt ")
# # #         print ("A     Daddies")
# # #         print ("B     Mummies")
# # #         print ("C     Aunties")
# # #         print ("D     Grannies")
# # #         print("A")
# # #         print("B")
# # #         print("C")
# # #         print("D")
# # #         quiz_choice   =  input()
# # #         if quiz_choice ==  "B":
# # #                 print("Correct answer !  ")
# # #         else:
# # #                 print("Please try again ! ")
# # # quiz_choice()


# # quiz = {
# #     1 : {
# #         "question" : "What is the first name of Iron Man?",
# #         "answer" : "Tony"
# #     },
# #     2 : {
# #         "question" : "Who is called the god of lightning in Avengers?",
# #         "answer" : "Thor"
# #     },
# #     3 : {
# #         "question" : "Who carries a shield of American flag theme in Avengers?",
# #         "answer" : "Captain America"
# #     },
# #     4 : {
# #         "question" : "Which avenger is green in color?",
# #         "answer" : "Hulk"
# #     },
# #     5 : {
# #         "question" : "Which avenger can change it's size?",
# #         "answer" : "AntMan"
# #     },
# #     6 : {
# #         "question" : "Which Avenger is red in color and has mind stone?",
# #         "answer" : "Vision"
# #     }
# # }





# # def check_ans(question, ans, attempts, score):
# #     """
# #     Takes the arguments, and confirms if the answer provided by user is correct.
# #     Converts all answers to lower case to make sure the quiz is not case sensitive.
# #     """
# #     if quiz[question]['answer'].lower() == ans.lower():
# #         print(f"Correct Answer! \nYour score is {score + 1}!")
# #         return True
# #     else:
# #         print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
# #         return False



# # while True:
# #     score = 0
# #     for question in quiz:
# #         attempts = 3
# #         while attempts > 0:
# #             print(quiz[question]['question'])
# #             answer = input("Enter Answer (To move to the next question, type 'skip') : ")
# #             if answer == "skip":
# #                 break
# #             check = check_ans(question, answer, attempts, score)
# #             if check:
# #                 score += 1
# #                 break
# #             attempts -= 1
# #     break

# # print(f"Your score is {score}!\n\n")
# # print("Thanks for playing! 💜")


# # def path_choice():
# #     print ("you are in the maze and you can see two paths from the distance ")
# #     print ("One is the main path out from the maze  ")
# #     print ( "The other one is a secret path and no one knows where it takes you    ")
# #     print ("Which way  do you choose ?")
# #     print("A")
# #     print("B")

# #     t_path_choice   =  input()

# #     if t_path_choice ==  "A":
# #         #code()
# #         print("code")
# #     elif t_path_choice == "B":
# #         print("stone_choice")
# #         #stone_choice()                
# #     else:
# #         print("Something went wrong , please try again ")
# #         path_choice()


# # path_choice()


# # #####_____Multiple Choice Quiz Room _____#####

# # def m_quiz_choice():
# #     print ("What is the name of the preserved bodies of ancient Egypt ")
# #     print ("A     Daddies")
# #     print ("B     Mummies")
# #     print ("C     Aunties")
# #     print ("D     Grannies")
# #     t_quiz_choice   =  input()
# #     if t_quiz_choice ==  "B":
# #         print("Correct answer !  ")
# #     else:
# #         print("Please try again ! ")
# #         m_quiz_choice()

# # #_______________________#

# # # m_quiz_choice()



# # #####_____Stone_choice_____#####
# # # Second room of game
# # # Random dude and all that.....
# # def stone_choice():
# #     print ("Welcome to the next stage of your mystery path")
# #     print ("you see a person in the distance")
# #     print ("He is holding three stones in hes hands , choose one and check if thats you lucky day and your stone  will move you to the next stage")
# #     time.sleep(0.5)
# #     print("stone1")
# #     print("stone2")
# #     print("stone3")
# #     time.sleep(0.5)

# #     t_stone_choice   =  input()

# #     if t_stone_choice ==  "stone1":
# #         print("elephant room")#elephant_room()
# #     elif t_stone_choice == "stone2":
# #         print("room")
# #     elif t_stone_choice == "stone3":
# #         print("try again")
# #     else:
# #         print("Incorrect Input, Try Again")        
# #         stone_choice()
# # stone_choice()

# # #####_____Try Again_____#####
# # # We use this function when the user needs to restart for whatever reason
# # # Example - They take a wrong turn and die
# # def try_again():
# #         print("\nTry Again?\n")
# #         print("\nType 'y' or 'n' for your decision\n")
# #         t_option = input()
# #         t_option = t_option(input.lower())
# #         if t_option == "y":
# #                 print("y")
# #         elif t_option =="n":
# #                 sys.exit()
# #         else:
# #                 print("Wrong option")
# #                 try_again()
# # #_______________________#
# # try_again()

# # a=(0.1)
# # b=(0.2)
# # s ='" helloooo'" "
# # for character in s:
# #     sys.stdout.write(character)
# #     sys.stdout.flush()
# #     time.sleep(b)

# # def path_choice():
# #     print ("you are in the maze and you can see two paths from the distance ")
# #     print ("One is the main path out from the maze  ")
# #     print ("The other one is a secret path and no one knows where it takes you    ")
# #     print ("Which way  do you choose ?")
# #     print("A")
# #     print("B")
# #     t_path_choice = input()      
# #     if t_path_choice.lower() ==  "A".lower():
# #         print("Main path out  ")
# #         print("stone_choice room")
# #     elif t_path_choice.lower() == "B".lower():
# #         print ("Door to the secret room ")
# #     else:
# #         print("Something went wrong , please try again ")
# #         path_choice()


# # def code():
# #     print ("Looks like you got off from the main path of the game. You can still go back on it through secret room  ")
# #     print ("But first you need to open the door to secret room. To do it you need to insert the code  ")
# #     print ( " The code is : All prime numbers between 1 and 10  ")
# #     print ("If you stuck you can type 'skip' which will take you back to another path instead")
    
# #     t_code =  input()

# #     if t_code ==  "2357":
# #         print("Code correct. Welcome in secret room  ")
# #         path_choice()
# #     elif t_code.upper() == "skip".upper():
# #             print("stone_choice room")
# #             stone_choice()
# #     else:
# #         print("Something went wrong , please try again ")
# #         code()

# # def quiz_choice():
# #     print ("Welcome to the secret room ")
# #     print ("From where you can go back to the main path of the game   ")
# #     print ( "You just need to take a part of our quiz and succesfully  ansewer  the question  ")
# #     print (" Correct answer will automatically direct you to the main path of the game ")
# #     time.sleep(1)
# #     print ("What is the hardest known mineral ? ")
# #     print ("A     Emerald")
# #     print ("B     Diamond")
# #     print ("C     Ruby")
# #     print ("D     Sapphire")

# #     quiz_choice1   =  input()

# #     if quiz_choice1.lower() ==  "B".lower():
# #         print("Correct answer !  ")
# #         print("stone_choice room")
# #     else:
# #         print("Please try again ! ")
# #         quiz_choice()

# # path_choice()

# # #####_____Variables_____#####
# # name = "" # Updated with name = input
# # #_______________________#

# # #####_____Quiz List_____#####
# # my_quiz = {
# #     1 : {
# #         "question" : "A detective who was mere days from cracking an international smuggling ring has suddenly gone missing \nWhile inspecting his last-known location, you find a note: '710 57735 34 5508 51 7718'" 
# #                      "\nCurrently there are 3 suspects: Bill, John, and Todd. \n\nCan you break the detective’s code and find the criminal’s name?(Hint: Maybe look at this from a different perspective(upside down perhaps?))",
# #         "answer" : "Bill"                                   # Bill. If you read the message upside down, you’ll notice that the numbers resemble letters and that those letters form legible sentences. The message is "Bill is boss. He sells oil."
# #     },
# #     2 : {
# #         "question" : "\nImagine that you have been captured by an enemy. You are to be killed," 
# #                      "\nBut in a moment of mercy, the enemyt has allowed you to pick your own demise."
# #                      "\nYour first choice is to be drowned in a lake of acid" 
# #                      "\nYour second choice is to be burned on a fire"
# #                      "\nYour third choice is to be thrown to a pack of wolves that have not been fed in over a month"
# #                      "\nYour final choice of fate is to be thrown from the walls of a castle, many hundreds of feet high."
# #                      "\n\nWhat fate would you be wise to choose?"
# #                      "(Type 1, 2, 3 or 4 for a decision on your fate)"
# #                      "(I wonder how I'd feel if I hadn't been fed in over a month)",
# #         "answer" : "3" #Being fed to the wolves - wolves cannot survive for 30 days without food, because they would all be dead
# #     },
# #     3 : {
# #         "question" : "\nA renowned chemist is found dead in his lab. There is no clear evidence except a piece of paper"
# #                      "\nThe paper is blank other than the name of five elements scrawled accross it hastily"
# #                      "\nNickel\nCarbon\nOxygen\nLanthanum\nSulfur"
# #                      "\nThe guard reported that three people visited the chemist that day"
# #                      "\nHis sister, LAURA; his collegue, NICOLAS; and his wife TESSA."
# #                      "\n\nThe Criminal was arrested immediately. Who was it?",
# #         "answer" : "nicolas"
# #      }
# # } ### Stores the questions and answers for the mystery quiz

# # m_quiz = {
# #     1 : {
# #         "question" : "What is the most popular lucky number?", # What could we ask I wonder ??? :)
# #         "answer" : "7"                                   # Change this for the answer
# #     },
# #     2 : {
# #         "question" : "What is 5 squared?",
# #         "answer" : "25"
# #     },
# #     3 : {
# #         "question" : "What is (10 + 20 + 30 / 5) x 0 ?\nIs it: |  30  |  0  |  60  |  100  |",
# #         "answer" : "0"
# #     }, 
# #      4 : {
# #          "question" : "Look at this sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...\n What comes after 34?",
# #          "answer" : "55"
# #     }
# # } ### Stores the questions and answers for the maths quiz

# # #_______________________#
# # def m_check_ans(question, ans, attempts, score):
# #     #Takes the arguments, and confirms if the answer provided by user is correct.
# #     # Converts all answers to lower case to make sure the quiz is not case sensitive.
# #     if m_quiz[question]['answer'].lower() == ans.lower():
# #         print(f"Correct Answer! \nYour score is {score + 1}!")
# #         return True    
# #     else:
# #         print(f"Wrong Answer :( \nYou have {attempts - 1} left! \n")
# #         return False

# # def maths_quiz():
# #     while True:
# #         score = 0
# #         for question in m_quiz:
# #             attempts = 3
# #             while attempts > 0:
# #                 print(m_quiz[question]['question'])
# #                 answer = input("Enter Answer (To move to the next question, type 'skip') : ")
# #                 if answer == "skip":
# #                     break
# #                 check = m_check_ans(question, answer, attempts, score)
# #                 if check:
# #                     score += 1
# #                     break
# #                 attempts -= 1               
# #         break        
# #     if score >= 3:
# #         time.sleep(1)
# #         print("elephant room")
# #         #lephant_room()
# #     else:
# #         time.sleep(1)
# #         print("m_quiz_choice")
# #         #m_quiz_choice()

# # maths_quiz()
# def question1():
#     print("         _             ")
#     time.sleep(0.2)
#     print("      _-'_'-_ ")
#     time.sleep(0.2)
#     print("   _-' _____ '-_ ")
#     time.sleep(0.2)
#     print("_-' ___________ '-_ ")
#     time.sleep(0.2)
#     print(" |___|||||||||___| ")
#     time.sleep(0.2)
#     print(" |___|||||||||___| ")
#     time.sleep(0.2)
#     print(" |___|||||||o|___| ")
#     time.sleep(0.2)
#     print(" |___|||||||||___| ")
#     time.sleep(0.2)
#     print(" |___|||||||||___| ")
#     time.sleep(0.2)
#     print(" |___|||||||||___| ")
#     time.sleep(0.2)
#     s= ("You stumble though a door into a room with 3 pillers,its fairly dark,there is some light but you arent sure where from, the room feels cold, and damp.\n"
#     "There appears to be an outline of a door at the far end of the room")
#     for character in s:
#         sys.stdout.write(character)
#         sys.stdout.flush()
#         time.sleep(0.004)
#     print("")
#     print("A Do you inspect the pillers?")
#     print("B Do you walk towards the door?")
#     answer=input("")
#     if answer.lower().strip()=="A".lower().strip():
#         print(" oOOO() ")
#         time.sleep(0.2)
#         print(" /  _)  ")
#         time.sleep(0.2)
#         print(" |  (  ")
#         time.sleep(0.2)
#         print(" \__)  ()OOOo")
#         time.sleep(0.2)
#         print("       (_  \ ")
#         time.sleep(0.2)
#         print("         )  |")
#         time.sleep(0.2)
#         print(" oOOO()  (__/")
#         time.sleep(0.2)
#         print(" /  _)")
#         time.sleep(0.2)
#         print(" |  (")
#         time.sleep(0.2)
#         print(" \__)  ()OOOo")
#         time.sleep(0.2)
#         s=("You walk over to the pillers and look closly and notice 1 markings on each, you go to touch one and it moves and water starts to fil the room as the door slams shut")
#         for character in s:
#             sys.stdout.write(character)
#             sys.stdout.flush()
#             time.sleep(0.004)
#         print("")
#         question2()
#     elif answer.lower().strip()=="B".lower().strip():
#         s=("You step on a floor tile that sinks under your weight, the door slams shut and water starts to pour in ")
#         for character in s:
#             sys.stdout.write(character)
#             sys.stdout.flush()
#             time.sleep(0.004)
#         print("")
#         question2()
#     else:
#         print("invaild input")
#         question1()
# def question2():
#     s=("You have 2 choices to survive")
#     for character in s:
#         sys.stdout.write(character)
#         sys.stdout.flush()
#         time.sleep(0.004)
#     print("")
#     print("A Do you run to the door to escape?") 
#     print("B Or grab the pillers and try to climb?")
#     answer=input(" ")
#     if answer =="A".lower():
#         print("oOOO() ")
#         time.sleep(0.1)
#         print("/  _)  ")
#         time.sleep(0.1)
#         print("|  (   ()OOOo ")
#         time.sleep(0.1)
#         print("\__)    (_  \ ")
#         time.sleep(0.1)
#         print("         )  | ")
#         time.sleep(0.1)
#         print("         (__/ ")
#         time.sleep(0.1)
#         s=("In your panic to set of you trip and fall over the other bodies on the floor you didn't see,you hurt your ankle,the water fills up around you,\n"
#         "you cant stay afloat in the water and you slowly drown in the room to sink on top of the other bodies") 
#         print("\n ")
#         for character in s:
#             sys.stdout.write(character)
#             sys.stdout.flush()
#             time.sleep(0.004)
#         print("")
#         question1()
#     elif answer =="B".lower():
#         print(" \ || /")
#         time.sleep(0.1)
#         print("  ||||")
#         time.sleep(0.1)
#         print("  ||||")
#         time.sleep(0.1)
#         print("  ||||")
#         time.sleep(0.1)
#         print("  ||||")
#         time.sleep(0.1)
#         print("  ||||")
#         time.sleep(0.1)
#         print("  ||||")
#         time.sleep(0.1)
#         print(" / || \ ")
#         time.sleep(0.1)
#         print("|  ||  |")
#         time.sleep(0.1)
#         s=("you grab the first piller and notice finger marks, you quickly start to climb you use the water to help you get to the top")
#         for character in s:
#             sys.stdout.write(character)
#             sys.stdout.flush()
#             time.sleep(0.004)
#         print("")
#         question3()
#     else:
#         print("invaild input")
#         question2()
# def question3():
#     s=("upon climbing the piller you see a small light from the top of one of the pillers, this must of been the light from when you walked in,it seems to small to fit though")
#     for character in s:
#         sys.stdout.write(character)
#         sys.stdout.flush()
#         time.sleep(0.004)
#     print("")
#     print("A Do you swim to the light? ")
#     print("B Do you try to dive down for the door?")
#     answer=input(" ")
#     if answer=="A".lower():
#         print("            ___")
#         time.sleep(0.2)
#         print("          /`  _\ ")
#         time.sleep(0.2)
#         print("          |  / 0|--.")
#         time.sleep(0.2)
#         print("     -   / \_|0`/ /.'._/  ")
#         time.sleep(0.2)
#         print("  - ~ -^_| /-_~ ^- ~_` - -~ _ ")
#         time.sleep(0.2)
#         print(" -  ~  -| |   - ~ -  ~  - ")
#         time.sleep(0.2)
#         print("        \ \, ~   -   ~")
#         time.sleep(0.2)
#         print("         \_|")
#         time.sleep(0.2)
#         s=("Upon swimming to the light you manage to push your hand thought the gap and after feeling around for a few seconds you feel a chain")
#         for character in s:
#             sys.stdout.write(character)
#             sys.stdout.flush()
#             time.sleep(0.004)
#         print("")
#         question4()
#     elif answer=="B".lower():
#         s=("You make it to the door, you fiddle with it,,,,its locked!!\n"
#         "You turn to swim away, but your pants leg is caught on the handle, in your panic you fail to release yourself, you drown and sink on top of the other bodies")
#         for character in s:
#             sys.stdout.write(character)
#             sys.stdout.flush()
#             time.sleep(0.004)
#         print("\n ")
#         question1()
#     else:
#         print("invaild input")
#         question3()
# def question4():
#     s=("You are treading water holding on to a piller and the chain,")
#     for character in s:
#         sys.stdout.write(character)
#         sys.stdout.flush()
#         time.sleep(0.004)
#     print("")
#     print("A Do you pull the chain")
#     print("B You dont pull the chain")
#     answer4=input(" ")
#     if answer4=="A".lower():
#         print("______________    ___________")
#         time.sleep(0.2)
#         print("              \  /      ")
#         time.sleep(0.2)
#         print("  A          ~SNAP~           ")
#         time.sleep(0.2)
#         print("    R           8 ")
#         time.sleep(0.2)
#         print("      H        8 ")
#         time.sleep(0.2)
#         print("        G     8 ")
#         time.sleep(0.2)
#         s=("you pull the chain and the its stuck, you yank on the chain,\n "
#         "the chain falls with you as it does the roof comes with it, a big boulder pushed up down and you lay stuck to drown on the bodies.")
#         for character in s:
#             sys.stdout.write(character)
#             sys.stdout.flush()
#             time.sleep(0.004)
#         print("")    
#         s=("SERIOUSLY, stop just pulling random chains")
#         for character in s:
#             sys.stdout.write(character)
#             sys.stdout.flush()
#             time.sleep(0.03)
#         print("\n ")
#         question1()
#     elif answer4=="B".lower():
#         s=("you stay holding the chain wondering what to do as pulling it doesnt seem right,\n"
#         "just as you think all is losed the weight of the water forces the door open\n"
#         "you ride the wave down and land just at the door entrance ready to walk out ")
#         for character in s:
#             sys.stdout.write(character)
#             sys.stdout.flush()
#             time.sleep(0.003)
#         print("")
#         time.sleep(0.3)     
#         s=("               ***     CONGRATULATIONS!!!    *** ") 
#         for character in s:
#             sys.stdout.write(character)
#             sys.stdout.flush()
#             time.sleep(0.03)
#         time.sleep(0.3)
#     else:
#         print("invaild input")
#         question4()
# question1()


time.sleep(0.5)
print(f"\nRubbing your eyes your sight becomes clearer, a door is in front of you and some words over the top of it...\n") # Welcome 
time.sleep(0.2)
print(f"""                                                                                  )                              )                                                                            )                      
   (          )                   (                        (       (    (      ( /(                           ( /(            (  (         )                            )                  ( /(                      
   )\      ( /(      )            )\ )                     )\      )\   )\     )\())                  (       )\())    (      )\))(   ' ( /(           (             ( /(     (    (       )\())    (    (       (   
((((_)(    )\())  ( /(    (      (()/(    (     (       ((((_)(   ((_) ((_)   ((_)\    (    `  )     ))\     ((_)\    ))\    ((_)()\ )  )\())   (      )\     (      )\())   ))\   )(     ((_)\    ))\   )(     ))\  
 )\ _ )\  ((_)\   )(_))   )\ )    ((_))   )\    )\ )     )\ _ )\   _    _      _((_)   )\   /(/(    /((_)   __ ((_)  /((_)   _(())\_)()((_)\    )\    ((_)    )\ )  (_))/   /((_) (()\     _((_)  /((_) (()\   /((_) 
 (_)_\(_) | |(_) ((_)_   _(_/(    _| |   ((_)  _(_/(     (_)_\(_) | |  | |    | || |  ((_) ((_)_\  (_))     \ \ / / (_))     \ \((_)/ /| |(_)  ((_)   | __|  _(_/(  | |_   (_))    ((_)   | || | (_))    ((_) (_))   
  / _ \   | '_ \ / _` | | ' \)) / _` |  / _ \ | ' \))     / _ \   | |  | |    | __ | / _ \ | '_ \) / -_)     \ V /  / -_)     \ \/\/ / | ' \  / _ \   | _|  | ' \)) |  _|  / -_)  | '_|   | __ | / -_)  | '_| / -_)  
 /_/ \_\  |_.__/ \__,_| |_||_|  \__,_|  \___/ |_||_|     /_/ \_\  |_|  |_|    |_||_| \___/ | .__/  \___|      |_|   \___|      \_/\_/  |_||_| \___/   |___| |_||_|   \__|  \___|  |_|     |_||_| \___|  |_|   \___| 
""")
time.sleep(2)