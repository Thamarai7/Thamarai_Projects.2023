import random


def deal_card():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def cal_card(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    else:
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
    return sum(cards)


def compare(user_score, pc_score):
    if user_score > 21 and pc_score > 21:
        return "you went over,you lose"
    if user_score == pc_score:
        return "Draw"
    elif pc_score == 0:
        return "lose ,opponent has blackjack"
    elif user_score == 0:
        return "win with a Blackjack"
    elif user_score > 21:
        return "you lose"
    elif pc_score > 21:
        return "opponent went over ,you win"
    elif user_score > pc_score:
        return "you win"
    else:
        return "you lose"


def play():
    user_card = []
    pc_card = []
    is_game_over = True
    for _ in range(2):
        user_card.append(deal_card())
        pc_card.append(deal_card())

    while is_game_over:
        user_score = cal_card(user_card)
        pc_score = cal_card(pc_card)

        print(f"your card {user_card},score {user_score}")
        print(f"pc card {pc_card[1]}")
        if user_score == 0 or pc_score == 0 or user_score > 21:
            is_game_over = False
        else:
            choice = input("Do you want to get new card y or n")
            if choice == "y":
                user_card.append(deal_card())
                user_score = cal_card(user_card)
            else:
                is_game_over = False
        while pc_score != 0 and pc_score < 17:
            pc_card.append(deal_card())
            pc_score = cal_card(pc_card)
    res = compare(user_score, pc_score)
    print(f"Final version of your card {user_card}\n your score{user_score}")
    print(f"Final card's of pc {pc_card}\n pc score {pc_score}")
    print(res)
print("Welcome to BlackJack")
run = True
play_game = input("Do you want to play BlackJack ")
while run:

    if play_game == "y":
        play()
    else:
        run = False
        print("See you some time")