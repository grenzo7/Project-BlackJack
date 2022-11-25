from blackjack_helper import *
from test_helper import *
import unittest

class TestBlackjackHelper(unittest.TestCase):

 
  def test_mock_randint_example(self):
    """
    Example of a test to compare output for a function that calls randint

    This does not count as one of your tests
    """
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)

 
  def test_print_card_name(self):
    self.assertEqual(get_print(print_card_name, 1),"Drew an Ace\n")
    self.assertEqual(get_print(print_card_name, 3),"Drew a 3\n")
    self.assertEqual(get_print(print_card_name, 10),"Drew a 10\n")
    self.assertEqual(get_print(print_card_name, 11),"Drew a Jack\n")
    self.assertEqual(get_print(print_card_name, 12),"Drew a Queen\n")
    self.assertEqual(get_print(print_card_name, 13),"Drew a King\n")
    self.assertEqual(get_print(print_card_name, 14),"BAD CARD\n")
    self.assertEqual(get_print(print_card_name, -1),"BAD CARD\n")
    self.assertEqual(get_print(print_card_name, 0),"BAD CARD\n")

  def test_mock_randint(self):
    self.assertEqual(mock_random([1], draw_card), 11)
    self.assertEqual(mock_random([2], draw_card), 2)
    self.assertEqual(mock_random([4], draw_card), 4)
    self.assertEqual(mock_random([11], draw_card), 10)
    self.assertEqual(mock_random([12], draw_card), 10)
    self.assertEqual(mock_random([13], draw_card), 10)
    self.assertEqual(mock_random([1,2], draw_starting_hand, "DEALER"), 13)
    self.assertEqual(mock_random([2,3], draw_starting_hand, "DEALER"), 5)
    self.assertEqual(mock_random([3,6], draw_starting_hand, "USER"), 9)
    self.assertEqual(mock_random([11,12], draw_starting_hand, "USER"), 20)
    self.assertEqual(mock_random([13,13], draw_starting_hand, "UTSAV"), 20)
    self.assertEqual(mock_random([14,13], draw_starting_hand, "UTSAV"), 24)
    self.assertEqual(mock_random([0,0], draw_starting_hand, "USER"), 0)
    self.assertEqual(mock_random([-1,-2], draw_starting_hand, "USER"), -3)

  def test_print_header(self):
    self.assertEqual(get_print(print_header,"USER"),"-----------\nUSER\n-----------\n")
    self.assertEqual(get_print(print_header,"DEALER"),"-----------\nDEALER\n-----------\n")
    self.assertEqual(get_print(print_header,"USER TURN"),"-----------\nUSER TURN\n-----------\n")
    self.assertEqual(get_print(print_header,"UTSAV TURN"),"-----------\nUTSAV TURN\n-----------\n")
    self.assertEqual(get_print(print_header,"GAME RESULT"),"-----------\nGAME RESULT\n-----------\n")
    
  def test_print_end_turn_status(self):
    self.assertEqual(get_print(print_end_turn_status,4),"Final hand: 4.\n")
    self.assertEqual(get_print(print_end_turn_status,6),"Final hand: 6.\n")
    self.assertEqual(get_print(print_end_turn_status,20),"Final hand: 20.\n")
    self.assertEqual(get_print(print_end_turn_status,0),"Final hand: 0.\n")
    self.assertEqual(get_print(print_end_turn_status,-1),"Final hand: -1.\n")
    self.assertEqual(get_print(print_end_turn_status,21),"Final hand: 21.\nBLACKJACK!\n")
    self.assertEqual(get_print(print_end_turn_status,22),"Final hand: 22.\nBUST.\n")

  def test_print_end_game_status(self):
    self.assertEqual(get_print(print_end_game_status,18,21),"-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status,18,20),"-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status,22,19),"-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status,22,21),"-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status,22,22),"-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status,18,22),"-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status,18,17),"-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status,21,17),"-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status,18,18),"-----------\nGAME RESULT\n-----------\nPush.\n")
    self.assertEqual(get_print(print_end_game_status,21,21),"-----------\nGAME RESULT\n-----------\nPush.\n")

    
    
    
 
  

if __name__ == '__main__':
    unittest.main()
