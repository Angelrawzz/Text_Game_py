import time
def path_choice():
    print ("you are in the maze and you can see two paths from the distance ")
    print ("One is the main path out from the maze  ")
    print ( "The other one is a secret path and no one knows where it takes you    ")
    print ("Which way  do you choose ?")
    print("A")
    print("B")

    t_path_choice   =  input()

    if t_path_choice ==  "A":
        code()
    elif t_path_choice == "B":
        stone_choice()                
    else:
        print("Something went wrong , please try again ")
        path_choice()

def code():
    print ("Looks like you got off from the main path of the game. You can still go back on it through secret room  ")
    print ("But first you need to open the door to secret room. To do it you need to insert the code  ")
    print ( " The code is : All prime numbers between 1 and 10  ")

    t_code =  input()

    if t_code ==  "2357":
        print("Code correct .Welcome in secret room  ")
    else:
        print("Something went wrong , please try again ")

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

path_choice()