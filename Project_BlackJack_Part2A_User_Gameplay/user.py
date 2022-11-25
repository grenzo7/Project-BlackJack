from random import randint


scores_dict={1:"Ace",2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:"Jack",12:"Queen",13:"King"}
user=randint(1,13)
if scores_dict[user]=="Ace" or scores_dict[user]==8:
  print("Drew an",scores_dict[user])
else:
  print("Drew a",scores_dict[user])
if user==11 or user==12 or user==13:
  user=10
elif user==1:
  user=11
sum=user
user=randint(1,13)
if scores_dict[user]=="Ace" or scores_dict[user]==8:
  print("Drew an",scores_dict[user])
else:
  print("Drew a",scores_dict[user])
if user==11 or user==12 or user==13:
  user=10
elif user==1:
  user=11
sum+=user


while sum<21:
  ans=input(f"You have {sum}. Hit (y/n)? ")
  if ans=="y":
      user=randint(1,13)
      if scores_dict[user]=="Ace" or scores_dict[user]==8:
          print("Drew an",scores_dict[user])
      else:
          print("Drew a",scores_dict[user])
        
      if user==11 or user==12 or user==13:
          user=10
      elif user==1:
          user=11
      sum+=user
  elif ans=="n":
    break
  else:
    print("Sorry I didn't get that.")


print("Final hand:", str(sum)+".")
if sum==21:
  print("BLACKJACK!")
elif sum>21:
  print("BUST.")
