import time


# quiz = {
#     1 : {
#         "question" : "What is the first name of Iron Man?", # What could we ask I wonder ??? :)
#         "answer" : "Tony"                                   # Change this for the answer
#     },
#     2 : {
#         "question" : "Who is called the god of lightning in Avengers?",
#         "answer" : "Thor"
#     },
#     3 : {
#         "question" : "Who carries a shield of American flag theme in Avengers?",
#         "answer" : "Captain America"
#     },
#     4 : {
#         "question" : "Which avenger is green in color?",
#         "answer" : "Hulk"
#     },
#     5 : {
#         "question" : "Which avenger can change it's size?",
#         "answer" : "AntMan"
#     },
#     6 : {
#         "question" : "Which Avenger is red in color and has mind stone?",
#         "answer" : "Vision"
#     }
# } ### Stores the questions and answers

# def check_ans(question, ans, attempts, score):
    
#     if quiz[question]['answer'].lower() == ans.lower():
#         print(f"Correct Answer! \nYour score is {score + 1}!")
#         return True
#     else:
#         print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
#         return False
# # This takes the arguments for the quiz and confirms if the answer by the user is correct
# # We convert the answer to lower case - We do this to prevent as many errors as we can
# # So it user does ANTHONY, anthony is also accepted

# # def intro_message():
    
# #     # Introudces user to the quiz basically, can also do this without using a function
# #     # Takes the user to the WHILE Statement regardless of any key pressed.
# #     # Don't think we need this just fun
# #     print("Welcome to the quiz")
# #     input("Press any key to start the fun ;) ")
# #     return True


# #intro = intro_message()
# while True:         # When the user presses any key from before do this
#     score = 0       # Temp Variable for score for this quiz only
#     for question in quiz:   # For how many questions there are in our QUIZ list do the following
#         attempts = 3        # User has 3 attempts to get each question correct
#         while attempts > 0: # While they have more than 0 attempts print a question and ask their input
#                             # Can always just have 0 attempts aswell
#             print(quiz[question]['question'])   # Print the question from the question list
#             answer = input("Enter Answer (To move to the next question, type 'skip') : ")
#             if answer == "skip":   # If the user skips the question break this and go to next question 
#                 break
#             check = check_ans(question, answer, attempts, score)
#             if check:
#                 score += 1
#                 break
#             #attempts -= 1

#     break

# print(f"Your final score is {score}!\n\n")

# print("Thanks for playing! 💜")

def check_ans(question, ans, attempts, score):
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


