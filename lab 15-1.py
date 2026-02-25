print("Hello! nice to meet you")
print("My name is I.B.A short for Interactive Bot of Archives")
print("Are you here because you want me to recommend movies, books or games? your choice")
print("So what would it be")  
    

while True:
    print('Main Menu')
    print('1. Utility')
    print('2. Game')
    print('3. Multimedia')
    print('4. Exit')
    user = input('What do you want? ')
    if user == '4':
        print('Thank you! Bye\n')
        break
    elif user =='1':
        while True:
            print('Utility Menu')
            print('1. Calculator')
            print('2. Email')
            print('3. Note')
            print('4. Main Menu')
            user = input('What do you want? ')
            if user == '4':
                break
            elif user == '1':
                print("I am sorry. It's not ready yet.\n")
                break
            elif user == '2':
                print("I am sorry. It's not ready yet.\n")
                break
            elif user == '3':
                print("I am sorry. It's not ready yet.\n")
                break
            else:
                print("I am sorry. Please input correctly.\n")
    elif user == '2':
        while True:
            print('Game Menu')
            print('1. Poker')
            print('2. Black ')
            print('3. Main Menu')
            user = input('What do you want? ')
            if user == '3':
                break
            elif user == '1':
                print("I am sorry. It's not ready yet.\n")
                break
            elif user == '2':
                print("I am sorry. It's not ready yet.\n")
                break
            else:
                print("I am sorry. Please input correctly.\n")
    elif user == '3':
        while True:
            print('Multimedia Menu')
            print('1. Music Player')
            print('2. Camera ')
            print('3. Music Download')
            print('4. Main Menu')
            user = input('What do you want? ')
            if user == '4':
                break
            elif user == '1':
                print("I am sorry. It's not ready yet.\n")
                break
            elif user == '2':
                print("I am sorry. It's not ready yet.\n")
                break       
            elif user == '3':
                print("I am sorry. It's not ready yet.\n")
                break
            else:
                print("I am sorry. Please input correctly.\n")
    else:
        print("I am sorry. Please input correctly.\n")