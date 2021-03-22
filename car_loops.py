car_started = False
answer = ''
while True:
    answer = input('> ').lower()

    with open('test.txt', 'a') as f:
        f.write(answer + '\n')
    if answer == 'help':
        print('''
Start - starts the car
Stop - stops the car
Quit - quit
            ''')  
    elif answer == 'start':
        if not car_started:
            print('Car started...Ready to go!')
            car_started = True
        else:
            print('Car is alredy started')
    elif answer == 'stop':
        if car_started:
            print('Car stopped.')
            car_started = False
        else:
            print('Car is already stopped')
    elif answer == 'quit':
        break    
    else:
        print("I don't understand that...")
print("dammit, my final message")        
