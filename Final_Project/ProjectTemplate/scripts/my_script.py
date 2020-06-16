"Script for Game"
import sys
sys.path.append('../')

# import classes and funtions needed for game 
#from my_module.functions import card_values, probability
#from my_module.classes import DeckOfCards, players

import random
from collections import Counter
#from functions import card_values, probability
from functions import *
#from classes import DeckOfCards, player
from classes import *


initial_start = input('Welcome to a Twist on Blackjack. Do you wanna play?: ')
if initial_start.upper() == 'YES':
    print("Let's Play!")
    player_name = input('Enter your name: ')
    # makes it so player can continue playing over again
    play_again = True
    while play_again == True:
        total_hand = DeckOfCards()
        player = players(player_name)

        #shuffles and distributes cards and adds total for player's cards


        player.hand = total_hand.shuffle(2)
        print('player:' + str(player.hand))

        total = card_values(player.hand)
        print(player.name + "'s total is " + str(total))
        
        #Gives probabilty facts based on what you get 
        probability_facts(player.hand)

        #sees if the total is between 17 and 21 on the first hit

        repeat = True 
        total = card_values(player.hand)

        if total >= 17 and total <= 21:

            print('Yay~! You won! \n You won in {} hits. Try for more hits next time.'.format(player.hits))
            repeat = False

        # Creates an empty hits sequence in order to keep track of the number of hits the player does 
        hits = 0
        
        #if the player does not have card values in between 17 and 21, it creates a loop and goes on to ask if they want another card
        while repeat:


            again = input ('Player would you like to hit or stand? \n' + 
                   'Current total = ' + str(total) + ' ')
            if again.lower() == 'hit':
                    hits = hits + 1
                    new_card = total_hand.shuffle(1)
                    player.hand.append(new_card[0])
                    total = card_values(player.hand)
                    print(new_card)
                    print(player.name + "'s new total is " + str(total))
                    

            else:
                    total = card_values(player.hand)
                    print('Current hand: ' + str(player.hand) + '\n' +
                          'Total :' + str(total))
                    if total < 17:
                        repeat = False
                        print('Womp womp :(')

            #Makes it so that if the total greater then 21,                    
            if total > 21:
                print('You bust! Sorry')
                repeat = False

            elif total >= 17 and total <= 21:
                print('Yay! You win! It took you ' + str(hits) + ' hits to get there')
                repeat = False
            
            #Shows the probability of winning in the next hand when total is under 17 after you have already hit
            elif total < 17:
                print('Your probability of winning in the next hand ' + str(probability(player.hand)) + '%.')
                continue

        # Makes it so the user can play agin as it restarts the loop or if not it ends the loop
        final_answer = input('Type "again" if you would like to play again:')
        if final_answer.lower() == 'again':
            play_again = True 
            
        else:
            play_again = False 
            print("Let's play again next time")
else:
    print('Aww. Too bad.')
            
            
