from random import randint


scores_dict={1:"Ace",2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:"Jack",12:"Queen",13:"King"}
dealer=randint(1,13)
if scores_dict[dealer]=="Ace" or scores_dict[dealer]==8:
  print("Drew an",scores_dict[dealer])
else:
  print("Drew a",scores_dict[dealer])
if dealer==11 or dealer==12 or dealer==13:
  dealer=10
elif dealer==1:
  dealer=11
sum=dealer
dealer=randint(1,13)
if scores_dict[dealer]=="Ace" or scores_dict[dealer]==8:
  print("Drew an",scores_dict[dealer])
else:
  print("Drew a",scores_dict[dealer])
if dealer==11 or dealer==12 or dealer==13:
  dealer=10
elif dealer==1:
  dealer=11
sum+=dealer


while sum<17:
  print("Dealer has",str(sum) + ".")
  dealer=randint(1,13)
  if scores_dict[dealer]=="Ace" or scores_dict[dealer]==8:
    print("Drew an",scores_dict[dealer])
  else:
    print("Drew a",scores_dict[dealer])
  if dealer==11 or dealer==12 or dealer==13:
    dealer=10
  elif dealer==1:
    dealer=11
  sum+=dealer
  if sum>=17:
    break


print("Final hand:", str(sum)+".")
if sum==21:
  print("BLACKJACK!")
elif sum>21:
  print("BUST.")
