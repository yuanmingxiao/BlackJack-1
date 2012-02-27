#!/usr/bin/python
# BlackJack v1.0 By Andrew Knapp
# This is a port (with some changes) of the Java version of BlackJack I wrote
import random

#Global Variables
money = 100
deck = ['AC','2C','3C','4C', '5C','6C', '7C', '8C', '9C', '0C', 'JC','QC','KC','AD','2D','3D','4D','5D','6D',
	'7D','8D','9D','0D','JD','QD','KD','AS','2S','3S','4S','5S','6S','7S','8S','9S','0S','JS','QS','KS','AH','2H',
	'3H','4H','5H','6H','7H','8H','9H','0H','JH','QH','KH']

#Functions
def intro():
    print "Welcome to Black Jack!"
    print "You have: $" + str(money)

def choice(ans):
    if ans[0].lower() == 'y':
	return True
    else:
	return False

def checkMoney():
    if (money == 0):
	print "You're out of money. House wins."
	return False

def getCardValue(card, total):
    if card[0].isdigit() and int(card[0]) != 0:
	return int(card[0])
    elif card[0] == "A" and total + 11 <= 21:
	return 11
    elif card[0] == "A" and total + 11 > 21:
	return 1
    else:
	return 10

def cardType(card):
    if card[0].isalpha():
	faceCards = ["Ace", "Jack", "Queen", "King"]
	for cardType in faceCards:
	    if cardType[0] == card[0]:
		return cardType
    elif card[0] == '0':
	 return "10"
    else:
	return str(card[0])

def suitType(card):
    suits = ["Spades","Hearts","Clubs","Diamonds"]
    for types in suits:
	if card[1] == types[0]:
	    return types

def findWinner(player_total, dealer_total, bet, money):
    if player_total <= 21 and dealer_total <= 21:
	 print "You have " + str(player_total) + " dealer has " + str(dealer_total)
	 if player_total == dealer_total:
	   print "Push"
	 elif player_total > dealer_total:
	   print "You won!"
	   money = money + bet
	 else:
	   print "House wins."
	   money = money - bet
    elif dealer_total > 21:
	print "Dealer Busts.  You win!"
	money = money + bet
    else: 
	print "House wins."
	money = money - bet
    return money

def playGame(bet, money):
    player_total = 0
    dealer_total = 0
    cards = []
    random.shuffle(deck)
    player_card1 = deck.pop()
    cards.append(player_card1)
    print "1st card: " + cardType(player_card1) + " of " + suitType(player_card1)
    player_total += getCardValue(player_card1, player_total)
    player_card2 = deck.pop()
    cards.append(player_card2)
    print "2nd card: " + cardType(player_card2) + " of " + suitType(player_card2)
    player_total += getCardValue(player_card2, player_total)
    dealer_card1 = deck.pop()
    dealer_total += getCardValue(dealer_card1, dealer_total)
    cards.append(dealer_card1)
    print "Dealer gets: " + cardType(dealer_card1) + " of " + suitType(dealer_card1)
    print "Dealer showing: " + str(dealer_total)
    print "You have: " + str(player_total)
    ans = raw_input('Do you want to hit? ')
    while choice(ans) and player_total < 21:
	player_card = deck.pop()
	cards.append(player_card)
	print cardType(player_card) + " of " + suitType(player_card)
	player_total += getCardValue(player_card, player_total)
	if player_total == 21:
	    print "You got 21!"
	elif player_total > 21:
	    print "You have: " + str(player_total)
	    print "You Busted."
	else:
	    print "You have: " + str(player_total)
	    ans = raw_input('Do you want to hit? ')
    while dealer_total <= 17 and player_total < 21:
	dealer_card = deck.pop()
	cards.append(dealer_card)
	print "Dealer gets: " + cardType(dealer_card) + " of " + suitType(dealer_card)
	dealer_total += getCardValue(dealer_card, dealer_total)
	print "Dealer has " + str(dealer_total)
    money = findWinner(player_total, dealer_total, bet, money)
    for item in cards:
	deck.append(item)
    return money

def winLoss():
    if money > 100:
	print "You won $" + str(money - 100)
    else:
	print "You lost $" + str(100 - money)
	    
#Function Call Area
intro()
ans = 'y'
while choice(ans):
    amount = raw_input("How much do you want to bet? ")
    while amount.isalpha():
	print "That is not a number"
	amount = raw_input("How much do you want to bet? ")
    bet = int(amount)
    money = playGame(bet, money)
    print "You have $" + str(money)
    if money <= 0:
       print "You are out of money."
       break;
    else:
      ans = raw_input('Do you want to play again? ')
winLoss() 
