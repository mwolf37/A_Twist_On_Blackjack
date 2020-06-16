from collections import Counter

"""A collection of function for doing my project."""
#Got help from this link for card_values 
#https://github.com/vanitaluja/punny_blackjack

#Probability and probability_facts is an orignial function
def card_values(hand):
    
    """
    Used to determine the total value of the hand.
    
    Parameters:
    ------------
    
        hand - list
            Hand is shown as a list of the cards the player has 
        
    Returns:
    ------------
        total - int
            total is shown as the sum of the values in hand
    """
    
        # Uses a dictionary in order to assign the values of the card in the hand 
    values_of_cards = {'Ace' : 1, 'King' : 10, 'Queen' : 10, 'Jack' : 10,
                           '10' : 10, '9' : 9, '8': 8, '7': 7, '6': 6, '5': 5,
                           '4': 4, '3': 3, '2': 2}
    total = 0
        
    #Adds up the values in the hand 
        
    for card in hand:
            
        value = values_of_cards[card]
        total += value
        
    return total

        
    
def probability(hand):
    
    """
    Used to find the probabilty of winning in the next round
    
    Parameters
    -----------
    hand: list 
        hand is shown as a list
    
    Returns
    ----------
    probability: int
        probability is shown as an integer
    """
    
    deck = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', 
            '7', '6', '5', '4', '3', '2'] * 4
    values_of_cards = {'Ace' : 1, 'King' : 10, 'Queen' : 10, 'Jack' : 10,
                           '10' : 10, '9' : 9, '8': 8, '7': 7, '6': 6, '5': 5,
                           '4': 4, '3': 3, '2': 2}
    
    #find cards left in deck
    total = Counter(deck)
    in_hand = Counter(hand)
    in_deck = list((total - in_hand).elements())
    
    #calculate range of cards that ca be a winning card
    total = card_values(hand)
    lower = 17 - total
    upper = 21 - total
    
    #calculate number of cards that could lead to a win
    winning = 0
    for card in in_deck:
        card_num = values_of_cards[card]
        
        if card_num >= lower and card_num <= upper: 
            winning = winning + 1
            
    probability = (winning / len(in_deck))
    return probability * 100

def probability_facts(hand):
    """Used to give probability facts regarding the cards drawn
    
    Parameters:
    -------------
    hand:list 
        hand is shown as a list 
        hand also has intergers for values of each card
    
    Returns
    ---------
    probablity_facts: str
        probability_facts are shown as strings
    """

    if 'Ace' == hand[0]:
        print("Your chances of getting an Ace as your first card is 1/13")
    elif 'King'== hand[1] or 'Jack' == hand[1] or 'Queen' == hand[1] or '10' == hand[1]:
        print("Your chances of gettting a value with 10 as your second card is 16/51")
    #if '9'or '8' or '7' or '6' or '5' or '4' or '3' or '2' in hand:
    else:
        print("Your chances of getting any value on the first card is 1/13")
    
    
        
    
