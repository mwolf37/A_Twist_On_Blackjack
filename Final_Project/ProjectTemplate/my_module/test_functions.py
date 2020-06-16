"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""


    
from functions import *
from classes import *
##
##

#test the cards value is an integer ,test if ace can be used as either a 1 or an 11 depending on the situation
def test_card_values():
    assert isinstance(card_values(['7', '5']), int)
    assert card_values(['3', '5', '5']) == 13
    assert card_values(['Ace', '3', '4']) == 18
    assert card_values(['Ace', 'Jack', '3']) == 14
    
#test Deck_Of_Cards and wheher it shows as a list, check to see if strings can be in it, checks the length of how many cards someone can get 
def test_DeckOfCards():
    deck = DeckOfCards()
    list1 =  ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8',
            '7', '6', '5', '4', '3', '2']
    cards = deck.shuffle(2)
    assert DeckOfCards, 52
    assert isinstance(cards, list)
    assert any(item in cards for item in list1)
    assert len(cards) == 2
    print(cards)

#tests the player and making sure it is a string                       
def test_players():
    player = players('name')
    assert isinstance(player.name,str)


#test values_of_cards and whether the string matches with the value  
def test_values_of_cards():
    assert card_values(['Jack']) == 10
    assert card_values(['King']) == 10
    assert card_values(['7']) == 7
    
hand = ['King','2']
total = 14
    
#test probability(hand) to make sure it is an integer
def test_probability(hand):
    test_i = isinstance(probability(hand), int)

#test probability_facts(hand) to make sure it is a string and to make sure that if you get an ace you will not
#get the phrase that goes with the values of 10
def test_probability_facts(hand):
    test = isinstance(probability_facts(hand), str)
    assert probability_facts (['Ace']) != "Your chances of gettting a value with 10 as your second card is 16/51"

    

    
                      
                      
                      
                      


    



                 
    