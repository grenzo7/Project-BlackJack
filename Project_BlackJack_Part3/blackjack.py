from blackjack_helper import *



#User Turn

user_hand=draw_starting_hand("YOUR")
while user_hand<21:
  ans=input(f"You have {user_hand}. Hit (y/n)? ")
  if ans=="y":
      user=draw_card()
      user_hand+=user
  elif ans=="n":
    break
  else:
    print("Sorry I didn't get that.")

print_end_turn_status(user_hand)

#Dealer Turn

dealer_hand=draw_starting_hand("DEALER")
while dealer_hand<17:
    print("Dealer has {}.".format(dealer_hand))
    dealer=draw_card()
    dealer_hand+=dealer


print_end_turn_status(dealer_hand)
print_end_game_status(user_hand,dealer_hand)
