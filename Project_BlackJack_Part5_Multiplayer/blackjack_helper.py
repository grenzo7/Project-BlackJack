from random import randint

def print_card_name(card_rank):
    # Implement card_name function here
    if card_rank == 1:
    # A 1 stands for an ace.
        card_name = "Ace"
    elif card_rank == 11:
    # An 11 stands for a jack.
        card_name = "Jack"
    elif card_rank == 12:
    # A 12 stands for a queen.
        card_name = "Queen"
    elif card_rank == 13:
    # A 13 stands for a king.
        card_name = "King"
    else:
    # All other cards are named by their
    # number, or rank.
        card_name = str(card_rank)

    if card_rank == 1 or card_rank == 8:
        drew_prefix = 'Drew an '
    else:
        drew_prefix = 'Drew a '

    if card_rank < 1 or card_rank > 13:
        print('BAD CARD')
    else:
        print(drew_prefix + card_name)

def draw_card():
   
    cardvalue_dict={1:"Ace",2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:"Jack",12:"Queen",13:"King"}
    card=randint(1,13)
   
    print_card_name(card)
    if card==11 or card==12 or card==13:
        card=10
        return card
    elif card==1:
        card=11
        return card
    else:
        return card

def print_header(message):
    
    print("-----------")
    print(str(message) )
    print("-----------")   


def draw_starting_hand(name):
    
    print_header(name+" TURN")
    card1=draw_card()
    card2=draw_card()
    hand_value=card1+card2
    return hand_value

def print_end_turn_status(hand_value):
    
    print("Final hand: {}.".format(hand_value) )
    if hand_value==21:
        print("BLACKJACK!")
    elif hand_value>21:
        print("BUST.")


def print_end_game_status(user_hand, dealer_hand):
  
    print_header("GAME RESULT")
    if user_hand<21:
        if dealer_hand<21:
            if user_hand<dealer_hand:
                print("Dealer wins!")
            elif user_hand>dealer_hand:
                print("You win!")
            else:
                print("Push.")
        elif dealer_hand == 21:
            print("Dealer wins!")
        elif dealer_hand >21:
            print("You win!")
    elif user_hand>21:
        print("Dealer wins!")
    elif user_hand==21:
        if dealer_hand ==21:
            print("Push.")
        else:
            print("You win!")
