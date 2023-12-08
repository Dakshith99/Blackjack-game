############### Blackjack Project #####################

import random
import clear
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card 
 

def calculatescore(cards):
  if sum(cards)== 21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(userscore,computerscore):
  if userscore==computerscore:
    return"Draw"
  elif computerscore==0:
    return"computer wins with a blackjack"
  elif userscore==0:
    return"win with a blac  jack"
  elif userscore>21:
    return "opponent win"
  elif computerscore>21:
    return "you win"
  elif userscore>computerscore:
    return "you win"
  else:
    return "computer wins"
    
def play_game():

  print(logo)
  user_cards = []
  computer_cards = []
  gameover=False 
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while not gameover:
    userscore = calculatescore(user_cards)
    computerscore = calculatescore(computer_cards)
    print(f"your cards:{user_cards},computer cards:{computer_cards}")
    print(f"computers first cards :{computer_cards[0]}")
    
    if userscore==0 or computerscore==0 or userscore>21:
      gameover=True
    else:
      userresponse=input("type 'y' to get another card,type 'n' to pass:")
      if userresponse=='y':
        user_cards.append(deal_card())
      else:
        gameover=True
    
  while computerscore!=0 and computerscore <17:
    computer_cards.append(deal_card())
    computerscore=calculatescore(computer_cards)
  
  print(f" your final hand:{user_cards}, final score:{userscore}")
  print(f" computers final hand:{computer_cards}, final score:{computerscore}")
  print(compare(userscore,computerscore))
  
while input("Do you wanna play a game of blackjack? Type 'y' or 'n':") == 'y':
  clear.clear()
  play_game()
