"""
Auther: Logan Zuidhoek
Description: This program will ask you a series of questions around anime/manga
and you will be givin the option true or false.
date: july 2022
"""
import random

continue_play = True

             
#questions
q1 = ['(BLEACH)- Ichigo has full controll of his bankai t/f',False]
q2 = ["(BLEACH)- White took over ichigo's body because he died fighting Ulquiorra t/f ",True]
q3 = ["(AOT)- Eren is actully putting on an act as the villan to save his friends and stop the war t/f ",True]
q4 = ['(JJK)- Yuji has control over sukuna t/f ',True]
q5 = ["(AOT)- The Ackerman's can turn into titans t/f ",False]
q6 = ["(OPM)- Saitama has no limit",True]
q7 = ["(JJK)- Yuji was a normal human before eating sukuna's finger t/f ",False]
q8 = ['(DS)- Tanjiro becomes a demon',True]
q9 = ['(OPM)- Saitama is so strong because of doing 100 push-ups, 100 sit-ups and a 10km run',False]
q10 = ['(DS)- Tanjiro only uses water breathing',False]
questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
#many diffrent answers that the user can use
correct_answers = ["y","yes","yeah","t","true"]
incorrect_answers = ["n",'no','nope','f','false']
score = 0
wrong = 0

print (''' Welcome to the true of false anime/manga quiz.

When asked a question you can answer with true or false and yes or no.
The anime/manga that the question is from will be in brackets at the start of the question.
When you are asked "Do you want anouther question to be asked" answering yes will make the program ask you anouther anime/manga question,
and no will end the program.

I hope you enjoy the quiz. Answer question bellow to begin!

''')
print()
#continue play is true, questions are asked until program is closed
while continue_play:
    question=random.choice(questions)
#formating the question,(doesn't show the answer at the end of the question.
    user_input = input(str(f"{question[0]} >")).lower()
    print ()
    #program, tells the user if they got it correct or not

    if user_input in correct_answers:
        user_input = True
    elif user_input in incorrect_answers:
        user_input = False
    else:
        user_input = "incorrect"
    if user_input == question[1]:
        print ('you got it')
        print()
        print ('you got', score + 1, 'right,','and', wrong, 'wrong')
        score += 1
        print()
    else:
        print('inncorect, try again')
        print()
        print ('you got', score, 'right,','and', wrong + 1, 'wrong')
        wrong += 1
        print()
    #asking user if they want another question asked, prints final score if
    #the program is ended
    want_to_continue = input('do you want anouther question to be asked? ')
    print()
    if want_to_continue in incorrect_answers:
        print ('your final score is ', score,', right and ', wrong,', wrong')
        continue_play = False


    
    

