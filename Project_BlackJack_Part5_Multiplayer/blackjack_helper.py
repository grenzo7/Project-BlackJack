from random import randint


def starter(players):
  scores_dict = {}
  for i in range(1,players+1):
    player_i = input(f"What is player {i}'s name? ")
    scores_dict[player_i] = [0,3]
  return scores_dict

def print_card_name(card_rank):
  if card_rank == 1:
    card_name = 'Ace'
  elif card_rank == 11:
    card_name = 'Jack'
  elif card_rank == 12:
    card_name = 'Queen'
  elif card_rank == 13:
    card_name = 'King'
  else:
    card_name = card_rank

  if card_rank == 8 or card_rank == 1:
    print('Drew an ' + str(card_name))
  elif card_rank < 1 or card_rank > 13:
    print('BAD CARD')
  else:
    print('Drew a ' + str(card_name))


def draw_card():
  card_rank = randint(1, 13)
  print_card_name(card_rank)

  if card_rank == 11 or card_rank == 12 or card_rank == 13:
    card_value = 10
  elif card_rank == 1:
    card_value = 11
  else:
    card_value = card_rank

  return card_value


def print_header(message):
  print('-----------')
  print(message)
  print('-----------')


def draw_starting_hand(name):
  print_header(name + ' TURN')
  return draw_card() + draw_card()


def print_end_turn_status(player,player_hand,scores_dict):
  print('Final hand: ' + str(player_hand) + '.')

  if player_hand == 21:
    print('BLACKJACK!')
  elif player_hand > 21:
    print('BUST.')
  scores_dict[player][0] = player_hand
  return scores_dict 

def print_end_game_status(player_hand, dealer_hand,scores_dict):
  print_header('GAME RESULT')
  updated_dict = {}
  for player in scores_dict:
    if player == "Dealer":
      continue
    if scores_dict[player][0] > scores_dict["Dealer"][0] and scores_dict[player][0] <= 21:
      scores_dict[player][1] += 1
      print(f"{player} wins! Score : {scores_dict[player][1]}")
      
    elif (scores_dict[player][0] >= scores_dict["Dealer"][0] or scores_dict[player][0] <= scores_dict["Dealer"][0])  and scores_dict[player][0] > 21:
      scores_dict[player][1] -= 1
      print(f"{player} loses! Score: {scores_dict[player][1]}")
      
    elif scores_dict[player][0] < scores_dict["Dealer"][0] and scores_dict["Dealer"][0] <= 21:
      scores_dict[player][1] -= 1
      print(f"{player} loses! Score: {scores_dict[player][1]}")

    elif scores_dict[player][0] < scores_dict["Dealer"][0] and scores_dict["Dealer"][0] > 21:
      scores_dict[player][1] += 1
      print(f"{player} wins! Score : {scores_dict[player][1]}")
    elif scores_dict[player][0] == scores_dict["Dealer"][0]:
      print(f"{player} pushes! Score : {scores_dict[player][1]}")
    if scores_dict[player][1] <= 0:
      print(f"{player} eliminated!")
    else:
      updated_dict[player] = [0,scores_dict[player][1]]
  if updated_dict == {}:
    print("All players eliminated!")
  return updated_dict
