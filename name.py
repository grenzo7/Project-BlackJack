choice=int(input())
if choice==1:
    print("Drew an Ace")
elif choice in range(2,11):
    if choice==8:
        print("Drew an "+str(choice))
    else:   
        print("Drew a "+ str(choice))
elif choice==11:
    print("Drew a Jack")
elif choice==12:
    print("Drew a Queen")
elif choice==13:
    print("Drew a King")
else:
    print("BAD CARD")
