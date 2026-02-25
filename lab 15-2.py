import os
while True:
    print("Login/Signup Menu")
    print("1. Login")
    print("2. Signup")
    print("3. Exit")
    choice = input("Please input: ")

    if choice == '1':
        print('Login')
        user_id = input("Please input an ID: ")
        password = input("Please input a Password: ")
        

        if os.path.exists("id.txt") and os.path.exists("pass.txt"):
            with open("id.txt", "r") as id_file, open("pass.txt", "r") as pass_file:
                ids = id_file.read().splitlines()
                passwords = pass_file.read().splitlines()
                if user_id in ids:
                    index = ids.index(user_id)
                    if passwords[index] == password:
                        print("Welcome back",user_id)

                        while True:
                            print('Main Menu')
                            print('1. Utility')
                            print('2. Game')
                            print('3. Multimedia')
                            print('4. Log out')
                            user = input('What do you want? ')
                            if user == '4':
                                print('You are log out!!\n')
                                break
                            elif user == '1':
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
                                    print('2. Black')
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
                                    print('2. Camera')
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
                        print("Incorrect password.\n")
                else:
                    print("ID not found.\n")
        else:
            print("ID or Password is incorrect!!\n")

    elif choice == '2':
        print('Sign Up')
        user_id = input("Create your ID: ")
        password = input("Create your Password: ")
        with open("id.txt", "a") as id_file, open("pass.txt", "a") as pass_file:
            id_file.write(user_id + "\n")
            pass_file.write(password + "\n")
        

    elif choice == '3':
        print("Thank you! Bye\n")
        break

    else:
        print("Invalid input. Please try again.\n")