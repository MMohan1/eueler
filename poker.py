import sys
dict1 = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T': 10,'J':11,'Q':12,'K':13,'A':14}
def consucative(card ='7H 8H 9H TH JH'):
	list2 = []
	list_card = card.split(' ')
	for m in list_card:
		list2.append(m[0])
	if dict1[list2[0]] == dict1[list2[1]]-1 == dict1[list2[2]]-2 == dict1[list2[3]]-3 == dict1[list2[4]]-4:
		return 'True'

def card_same_value(card ='7H 7H 6S TH 7H'):
	list2 = []
	list_card = card.split(' ')
	for m in list_card:
		list2.append(m[0])
	for j in list2:
		if list2.count(j) == 4:
		elif list2.count(j) == 3:
			return 'Three'

def pair(card):
	list2 = []
	list_card = card.split(' ')
	for m in list_card:
		list2.append(m[0])
	for m in list2:
		if list2.count(m) == 2:
			return 'Two'

def pairs(card):
	list2 = []
	list3 = set()
	list_card = card.split(' ')
	for m in list_card:
		list2.append(m[0])
	for m in list2:8C TS KC 9H 
		if list2.count(m) == 2:
			list3.add(m)
	if len(list3) == 2:
		return 'Two pairs'

def if_value_same(card1,card2):
	a,b,x,y,c,d = 0,0,0,0,0,0
	list1 = []
	list2 = []
	list_card1 = card1.split(' ')
	list_card2 = card2.split(' ')
	for m in list_card1:
		list1.append(m[0])
	for m in list_card2:
		list2.append(m[0])
	for i in list1:
		if list1.count(i) == 3:
			c = dict1[i]
	for i in list2:
		if list2.count(i) == 3:
			d = dict1[i]
	for i in list1:
		if list1.count(i) == 2:
			x = dict1[i]
	for i in list2:
		if list2.count(i) == 2:
			y = dict1[i]
	if c > d:
		return card1
	elif c < d:
		return card2
	else:
		if x > y:
			return card1
		elif x < y:
			return card2
		elif x == y:
			for i in list1:
				if list1.count(i) == 1:
					if dict1[i] > a:
						a = dict1[i]
			for i in list2:
				if list2.count(i) == 1:
					if dict1[i] > b:
						b = dict1[i]
			if a > b:
				return card1
			else:
				return card2	
	

def conditions(card):	
	if card.count('H') == 5 or card.count('S') == 5 or card.count('D')==5 or card.count('C')==5:
		if card.count('T') == 1 and card.count('Q') == 1 and card.count('K')==1 and card.count('A')==1 and card.count('J')==1:
			return 'Royal Flush'
			
		elif consucative(card): 
			return 'Stright Flush'
		
		else:
			return 'Flush'
	
	elif consucative(card):
		return 'Straight'
	
	elif card_same_value(card) == 'Four':
		return 'Four of a Kind'
	
	elif pair(card) == 'Two' and card_same_value(card) == 'Three':
		return 'Full House'
	
	elif card_same_value(card) == 'Three':
		return 'Three of a Kind'
	
	elif pairs(card) == 'Two pairs':
		return 'Two Pairs'	
	
	elif pair(card) == 'Two':
		return 'One Pair'
	
	
	else:
		return 'Highest Card'

def poker():
	out_put = {'Royal Flush':10,'Stright Flush':9,'Four of a Kind':8,'Full House':7,'Flush':6,'Straight':5,'Three of a Kind':4,'Two Pairs':3,'One Pair':2,'Highest Card':1}
	player1_card = '5H 6C 7D 8C 9S'
	player2_card = '4C 5S 6H 7C 8D'
	player1 = conditions(player1_card)
	player2 = conditions(player2_card)
	if out_put[player1] > out_put[player2]:
		print 'player one is won'
	
	elif out_put[player1] < out_put[player2]:
		print 'player two is won'
	
	elif out_put[player1] ==out_put[player2]:
		if if_value_same(player1_card,player2_card) == player1_card:
			print 'player one is won'
		else:
			print 'player two is won'



if __name__ == '__main__':
	poker()
