import random

cardarray = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
suits = ['hearts', 'spades', 'clubs', 'diamonds']

class Deck(object):
	def __init__(self):
		self.deckcards = []
		for s in suits:
			for i in cardarray:
				self.deckcards.append(str(i) + ' of ' + str(s))
		self.decklength = len(self.deckcards)
		# print self.decklength
	def draw(self):
		yourdraw = self.deckcards.pop()
		self.decklength -= 1
		# print self.decklength
		return yourdraw
	def addcard(self, card_to_add):
		#self.deckcards.append(card_to_add)
		for i in range(len(self.deckcards)-1, -1, -1):
			self.deckcards[i] = self.deckcards[i-1]
		self.deckcards[0] = card_to_add
		self.decklength += 1
		# print self.decklength
		return self
	def shuffle(self):
		for i in range(self.decklength-1):
			idx = random.randint(1, self.decklength-1)
			temp = self.deckcards[i]
			self.deckcards[i] = self.deckcards[idx]
			self.deckcards[idx] = temp
		# for x in self.deckcards:
		# 	print x
		return self
	def printdeck(self):
		print self.decklength
		# print self.deckcards[0]
		# print self.deckcards[len(self.deckcards)-1]

class Player(object):
	def __init__(self, name):
		self.hand = []
		self.name = name
	def receive(self, deck_to_draw_from):
		temp = deck_to_draw_from.draw()
		self.hand.append(temp)
		#print len(self.hand)
		return self
	# def giveR(self, deckRef):
	# 	idx = random.randint(1, len(self.hand))
	# 	temp = self.hand[idx]
	# 	deckRef.addcard(temp)
	# 	return self
	def giveI(self, deckRef, idx):
		if idx > len(self.hand)-1:
			idx = len(self.hand)-1

		swap = self.hand[idx]
		self.hand[idx] = self.hand[len(self.hand)-1]
		self.hand[len(self.hand)-1] = swap
		self.hand.pop()
		deckRef.addcard(swap)
		#print len(self.hand)
		return self
	def showhand(self, deck_to_draw_from):
		#deck_to_draw_from.printdeck()
		print self.hand
		return self


aDeck = Deck().shuffle()
aPlayer = Player('Vitali').receive(aDeck).receive(aDeck).receive(aDeck).receive(aDeck).receive(aDeck).receive(aDeck)
aPlayer.showhand(aDeck).giveI(aDeck, 7).showhand(aDeck)
aPlayer.receive(aDeck).showhand(aDeck)
aDeck.printdeck()

