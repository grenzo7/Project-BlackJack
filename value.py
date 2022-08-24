choice=int(input())
hand_value=0
if choice in range(2,11):
    hand_value=choice
    print("Your hand value is "+ str(hand_value) + ".")
elif choice==11 or choice==12 or choice==13:
    hand_value=10
    print("Your hand value is "+ str(hand_value) + ".")
elif choice==1:
    hand_value=11
    print("Your hand value is "+ str(hand_value) + ".")
else:
    print("BAD CARD")
