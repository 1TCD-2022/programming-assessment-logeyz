"""
Auther: Logan Zuidhoek
Description: This program will ask you a series of questions around anime/manga
and you will be givin the option true or false.
date: july 2022
"""
import random

continue_play = True

             
#questions
q1 = ['Bleach was released in 2006',False]
q2 = ['Cowbow Bebop is a good show',True]
q3 = ['Attack on titan more like attack',True]
q4 = ['Bingus the anime should come out.',True]
q5 = ['Minions movie is an anime',False]
q6 = ["Slippin' Jimmy is an anime",True]
q7 = ['1+1=3',False]
q8 = ['Logan is a musical',True]
q9 = ['gabagabadoo schmoo?',False]
q10 = ['anime more like nime',False]
questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
#many diffrent answers that the user can use
correct_answers = ["y","yes","yeah","t","true"]
incorrect_answers = ["n",'no','nope','f','false']
score = (0)
wrong = (0)
#continue play is true, questions are asked until program is closed
while continue_play:
    question=random.choice(questions)
#formating the question,(doesn't show the answer at the end of the question.
    user_input = input(str(f"{question[0]} >")).lower()
    #program, tells the user if they got it correct or not

    if user_input in correct_answers:
        user_input = True
    elif user_input in incorrect_answers:
        user_input = False
    else:
        user_input = "incorrect"
    if user_input == question[1]:
        print ('you got it')
        print ('you got', score + 1, 'right,','and', wrong, 'wrong')
        score += 1
        
    else:
        print('inncorect, try again')
        print ('you got', score, 'right,','and', wrong + 1, 'wrong')
        wrong += 1
        
    #asking user if they want another question asked, 
    want_to_continue = input('do you want anouther question to be asked? ')
    if want_to_continue in incorrect_answers:
        continue_play = False


    
    

