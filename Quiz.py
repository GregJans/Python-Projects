def normal_quiz():
    import random
    x = 1
    questions = ['How many clubs does our school have? (not including sports teams)' , 'True or false: Our school has a room 100C' ,
                 'True or false: Our school has a pledge.' , 'Which teacher has been teaching at Christ the King the longest?' , 'Which C.K. sport has never won the City Championship' ,
                 'Who is famous for this quote: \"Sir, tuck in your pants\"' , 'Which subject has Mr. Jans never tought: Computer, Science, English, Math' ,
                 'Which chappel used to be an all girl\'s chappel: the A side or B side' , 'Which current teacher has not graduated from Christ the King: Scalfaro, Munoz, Bellington, Mueller']
    
    
    
    answers = ['18'  , 'true' , 'true' , 'bellington' , 'football' , 'ouellette' , 'math' , 'a side' , 'mueller']
    
    facts = ['C.K offers a variety of clubs and activities to its students.' , 'Room 100C is the band room located across from the boy\'s locker room.' ,
             'The school has always had its own pledge, although it is rarely ever used.' , '' , 'It\'s sad but true. Maybe next time Royals!' ,
             'Did you know Mr. Ouellette also has a chant spelling out his name?' , 'Mr. Jans did in fact have to take over teaching an English class for the second half of a school year.' ,
             'Our school used to actually be two schools (an all boys and all girls school). The girls had the A-side.' , '']
    
    user_score = int(0)
    for x in range(0,5):
        question_number = random.randint(0,3)
        question = questions[question_number]
        answer = answers[question_number]
        info = facts[question_number]
        print(question)
        user_answer = input()
        if user_answer.lower() == answer:
            print('Correct!')
            print(info)
            user_score += 1
            print(f"Your score so far is {user_score} point(s)!\n")
        else:
            print(f'Incorrect, the answr is {answer}')
            print(info)
            print(f'Your score is still {user_score} point(s).\n')
        questions.remove(question)
        answers.remove(answer)
        facts.remove(info)
        x += 1
    if user_score > 2:
        print(f'\nCongratulations, you passed with a score of {user_score} point(s)\n')
    else:
        print(f'\nSory, but you failed with a score of {user_score} point(s)\n')
    
    
    
    
normal_quiz()