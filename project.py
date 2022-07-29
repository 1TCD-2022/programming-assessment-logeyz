"""
Auther: Logan Zuidhoek
Description: This program will ask you a series of questions around anime/manga
and you will be givin the option true or false.
date: july 2022
"""
import random

continue_play = True
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

correct_answers = ["y","yes","yeah","t","true"]
incorrect_answers = ["n",'no','nope','f','false']
while continue_play:
    question=random.choice(questions)
    user_input = input(str(f"{question[0]} >")).lower()

    if user_input in correct_answers:
        user_input = True
    elif user_input in incorrect_answers:
        user_input = False
    else:
        user_input = "incorrect"
    if user_input == question[1]:
        print ('you got it')
    else:
        print('inncorect, try again')
        
    


    
    

