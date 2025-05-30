import random as rd
default = False
game = True
i = 0
while game:
    if default == False:
        print("Enter the range of the numbers you want to play with : ")
        try:
            start = int(input("From : "))
            end = int(input("End : "))
            if start<0 or end<start:
                raise ValueError("Number must be greater than or equal to 0")
            else:
                 random_num = rd.randint(start,end)
        except Exception as e:
            print("Please enter a valid number. Number must be greater or equal to 0")
        print("Lets begin the game!!")
        default = True
    #takes user input 
    try:
        value = int(input(f"Enter the number between {start}-{end}: "))
        if value<start or value>end:
            raise ValueError(f"Number must be within the given range {start} - {end}")
    except Exception as e:
        print("Enter a valid input")
        continue
    if value<random_num:
        print("too low")
        i += 1
    elif value>random_num:
        print("too high")
        i += 1
    elif value==random_num:
        print("You win!")
        break
    else:
        pass
    if i == 3:
        print("Too many attempts you lose! Bye! Better luck next time!")
        game = False
    if i == 3:
        ask = True
        while ask:
            try:
                play = input("Want to play again? (y/n) : ")
                if play not in ['n','y']:
                    raise ValueError("Enter a valid option! (y/n)")
            except ValueError as e:
                print("what? :-|")
                continue
            if play=='n':
                print("It was nice playing with you bye!")
                ask = False
                game = False
            else:
                print("Let's GO!")
                ask = False
                default = False
                i = 0
