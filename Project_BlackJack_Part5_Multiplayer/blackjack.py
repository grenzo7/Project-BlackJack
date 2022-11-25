
from blackjack_helper import *

players = int(input("Welcome to Blackjack! How many players? "))
scores_dict = starter(players)

ans = "y"
# USER'S TURN
while ans == "y":
  scores_dict["Dealer"] = [0,3]
  for player in scores_dict: 
    if player == "Dealer":
      continue
    player_hand = draw_starting_hand(player.upper() + "'S")
    should_hit = 'y'
    while player_hand < 21:
      should_hit = input("You have {}. Hit (y/n)? ".format(player_hand))
      if should_hit == 'n':
        break
      elif should_hit != 'y':
        print("Sorry I didn't get that.")
      else:
        player_hand = player_hand + draw_card()
    scores_dict = print_end_turn_status(player,player_hand,scores_dict)
    
  # DEALER'S TURN
  dealer_hand = draw_starting_hand("DEALER")
  while dealer_hand < 17:
    print("Dealer has {}.".format(dealer_hand))
    dealer_hand = dealer_hand + draw_card()
  scores_dict = print_end_turn_status("Dealer",dealer_hand,scores_dict)

  # GAME RESULT
  scores_dict = print_end_game_status(player_hand, dealer_hand,scores_dict)
  if scores_dict == {}:
    break
  ans = input("Do you want to play another hand (y/n) ")
