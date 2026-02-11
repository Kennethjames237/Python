"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

    

def value_of_card(card):
    if(card in "JQK"):
        return 10
    elif(card == "A"):
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if(value_one == value_two):
        return card_one, card_two
    elif(value_one > value_two):
        return card_one
    else :
        return card_two
    

def value_of_ace(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    sum = value_one + value_two
    if(sum == 20):
        return 1
    elif(value_one==1 or value_two==1):
        return 1
    elif(12 <= sum <= 19):
        return 1;
    else :
        return 11

def is_blackjack(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if( (value_one==1 and value_two==10) or (value_one==10 and value_two==1) ):
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if(value_one == value_two):
        return True
    else:
        return False

def can_double_down(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    sum = value_one + value_two
    if(9 <= sum <= 11):
        return True
    else:
        return False
        
