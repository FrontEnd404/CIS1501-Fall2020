number_grid = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]

skip = "no"
user = 1
keep_going1 = "yes"
win ="no"
for i in range(len(number_grid)):
    for x in number_grid:
        print(x[i], end =' ')
    print()

user_selected_drop_row = int
don_not_change_player = "no"


def place_token1():
    global user_selected_drop_row
    global skip
    print("player")
    print(user)
    user_selected_drop_row = int(input("which row would you like to drop it in (1-4)"))
    if number_grid [user_selected_drop_row-1][0] != 0:
        print("that row is to full you must choose another one")
        skip = "yes"
    elif number_grid [user_selected_drop_row-1][1] != 0:
        number_grid [user_selected_drop_row-1][0] = 1
    elif number_grid [user_selected_drop_row-1][2] != 0:
        number_grid [user_selected_drop_row-1][1] = 1
    elif number_grid [user_selected_drop_row-1][3] != 0:
        number_grid [user_selected_drop_row-1][2] = 1
    else:
        number_grid[user_selected_drop_row - 1][3] = 1

def place_token2():
    global user_selected_drop_row
    global skip
    print("player")
    print(user)
    user_selected_drop_row = int(input("which row would you like to drop it in (1-4)"))
    if number_grid [user_selected_drop_row-1][0] != 0:
        print("that row is to full you must choose another one")
        skip = "yes"
    elif number_grid [user_selected_drop_row-1][1] != 0:
        number_grid [user_selected_drop_row-1][0] = 2
    elif number_grid [user_selected_drop_row-1][2] != 0:
        number_grid [user_selected_drop_row-1][1] = 2
    elif number_grid [user_selected_drop_row-1][3] != 0:
        number_grid [user_selected_drop_row-1][2] = 2
    else:
        number_grid[user_selected_drop_row - 1][3] = 2


def check_for_vertical_win():
    global win
    if number_grid [0][0] == 1 and number_grid [0][1] ==1 and number_grid [0][2] ==1 and number_grid [0][3] ==1:
        print("you win")
        win = "yes"
    elif number_grid [1][0] == 1 and number_grid [1][1] ==1 and number_grid [1][2] ==1 and number_grid [1][3] ==1:
        print("you win")
        win = "yes"
    elif number_grid [2][0] == 1 and number_grid [2][1] ==1 and number_grid [2][2] ==1 and number_grid [2][3] ==1:
        print("you win")
        win = "yes"
    elif number_grid [3][0] == 1 and number_grid [3][1] ==1 and number_grid [3][2] ==1 and number_grid [3][3] ==1:
        print("you win")
        win = "yes"
    elif number_grid [0][0] == 2 and number_grid [0][1] ==2 and number_grid [0][2] ==2 and number_grid [0][3] ==2:
        print("you win")
        win = "yes"
    elif number_grid [1][0] == 2 and number_grid [1][1] ==2 and number_grid [1][2] ==2 and number_grid [1][3] ==2:
        print("you win")
        win = "yes"
    elif number_grid [2][0] == 2 and number_grid [2][1] ==2 and number_grid [2][2] ==2 and number_grid [2][3] ==2:
        print("you win")
        win = "yes"
    elif number_grid [3][0] == 2 and number_grid [3][1] ==2 and number_grid [3][2] ==2 and number_grid [3][3] ==2:
        print("you win")
        win = "yes"


def check_for_horizontal_win():
    global win
    if number_grid[0][0] == 1 and number_grid[1][0] == 1 and number_grid[2][0] == 1 and number_grid[3][0] == 1:
        print("you win")
        win = "yes"
    elif number_grid[0][1] == 1 and number_grid[1][1] == 1 and number_grid[2][1] == 1 and number_grid[3][1] == 1:
        print("you win")
        win = "yes"
    elif number_grid[0][2] == 1 and number_grid[1][2] == 1 and number_grid[2][2] == 1 and number_grid[3][2] == 1:
        print("you win")
        win = "yes"
    elif number_grid[0][3] == 1 and number_grid[1][3] == 1 and number_grid[2][3] == 1 and number_grid[3][3] == 1:
        print("you win")
        win = "yes"
    elif number_grid[0][0] == 2 and number_grid[1][0] == 2 and number_grid[2][0] == 2 and number_grid[3][0] == 2:
        print("you win")
        win = "yes"
    elif number_grid[0][1] == 2 and number_grid[1][1] == 2 and number_grid[2][1] == 2 and number_grid[3][1] == 2:
        print("you win")
        win = "yes"
    elif number_grid[0][2] == 2 and number_grid[1][2] == 2 and number_grid[2][2] == 2 and number_grid[3][2] == 2:
        print("you win")
        win = "yes"
    elif number_grid[0][3] == 2 and number_grid[1][3] == 2 and number_grid[2][3] == 2 and number_grid[3][3] == 2:
        print("you win")
        win = "yes"


def check_for_diagonal_win():
    global win
    if number_grid[3][0] == 1 and number_grid[2][1] == 1 and number_grid[1][2] == 1 and number_grid[0][3] == 1:
        print("you win")
        win = "yes"
    elif number_grid[3][3] == 1 and number_grid[2][2] == 1 and number_grid[1][1] == 1 and number_grid[0][0] == 1:
        print("you win")
        win = "yes"
    elif number_grid[3][0] == 2 and number_grid[2][1] == 2 and number_grid[1][2] == 2 and number_grid[0][3] == 2:
        print("you win")
        win = "yes"
    elif number_grid[3][3] == 2 and number_grid[2][2] == 2 and number_grid[1][1] == 2 and number_grid[0][0] == 2:
        print("you win")
        win = "yes"

def change_user():
    global user
    if user ==1:
        user = user + 1
    elif user == 2:
        user = user -1

def check_for_tie():
    global win
    if number_grid [3][0] != 0 and number_grid [3][1] != 0  and number_grid [3][2] != 0 and number_grid [3][3] != 0:
        print("the game ends in a tie")
        win = "yes"











while win == "no":
    if user == 1:
        place_token1()
    elif user == 2:
        place_token2()
    elif don_not_change_player == "yes":
        don_not_change_player = "no"



    check_for_vertical_win()
    check_for_horizontal_win()
    check_for_diagonal_win()
    check_for_tie()
    if skip == "no":
      change_user()
    elif skip == "yes":
        skip = "no"
        continue
    keep_going1 = "yes"
    for i in range(len(number_grid)):
        for x in number_grid:
            print(x[i], end=' ')
        print()