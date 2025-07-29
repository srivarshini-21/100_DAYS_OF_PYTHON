import random
logo=r'''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/           '''

def deal_card():
    """Returns random card from the deck"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    """Calculates score from cards list """
    if sum(cards)==21 and len(cards) ==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, comp_score):
    if user_score==comp_score:
        return "Draw 😯"
    elif comp_score==0:
        return "Lose, opponent has BlackJack 😱"
    elif user_score==0:
        return "Win with a BlackJack 😎"
    elif user_score>21:
        return "You went over. You lose 😭"
    elif comp_score>21:
        return "Opponent went over. You win 😁"
    elif user_score>comp_score:
        return "You win 🥳"
    else:
        return "You lose 😮‍💨"


def blackjack():
    print(logo)
    user_cards=[]
    comp_cards=[]
    comp_score= -1
    user_score= -1
    game_over=False
    
    for _ in range(2): # To assign 2 cards each to user and computer
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not game_over:
        user_score=calculate_score(user_cards)
        comp_score=calculate_score(comp_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")

        if user_score==0 or comp_score==0 or user_score>21:
            game_over=True
        else:
            another_card=input("Type 'y' to get another card, type 'n' to pass. ")
            if another_card=="y":
                user_cards.append(deal_card())
            else:
                game_over=True

    while comp_score!=0 and comp_score<17:
        comp_cards.append(deal_card())
        comp_score=calculate_score(comp_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score,comp_score))
    
while input("Do you want to play a game of BlackJack? Type 'y' or 'n' : ")=="y":
    print("\n" * 20)
    blackjack()
    
