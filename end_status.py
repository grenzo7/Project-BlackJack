hand_value=int(input())
if hand_value==21:
    print("BLACKJACK!")
if hand_value>21:
    print("BUST.")
if hand_value<4 or hand_value>31:
    print("BAD HAND VALUE!")
    
