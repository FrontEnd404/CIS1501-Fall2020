import random
print("Hello")
print("Lets play agame.")
print("I'm going to pick a whole random number between 0 and a maximum number and you get to choose what the maximum number is")
max_number = input("what would you like the whole maximum number to be?")
max_number =int(max_number)
good_number = random.randint(0, max_number)

user_number = input("good now what do you think the random number is?")
user_number = int(user_number)

if good_number == user_number:
    print("good job you guessed the correct number")
else:
    print("sorry that is not the correct number")
    print("you have four more trys left")
    user_number2 =input("what do you think the number is now")
    if good_number == user_number2:
        print("good you got the number in two trys")
    else:
        print("sorry that is not the correct number")
        print("you have three more trys left")
        user_number3 = ("what do you think the number is now")
        if good_number == user_number3:
            print("good you got the number in three trys")
        else:
            print("sorry that is not the correct number")
            print("you have two more trys left")
            user_number4 = input("what do you think the number is now")
            if good_number == user_number4:
                print("good you got the number in four trys")
            else:
                print("sorry that is not the correct number")
                print("you have one more try left")
                user_number5 = input("what do you think the number is now")
                if good_number == user_number5:
                    print("good you got the number in five trys")
                else:
                    print("sorry that is not the correct number")
                    print("you ran out of trys you lose")








