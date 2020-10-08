
import random

total_winnings = 0
total_spent = 0

print("only whole numbers 1-9 are allowed")
print("input numbers one at a time")
player_choose = input("choose y to input your number r to get random numbers and x to stop playing")

while player_choose == "y" or player_choose == "r":
    # PICKS WINNING NUMBERS
    i = 0
    winning_number = []
    while i < 4:
        i += 1
        winning_number.append(random.randint(1, 9))
    if player_choose == "y":
        # Get user numbers
        i = 0
        user_number = []
        while i < 4:
            number = input("input a number")
            try:
                number = int(number)
            except ValueError:
                print("that is not a valid number please input a new one")
                continue
            if number >= 1 and number <= 9:
                user_number.append(number)
                i += 1
            else:
                print("number must be between 1 and 9")
                continue
    else:
        # get random numbers
        i = 0
        user_number = []
        while i < 4:
            i += 1
            user_number.append(random.randint(1, 9))
    # Process numbers
    print("the winning numbers are")
    print(winning_number)
    print("your numbers are")
    print(user_number)
    if user_number == winning_number:
        print("you win")
        total_spent = total_spent + 1
        total_winnings = total_winnings + 5000
    elif user_number[1] == winning_number[1] and user_number[2] == winning_number[2] and (user_number[0] == winning_number[0] or user_number[3] == winning_number[3]):
        print("you got a one off win")
        total_spent = total_spent + 1
        total_winnings = total_winnings + 275
    else:
        print("you did not win")
        total_spent = total_spent + 1
    print("your total winnings are $" + str(total_winnings) + " and you spent a total of $" + str(total_spent))
    player_choose = input("choose y to input your number r to get random numbers and x to stop playing")
print("thanks for playing")


