from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

 
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_stand_dealer_stand_user_wins(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards such that the hand value is less than 21.
        The user wins by having a greater hand value than the dealer.
        '''
        output = run_test([1,6,2], ['y', 'n'], [4,5,6,2], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 6\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 5\n" \
                   "Dealer has 9.\n" \
                   "Drew a 6\n" \
                   "Dealer has 15.\n" \
                   "Drew a 2\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output,expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_dealt_bj_dealer_stand_user_wins(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards such that the hand value is less than or equal to 21.
        The user wins by having hand value equal to 21(BLACKJACK!) and greater than the hand value of dealer.
        '''
        output = run_test([11,6,5], ['y', 'n'], [1,5,4], randint_mock, input_mock)
        expected =  "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew a Jack\n" \
                    "Drew a 6\n" \
                    "You have 16. Hit (y/n)? y\n" \
                    "Drew a 5\n" \
                    "Final hand: 21.\n" \
                    "BLACKJACK!\n" \
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew an Ace\n" \
                    "Drew a 5\n" \
                    "Dealer has 16.\n" \
                    "Drew a 4\n" \
                    "Final hand: 20.\n" \
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "You win!\n"
        self.assertEqual(output,expected)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_stand_dealer_bust_user_wins(self, input_mock, randint_mock):
        '''
        The dealer and user receive cards such that the hand value of user is less than 21 and that of the dealer is greater than 21(BUST).
        The user wins since the dealer is busted with a hand value greater than 21.
        '''
        output = run_test([10,6,4], ['y', 'n'], [1,1], randint_mock, input_mock)
        expected =  "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew a 10\n" \
                    "Drew a 6\n" \
                    "You have 16. Hit (y/n)? y\n" \
                    "Drew a 4\n" \
                    "You have 20. Hit (y/n)? n\n" \
                    "Final hand: 20.\n" \
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew an Ace\n" \
                    "Drew an Ace\n" \
                    "Final hand: 22.\n" \
                    "BUST.\n" \
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "You win!\n"
        self.assertEqual(expected,output)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_stand_dealer_stand_dealer_wins(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards such that the hand value is less than 21.
        The dealer wins by having hand value greater than that of the user.
        '''
        output = run_test([10,2,3], ['y', 'n'], [5,5,8], randint_mock, input_mock)
        expected =  "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew a 10\n" \
                    "Drew a 2\n" \
                    "You have 12. Hit (y/n)? y\n" \
                    "Drew a 3\n" \
                    "You have 15. Hit (y/n)? n\n" \
                    "Final hand: 15.\n" \
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew a 5\n" \
                    "Drew a 5\n" \
                    "Dealer has 10.\n" \
                    "Drew an 8\n" \
                    "Final hand: 18.\n" \
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "Dealer wins!\n"
        self.assertEqual(expected,output)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_hit_bust_dealer_hit_bust_dealer_wins(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards such that the hand value is greater than 21(BUST) but equal.
        User busts so dealer wins.
        '''
        output = run_test([1,9,2], ['y', 'n'], [1,5,6], randint_mock, input_mock)
        expected =  "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew an Ace\n" \
                    "Drew a 9\n" \
                    "You have 20. Hit (y/n)? y\n" \
                    "Drew a 2\n" \
                    "Final hand: 22.\n" \
                    "BUST.\n" \
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew an Ace\n" \
                    "Drew a 5\n" \
                    "Dealer has 16.\n" \
                    "Drew a 6\n" \
                    "Final hand: 22.\n" \
                    "BUST.\n" \
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "Dealer wins!\n"
        self.assertEqual(expected,output)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_bust_dealer_bust_dealer_wins(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards such that the hand value is greater than 21(BUST) but not equal.
        User busts so dealer wins.
        '''
        output = run_test([1,9,3], ['y', 'n'], [1,5,6], randint_mock, input_mock)
        expected =  "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew an Ace\n" \
                    "Drew a 9\n" \
                    "You have 20. Hit (y/n)? y\n" \
                    "Drew a 3\n" \
                    "Final hand: 23.\n" \
                    "BUST.\n" \
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew an Ace\n" \
                    "Drew a 5\n" \
                    "Dealer has 16.\n" \
                    "Drew a 6\n" \
                    "Final hand: 22.\n" \
                    "BUST.\n" \
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "Dealer wins!\n"
        self.assertEqual(expected,output)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_bust_dealer_bj_dealer_wins(self, input_mock, randint_mock):
        '''
        The dealer and user receive cards such that the hand value of user is greater than 21(BUST) and hand value of dealer is 21(BLACKJACK).
        The dealer wins by having a hand value equal to 21(BLACKJACK).
        '''
        output = run_test([10,10,5], ['y', 'n'], [10,1], randint_mock, input_mock)
        expected =  "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew a 10\n" \
                    "Drew a 10\n" \
                    "You have 20. Hit (y/n)? y\n" \
                    "Drew a 5\n" \
                    "Final hand: 25.\n" \
                    "BUST.\n" \
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew a 10\n" \
                    "Drew an Ace\n" \
                    "Final hand: 21.\n" \
                    "BLACKJACK!\n" \
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "Dealer wins!\n"
        self.assertEqual(expected,output)

    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_stand_dealer_bj_dealer_wins(self, input_mock, randint_mock):
        '''
        The dealer and user receive cards such that the hand value of user is greater than 21(BUST) and hand value of dealer is 21(BLACKJACK).
        The dealer wins by having a hand value equal to 21(BLACKJACK).
        '''
        output = run_test([10,5,3], ['y', 'n'], [10,1], randint_mock, input_mock)
        expected =  "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew a 10\n" \
                    "Drew a 5\n" \
                    "You have 15. Hit (y/n)? y\n" \
                    "Drew a 3\n" \
                    "You have 18. Hit (y/n)? n\n" \
                    "Final hand: 18.\n" \
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew a 10\n" \
                    "Drew an Ace\n" \
                    "Final hand: 21.\n" \
                    "BLACKJACK!\n" \
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "Dealer wins!\n"
        self.assertEqual(expected,output)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_stand_dealer_stand_push(self, input_mock, randint_mock):
        '''
        The dealer and user receive cards such that the hand value of user and dealer is less than 21.
        The result is a Push since both user and dealer have the same hand value.
        '''
        output = run_test([5,5,10], ['y', 'n'], [10,6,4], randint_mock, input_mock)
        expected =  "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew a 5\n" \
                    "Drew a 5\n" \
                    "You have 10. Hit (y/n)? y\n" \
                    "Drew a 10\n" \
                    "You have 20. Hit (y/n)? n\n" \
                    "Final hand: 20.\n" \
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew a 10\n" \
                    "Drew a 6\n" \
                    "Dealer has 16.\n" \
                    "Drew a 4\n" \
                    "Final hand: 20.\n" \
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "Push.\n"  
        self.assertEqual(expected,output)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_bj_dealer_bj_push(self, input_mock, randint_mock):
        '''
        The dealer and user receive cards such that the hand value of user and dealer is equal to 21(BLACKJACK).
        The result is a push since both user and dealer have the same hand value.
        '''
        output = run_test([1,10], ['y', 'n'], [10,1], randint_mock, input_mock)
        expected =  "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew an Ace\n" \
                    "Drew a 10\n" \
                    "Final hand: 21.\n" \
                    "BLACKJACK!\n" \
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew a 10\n" \
                    "Drew an Ace\n" \
                    "Final hand: 21.\n" \
                    "BLACKJACK!\n" \
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "Push.\n"  
        self.assertEqual(expected,output)


    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_stand_dealer_hit_user_wins(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards such that the hand value is less than or equal to 21.
        The user wins by having hand value greater than dealer
        '''
        output = run_test([1,9], ['n', 'n'], [1,6], randint_mock, input_mock)
        expected =  "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew an Ace\n" \
                    "Drew a 9\n" \
                    "You have 20. Hit (y/n)? n\n" \
                    "Final hand: 20.\n" \
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew an Ace\n" \
                    "Drew a 6\n" \
                    "Final hand: 17.\n" \
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "You win!\n"
        self.assertEqual(output,expected)




    

if __name__ == '__main__':
    main()
