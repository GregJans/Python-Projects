import random

def normalQuiz():
    global hard_mode_unlocked

    questions = ['How many bones are there in the human body?' , 'Which U.S. state is known for peaches?' ,
                 'Which fictional city is the home of Batman?' , 'Which planet is closest to Earth?' , 'Fe is the chemical symbol for which element?' ,
                 'What temperature (in Fahrenheit) does water freeze at?' , 'What language is the most popularly spoken worldwide?' ,
                 'What has a gravitational pull so strong that light cannot even escape it?' , 'What vegetable is known to help you see in the dark?']



    answers = ['206'  , 'georgia' , 'gotham' , 'venus' , 'iron' , '32' , 'chinese' , 'black hole' , 'carrot']


    user_score = 0
    for x in range(0,5):
        #Use random number instead of choice in order to have the position of the answer in the list
        question_number = random.randint(0,len(questions) - 1)
        question = questions[question_number]
        answer = answers[question_number]
        print(question)
        user_answer = input("\n\n> ")
        if answer in user_answer.lower():
            print('Correct!')
            user_score += 1
            print(f"Your score so far is {user_score} point(s)!\n")
        else:
            print(f'Incorrect, the answer is {answer}')
            print(f'Your score is still {user_score} point(s).\n')
        questions.remove(question)
        answers.remove(answer)

    if user_score > 3:
        print(f'\nCongratulations, you passed with a score of {user_score} point(s)\n')
        hard_mode_unlocked = True
        print('You may now play on hard mode!')
    else:
        print(f'\nSory, but you failed with a score of {user_score} point(s)\n')


def hardQuiz():
    questions = ['What is hummus made from?' , 'Which U.S. state is known as “America’s Dairyland”?' ,
                 'What animal is known as a "flamboyance" while in a group?' , 'Which U.S. State is the largest?' , 'Which astrological sign\'s symbol is a crab?' ,
                 'What is the #1 selling type of cookie in the United States?' , 'How many hearts does an octopus have?' ,
                 'Which country hosted the first Olympic Games in 1896?' , 'What is the rarest blood type?']



    answers = ['chickpea'  , 'wisconsin' , 'flamingo' , 'alaska' , 'cancer' , 'oreo' , '3' , 'greece' , 'ab negative']



    user_score = 0
    for x in range(0,5):
        #Use random number instead of choice in order to have the position of the answer in the list
        question_number = random.randint(0,len(questions) - 1)
        question = questions[question_number]
        answer = answers[question_number]
        print(question)
        user_answer = input("\n\n> ")
        if answer in user_answer.lower():
            print('Correct!')
            user_score += 1
            print(f"Your score so far is {user_score} point(s)!\n")
        else:
            print(f'Incorrect, the answer is {answer}')
            print(f'Your score is still {user_score} point(s).\n')
        questions.remove(question)
        answers.remove(answer)

    if user_score > 3:
        print(f'\nCongratulations, you passed with a score of {user_score} point(s)\n')

    else:
        print(f'\nSory, but you failed with a score of {user_score} point(s)\n')


hard_mode_unlocked = False

print('Alright lets do this!')
while True:
    quiz = input('\nWould you like the normal or hard quiz? (quit to stop)\n> ')
    if 'normal' in quiz.lower():
        #Run the normal quiz found in GameExtras
        normalQuiz()
    elif 'hard' in quiz.lower():
        #Make sure they passed the easy quiz first
        if hard_mode_unlocked:
            print('Get ready, these are hard!')
            hardQuiz()
        else:
            print('I\'m sorry, but you must first pass the easy quiz\n')

    elif quiz.lower() == 'quit':
        break
    else:
        print(f'Sory but {quiz} is not an option.')

print('Thank you for playing trivia. See you next time')
