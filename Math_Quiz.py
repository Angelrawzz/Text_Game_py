import time

#####_____Maths_Quiz_____#####


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
} ### Stores the questions and answers


def check_ans(question, ans, attempts, score):
    """
    Takes the arguments, and confirms if the answer provided by user is correct.
    Converts all answers to lower case to make sure the quiz is not case sensitive.
    """
    if m_quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True    
    else:
        print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
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
                check = check_ans(question, answer, attempts, score)
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
        print("THIS WILL TAKE YOU TO ELEPHANT ROOM")
    else:
        time.sleep(1)
        print(f"\nRIDDLE ROOM\n")
            
#_______________________#





# def maths_q1():
#     global m_score
#     print (f"What is the most popular lucky number?")    
#     answer=input()
#     if answer=="7":        
#         m_score = m_score + 1
#         print(f"Correct\nCurrent Score: ", m_score )
#         maths_q2()
#     elif answer != "7":
#         print(f"Incorrect\nCurrent Score: ", m_score )        
#         maths_q2()
# def maths_q2():
#     global m_score
#     print (f"What is 5 squared")    
#     answer=input()
#     if answer=="25":        
#         m_score = m_score + 1
#         print(f"Correct\nCurrent Score: ", m_score )
#         maths_q3()
#     elif answer != "25":
#         print(f"Incorrect\nCurrent Score: ", m_score )        
#         maths_q3()

# def maths_q3():
#     global m_score
#     print (f"What is (10 + 20 + 30 / 5) x 0 ?")
#     print (f"Is it: |  30  |  0  |  60  |  100  |")    
#     answer=input()
#     if answer=="0":        
#         m_score = m_score + 1
#         print(f"Correct\nCurrent Score: ", m_score )
#         maths_q4()
#     elif answer != "0":
#         print(f"Incorrect\nCurrent Score: ", m_score )        
#         maths_q4()

# def maths_q4():
#     global m_score
#     print (f"Look at this sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...")    
#     time.sleep(0.5)
#     print (f"What comes after 34?")
#     answer=input()
#     if answer=="55":        
#         m_score = m_score + 1
#         print(f"Correct\nCurrent Score: ", m_score )
#         maths_quiz()
#     elif answer != "55":
#         print(f"Incorrect\nCurrent Score: ", m_score )        
#         maths_quiz()

# def maths_quiz():
#     global m_score    
#     if m_score >=3:
#         print("elephant room")
#     else:
#         print("multiple choice room")

maths_quiz()