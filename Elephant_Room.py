
#####_____Elephant Room _____#####
def elephant_room():
        print("\nYou hurry through winding corridor which seems to get tighether the more you go")
        print("\nLuckily, I'm not claustraphobic, hehe....")
        print("\nYou squeeze through a small door to find yourself in a room with, an Elephant?!\n'OK that's just bizarre now, you say with confusion upon your face'")     

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
            #time.sleep(1)
            print("The player gets stomped to death")
            #try_again()
        elif option == "crawl":
                print("'Player crawls through the hole in the wall' AND makes it to room: Riddle")
        else:
                print("\nWrong Option please try again")
                #time.sleep(0.5)   
                elephant_room()
elephant_room()
