import random

game_number = 1
turn_list = []
master_average_turn_list = []

while game_number <= 100:
    card_deck_list = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9,
                      10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14]
    card_deck_list2 = card_deck_list * 2
    card_deck_list3 = card_deck_list * 3
    card_deck_list4 = card_deck_list * 4
    card_deck_list5 = card_deck_list * 5

    random.shuffle(card_deck_list)

    total_cards = (len(card_deck_list))
    print(total_cards)

    player_1_card_deck = []
    player_2_card_deck = []
    stack_the_winner_takes = []
    player_1_card_deck = card_deck_list[:len(card_deck_list) // 2]
    player_2_card_deck = card_deck_list[len(card_deck_list) // 2:]

    number_of_turns = 0
    small_war = 'no'
    no_war = 'no'

    while len(player_1_card_deck) and len(player_2_card_deck) != 0:
        #print(player_1_card_deck)
        #print(player_2_card_deck)
        print(number_of_turns)
        if len(player_1_card_deck) < 4 or len(player_2_card_deck) < 4:
            small_war = 'yes'
        if len(player_1_card_deck) == 1 or len(player_2_card_deck) == 1:
            no_war = 'yes'
        p1_drawn_card = player_1_card_deck.pop(0)
        p2_drawn_card = player_2_card_deck.pop(0)
        print("player one drew", p1_drawn_card)
        print("player one drew",p2_drawn_card)
        stack_the_winner_takes.append(p1_drawn_card)
        stack_the_winner_takes.append(p2_drawn_card)

        if p1_drawn_card > p2_drawn_card:
            player_1_card_deck = stack_the_winner_takes + player_1_card_deck
            print("player1 wins these cards")
            print(stack_the_winner_takes)
        elif p2_drawn_card > p1_drawn_card:
            player_2_card_deck = stack_the_winner_takes + player_2_card_deck
            print("player2 wins these cards")
            print(stack_the_winner_takes)


        elif small_war == 'no' and p2_drawn_card == p1_drawn_card:
            print("war")
            p1_war_card1 = player_1_card_deck.pop(0)
            p1_war_card2 = player_1_card_deck.pop(0)
            p2_war_card1 = player_2_card_deck.pop(0)
            p2_war_card2 = player_2_card_deck.pop(0)
            stack_the_winner_takes.append(p1_war_card1)
            stack_the_winner_takes.append(p1_war_card2)
            stack_the_winner_takes.append(p2_war_card1)
            stack_the_winner_takes.append(p2_war_card2)
            print(stack_the_winner_takes)
            small_war = 'no'
            no_war = 'no'
            continue
        elif p2_drawn_card == p1_drawn_card and small_war == 'yes' and no_war == 'no':
            p1_war_card1 = player_1_card_deck.pop(0)
            p2_war_card2 = player_2_card_deck.pop(0)
            small_war = 'no'
            no_war = 'no'
            continue
        elif p1_drawn_card == p2_drawn_card and no_war == 'yes':
            print("game over")
            player_1_card_deck = []
            player_2_card_deck = []
            continue

        number_of_turns = number_of_turns + 1
        small_war = 'no'
        stack_the_winner_takes.clear()

    print("number of turns in game number", game_number, "=", number_of_turns)
    turn_list.append(number_of_turns)
    print(turn_list)
    game_number = game_number + 1

sum_of_turn_list = sum(turn_list)
average_number_of_turns = sum_of_turn_list / 100
master_average_turn_list.append(average_number_of_turns)
print(average_number_of_turns)
game_number = 2





turn_list = []


while game_number <= 100:
    card_deck_list1 = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9,
                      10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14]
    card_deck_list2 = card_deck_list1 * 2
    card_deck_list3 = card_deck_list * 3
    card_deck_list4 = card_deck_list * 4
    card_deck_list5 = card_deck_list * 5

    random.shuffle(card_deck_list2)

    total_cards = (len(card_deck_list2))
    print(total_cards)

    player_1_card_deck = []
    player_2_card_deck = []
    stack_the_winner_takes = []
    player_1_card_deck = card_deck_list2[:len(card_deck_list2) // 2]
    player_2_card_deck = card_deck_list2[len(card_deck_list2) // 2:]

    number_of_turns = 0
    small_war = 'no'
    no_war = 'no'

    while len(player_1_card_deck) and len(player_2_card_deck) != 0:
        #print(player_1_card_deck)
        #print(player_2_card_deck)
        print(number_of_turns)
        if len(player_1_card_deck) < 4 or len(player_2_card_deck) < 4:
            small_war = 'yes'
        if len(player_1_card_deck) == 1 or len(player_2_card_deck) == 1:
            no_war = 'yes'
        p1_drawn_card = player_1_card_deck.pop(0)
        p2_drawn_card = player_2_card_deck.pop(0)
        print("player one drew", p1_drawn_card)
        print("player one drew", p2_drawn_card)
        stack_the_winner_takes.append(p1_drawn_card)
        stack_the_winner_takes.append(p2_drawn_card)

        if p1_drawn_card > p2_drawn_card:
            player_1_card_deck = stack_the_winner_takes + player_1_card_deck
            print("player1 wins these cards")
            print(stack_the_winner_takes)
        elif p2_drawn_card > p1_drawn_card:
            player_2_card_deck = stack_the_winner_takes + player_2_card_deck
            print("player2 wins these cards")
            print(stack_the_winner_takes)


        elif small_war == 'no' and p2_drawn_card == p1_drawn_card:
            print("war")
            p1_war_card1 = player_1_card_deck.pop(0)
            p1_war_card2 = player_1_card_deck.pop(0)
            p2_war_card1 = player_2_card_deck.pop(0)
            p2_war_card2 = player_2_card_deck.pop(0)
            stack_the_winner_takes.append(p1_war_card1)
            stack_the_winner_takes.append(p1_war_card2)
            stack_the_winner_takes.append(p2_war_card1)
            stack_the_winner_takes.append(p2_war_card2)
            print(stack_the_winner_takes)
            small_war = 'no'
            no_war = 'no'
            continue
        elif p2_drawn_card == p1_drawn_card and small_war == 'yes' and no_war == 'no':
            p1_war_card1 = player_1_card_deck.pop(0)
            p2_war_card2 = player_2_card_deck.pop(0)
            small_war = 'no'
            no_war = 'no'
            continue
        elif p1_drawn_card == p2_drawn_card and no_war == 'yes':
            print("game over")
            player_1_card_deck = []
            player_2_card_deck = []
            continue

        number_of_turns = number_of_turns + 1
        small_war = 'no'
        stack_the_winner_takes.clear()

    print("number of turns in game number", game_number, "=", number_of_turns)
    turn_list.append(number_of_turns)
    print(turn_list)
    game_number = game_number + 1

sum_of_turn_list = sum(turn_list)
average_number_of_turns = sum_of_turn_list / 100
master_average_turn_list.append(average_number_of_turns)
print(average_number_of_turns)
print(master_average_turn_list)
game_number = 3
turn_list = []



while game_number <= 100:
    card_deck_list1 = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9,
                      10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14]
    card_deck_list2 = card_deck_list1 * 2
    card_deck_list3 = card_deck_list1 * 3
    card_deck_list4 = card_deck_list1 * 4
    card_deck_list5 = card_deck_list1 * 5

    random.shuffle(card_deck_list2)

    total_cards = (len(card_deck_list2))
    print(total_cards)

    player_1_card_deck = []
    player_2_card_deck = []
    stack_the_winner_takes = []
    player_1_card_deck = card_deck_list3[:len(card_deck_list3) // 2]
    player_2_card_deck = card_deck_list3[len(card_deck_list3) // 2:]

    number_of_turns = 0
    small_war = 'no'
    no_war = 'no'

    while len(player_1_card_deck) and len(player_2_card_deck) != 0:
        #print(player_1_card_deck)
        #print(player_2_card_deck)
        print(number_of_turns)
        if len(player_1_card_deck) < 4 or len(player_2_card_deck) < 4:
            small_war = 'yes'
        if len(player_1_card_deck) == 1 or len(player_2_card_deck) == 1:
            no_war = 'yes'
        p1_drawn_card = player_1_card_deck.pop(0)
        p2_drawn_card = player_2_card_deck.pop(0)
        print("player one drew", p1_drawn_card)
        print("player one drew", p2_drawn_card)

        stack_the_winner_takes.append(p1_drawn_card)
        stack_the_winner_takes.append(p2_drawn_card)

        if p1_drawn_card > p2_drawn_card:
            player_1_card_deck = stack_the_winner_takes + player_1_card_deck
            print("player1 wins these cards")
            print(stack_the_winner_takes)
        elif p2_drawn_card > p1_drawn_card:
            player_2_card_deck = stack_the_winner_takes + player_2_card_deck
            print("player2 wins these cards")
            print(stack_the_winner_takes)


        elif small_war == 'no' and p2_drawn_card == p1_drawn_card:
            print("war")
            p1_war_card1 = player_1_card_deck.pop(0)
            p1_war_card2 = player_1_card_deck.pop(0)
            p2_war_card1 = player_2_card_deck.pop(0)
            p2_war_card2 = player_2_card_deck.pop(0)
            stack_the_winner_takes.append(p1_war_card1)
            stack_the_winner_takes.append(p1_war_card2)
            stack_the_winner_takes.append(p2_war_card1)
            stack_the_winner_takes.append(p2_war_card2)
            print(stack_the_winner_takes)
            small_war = 'no'
            no_war = 'no'
            continue
        elif p2_drawn_card == p1_drawn_card and small_war == 'yes' and no_war == 'no':
            p1_war_card1 = player_1_card_deck.pop(0)
            p2_war_card2 = player_2_card_deck.pop(0)
            small_war = 'no'
            no_war = 'no'
            continue
        elif p1_drawn_card == p2_drawn_card and no_war == 'yes':
            print("game over")
            player_1_card_deck = []
            player_2_card_deck = []
            continue

        number_of_turns = number_of_turns + 1
        small_war = 'no'
        stack_the_winner_takes.clear()

    print("number of turns in game number", game_number, "=", number_of_turns)
    turn_list.append(number_of_turns)
    print(turn_list)
    game_number = game_number + 1

sum_of_turn_list = sum(turn_list)
average_number_of_turns = sum_of_turn_list / 100
master_average_turn_list.append(average_number_of_turns)
print(average_number_of_turns)
print(master_average_turn_list)
game_number = 4

print("the average number of turns for a game with 1 decks is:", master_average_turn_list[0])
print("the average number of turns for a game with 2 decks is:", master_average_turn_list[1])
print("the average number of turns for a game with 3 decks is:", master_average_turn_list[2])