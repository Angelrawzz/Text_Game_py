def question1():
    print("you enter a room with 3 pillers ")
    print("1 do you inspect the pillers?")
    print("2  do you walk for the door")
    answer=input(" ")
    if answer=="1":
        print("you walk over to the pillers and look closly and notice 1 markings on each, you go to touch one and it moves and water starts to fil the room as the door slams shut")   
        question2()
    elif answer=="2":
        print("you step on a floor tile that sinks under your weight, the door slams shut and water starts to pour in ")
        question2()
def question2():
    print("you have 2 choices")
    print("1 run to the door") 
    print("2 or garb the pillers and try to climb")
    answer=input(" ")
    if answer =="1":
        print(" you trip and fall and hurt your ankle,the water fills up around you as you drown")
        question1()
    elif answer =="2":
        print("you grab the first piller and notice finger marks to the top from previous challenages, you climb to the top")
        question3()
def question3():
    print("upon climbing the piller you see a small light from the top of one of the pillers")
    print("1 you swim to the light ")
    print("2 you try to dive down for the door")
    answer=input(" ")
    if answer=="1":
        print(" you manage to push your hand thought the gap and feel a chain")
        question4()
    elif answer=="2":
        print("you get trapped ands die")
        question1()
def question4():
    print("do you pull the chain")
    print("1 do you pull the chain")
    print("2 you dont pull the chain, i mean who would really yeah")
    answer4=input(" ")
    if answer4=="1":
        print("you pull the chain and the door opens letting the water out and you to ride the wave down to the floor and safley out the door. ")
        print(" you made the easy bit i see, welcome to the next challeage ")
    elif answer4=="2":
        print("you stay holding the chain until your body freezes in the cold water and you float down to be a victim of the room...why would not pull the chain.")
        question1()
question1()