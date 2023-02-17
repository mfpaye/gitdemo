import random


class Player:

    def number_of_players(self):
        while True:
            try:
                return int(input('Please enter 1 or 2 for the number of players:\n'))
            except:
                print("Error 0001: Invalid Entry!")


    def name_of_players(self, numberofplayers):
        player1_name = input('Player 1, please enter your name:\n')
        
        if numberofplayers == 2:
            player2_name = input('Player 2, please enter your name:\n')
        else:
            player2_name = 'Computer'

        return player1_name, player2_name


    def keep_playing(self, numberofplayers):
        play1 = input(f'{player_name}, Would you like to continue with playing?\nEnter Y or N\n').upper()
        if numberofplayers == 2:
            play2 = input(f'{player_name}, Would you like to continue with playing?\nEnter Y or N\n').upper()
        else:
            play2 = 'Y'
        
        return False if 'N' in [play1, play2] else True





# ---------------------------------------------------------
# ---------------------------------------------------------


class Deck:
    the_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*4


    def distribute_deck(self):
        random.shuffle(Deck.the_deck)

        playera_hand = []
        playerb_hand = []
        
        random.shuffle(Deck.the_deck)
        
        for position in range(len(Deck.the_deck)):
            if position % 2 == 0:
                playera_hand.append(Deck.the_deck[position])
            else:
                playerb_hand.append(Deck.the_deck[position])
        return playera_hand, playerb_hand


    # def print_the_card(self, player_card):
    #     deck_key = {
    #     2 : ' Two ',
    #     3 : 'Three',
    #     4 : 'Four ',
    #     5: 'Five ',
    #     5: ' Six ',
    #     7: 'Seven',
    #     8: 'Eight',
    #     9: 'Nine ',
    #     10: 'Jack ',
    #     11: 'Queen',
    #     12: 'King ',
    #     13: ' Ace '}

    #     print_player_card = f""" 
    #     -------
    #     |       |
    #     | {deck_key[player_card]} |
    #     |       |
    #     -------
    #     """

    #     return print_player_card


# ---------------------------------------------------------
# ---------------------------------------------------------


class Card:

    def remove_card(number_of_cards, playera_hand, playerb_hand, card_holder):
        playera_play = []
        playerb_play = []
        for item in range(number_of_cards):
            playera_play += playera_hand.pop(item)
            playerb_play += playerb_hand.pop(item)
        card_holder += [playera_play, playerb_play]

        return playera_play, playera_hand, playerb_play, playerb_hand, card_holder 


    def compare_cards(self, playera_name, playera_hand, playerb_name, playerb_hand, playera_play, playerb_play):
        # playera_play = playera_hand.pop(0)
        # playerb_play = playerb_hand.pop(0)

        ## Print the cards
        # def print_the_card(playera_top_card, playerb_top_card):
        def print_the_card(playera_play, playerb_play):
            deck_key = {
            2 : ' Two ',
            3 : 'Three',
            4 : 'Four ',
            5: 'Five ',
            5: ' Six ',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine ',
            10: 'Jack ',
            11: 'Queen',
            12: 'King ',
            13: ' Ace '}

            print_playera_card = f""" 
            -------
            |       |
            | {deck_key[playera_play]} |
            |       |
            -------
            """
            print_playerb_card = f""" 
            -------
            |       |
            | {deck_key[playerb_play]} |
            |       |
            -------
            """
            return f'{playera_name} played: {print_playera_card}\n {playerb_name} played: {print_playerb_card}'

        print(print_the_card(playera_play, playerb_play))

        ##Compare teh cards and declare the round's winner
        # if playera_top_card == playerb_top_card:
        #     return 'War!'
        # else:
        #     if playera_top_card > playerb_top_card:
        #         playera_hand += [playera_top_card, playerb_top_card]
        #         print(f'{playera_name} has won this round!')
            
        #     elif playerb_top_card > playera_top_card:
        #         playerb_hand += [playera_top_card, playerb_top_card]
        #         print(f'{playerb_name} has won this round!')
        
        # return (playera_hand, playerb_hand)


        if playera_play == playerb_play:
            return 'War!'
        else:
            if playera_play > playerb_play:
                playera_hand += [playera_play, playerb_play]
                print(f'{playera_name} has won this round!')
                winner = playera_name
            
            elif playerb_play > playera_play:
                playerb_hand += [playera_play, playerb_play]
                print(f'{playerb_name} has won this round!')
                winner = playerb_name
        
        return (playera_hand, playerb_hand, winner)


    
    def risk_cards(self, player_name):
       
        #ask player how many cards they want to risk
        while True:
            try:
                return int(input(f'{player_name}, please enter the number of cards you want to play:\n'))
            except:
                print(f'Error 000X: {player_name}, Invalid Entry!\nPlease enter a number.')
            



# ---------------------------------------------------------
# ---------------------------------------------------------

# GAME LOGIC

# ---------------------------------------------------------
# ---------------------------------------------------------

#Ask the number of players
players = Player()
number_of_players = players.number_of_players()

#Ask the name of the players
player1, player2 = players.name_of_players(number_of_players)

#Distribute the Deck
the_deck = Deck()
player1_hand, player2_hand = the_deck.distribute_deck()

round = 0
risk_card_holder = []
played_card_holder = []
war_on = False
#As long as neither player is empty handed and both want to play

if round % 2==0:
    player_name = player1
    player_hand = player1_hand
else:
    player_name = player2
    player_hand = player2_hand

#Ask the player to play or exit
game_on = players.keep_playing(number_of_players)


#Play normally. There is no war
card_playing = Card()
player1_play, player1_hand, player2_play, player2_hand, played_card_holder  = card_playing.remove_card(1, player1_hand, player2_hand, played_card_holder)
results = card_playing.compare_cards(player1, player1_hand, player2, player2_hand, player1_play, player2_play)


#If there is a war
while results == 'War!':
    player1_risk = card_playing.risk_cards(player1)
    player2_risk = card_playing.risk_cards(player2)
    numb_cards = min(player2_risk, player1_risk)

    #Add the risked card to the card holder till winner is declared
    player1_play, player1_hand, player2_play, player2_hand, risk_card_holder = card_playing.remove_card(numb_cards, player1_hand, player2_hand, risk_card_holder)
    results = card_playing.compare_cards(player1, player1_hand, player2, player2_hand, player1_play[-1], player2_play[-1])

else:
    player1_hand, player2_hand, winner = results

if winner == player1:
    player1_hand += risk_card_holder
    player1_hand += played_card_holder




# while game_on:
#     #Print the players top cards
#     the_deck.print_the_card()

    #Compare the cards

    #if there is a winner:
        #Declare the round's winner
    
    #else:
        #Declare War!

        #Ask the players if they want to the number of cards they want to risk

        #Pick the lowest of the two numbers

        #Print out the cards

        #Till there is a winner:
            #Remove those cards from the top deck of each player


            #Compare the next top cards


            # Id there is a winner, end the round and declare the winner


    #Check the size of both decks
        #if one hand is empty: end the game
        






