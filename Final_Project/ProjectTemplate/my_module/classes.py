"""Classes used throughout project"""
#imports random in order to shuffle and randomize the cards
import random
#Creates a deck of cards by using a list 

# Got help from this link for DeckOfCards
# https://codereview.stackexchange.com/questions/194812/a-simple-blackjack-game-implementation-in-python

#Player is an original function

# creates a class for players in order to keep track of the number of hits a player did and keeps track of what's in the player's hand 
class DeckOfCards():
    """Used to create a deck of cards 
    Parameters:
    -----------
    deck - list 
    
    Returns:
    -----------
    
    distributes and shuffles cards to player
    cards - list 
    """
    
    deck = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', 
            '7', '6', '5', '4', '3', '2'] * 4
    cards = []
    
    #shuffles the cards and helps pass out the cards to the player's hand 
    
    def shuffle(self, value = 52):
        cards = []
        
        for num in range(value):
            max_num = len(self.deck) - 1
            picked = random.randint(0, max_num)
            cards.append(self.deck[picked])
        
        # removes card that was chosen from the deck 
        self.deck.remove(self.deck[picked])

    
        return cards
class players():
    """Used to create a player
    Parameters:
    -------------
    hand - list 
    
    Returns:
    ----------
    name = string input
    """
    #Creates a player using the inputted name and keeps track of the player's hits and their hand
    hits = 0
    hand = []
    def __init__(self, name):    
        self.name = name
