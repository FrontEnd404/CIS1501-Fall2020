import random
# takes user input
number_of_sides = int(input("How many sides do you want the dice to have?"))
number_of_dice_rolls = int(input("How many dice do you want to roll?"))
total_number_of_rolls = int(input("How many times do you want to roll the dice?"))
 # initialize var
dice_totals_to_sum = []
sums_of_all_the_sums = []
rolls_so_far_ = 0
total_number_of_rolls_so_far = 1
pos_numbers_for_sum_of_dice = number_of_sides * number_of_dice_rolls
displayed_so_far = 1
list_of_number_of_times_a_sum_occurs = []
# simulates the die rolls
while number_of_dice_rolls >= rolls_so_far_ and total_number_of_rolls >= total_number_of_rolls_so_far:
    if number_of_dice_rolls == rolls_so_far_:
        sums_of_all_the_sums.append(sum(dice_totals_to_sum))
        dice_totals_to_sum.clear()
        total_number_of_rolls_so_far = total_number_of_rolls_so_far + 1
        rolls_so_far_ = 0
        continue
    else:
        dice_totals_to_sum.append(random.randint(1, number_of_sides))
        rolls_so_far_ = rolls_so_far_ + 1
# can be used to make sure the numbers are correct
# print(sums_of_all_the_sums)
# print(sorted(sums_of_all_the_sums))

# prints histogram
while pos_numbers_for_sum_of_dice >= displayed_so_far:
    print(str(displayed_so_far) + ":" + str(sums_of_all_the_sums.count(displayed_so_far)))
    displayed_so_far = displayed_so_far + 1



