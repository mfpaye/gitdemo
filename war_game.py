def war_game ():
    import random
    class Player:

        #ask number of players
        def number_of_players(self):
            while True:
                try:
                    numb_player = 1
                    while True:
                        numb_player = int(input('Please enter the number of players:\n'))
                        if 52 % numb_player != 0 or numb_player >= 52:
                            print('ERROR 01: The number of players must evenly divisible by and be less than the number cards on the deck (52)!')
                        else:
                            return numb_player
                except:
                    print('ERROR 02: Invalid entry! Numbers only!')


        #ask for their names
        def players_names(self, number_of_players):
            player1 = input('Player 1, please enter your name:\n')
            player_names =[player1]

            if number_of_players > 1:
                for each_player in range(1,numb_players):
                    player_names += [input(f'Player {each_player+1}, please enter your name:\n')]
            else:
                player_names += ['Computer']
                number_of_players += 1

            return player_names, number_of_players
    
    
    class Deck:
        
        #Create then distribute the deck
        def distribute_deck(self, player_names):
            #Make the deck
            suits = [' Hearts ', ' Spades ', 'Diamonds', ' Clubs  ']
            ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

            #make the decks with hearts
            the_deck = []
            for suit in suits:
                for digit in ranks:
                    if digit <10:
                        the_deck.append(('0'+str(digit))[-2:]+suit)
                    else:
                        the_deck.append((str(digit))[-2:]+suit)
            
            random.shuffle(the_deck)
            
            #Create the empty list for each player
            players_hands = dict()
            for each_players in player_names:
                    players_hands[each_players] = []
            
            #add the cards to each players empty list
            while len(the_deck)>0:
                for each_players in player_names:
                    players_hands[each_players] += [the_deck.pop(0)]

            return players_hands
    
    
    class Card:

        ##Ask each player to put out a card
        def play_your_card(self, all_players_card ):

            played_cards = dict()

            for each_player in all_players_card :
                the_players_card = all_players_card[each_player].pop(0)
                played_cards[each_player] = the_players_card
            
            return played_cards, all_players_card


        #Get the players with the highest cards
        def winning_players (self, cards_played):
            
            #Collect the numbers and convert them from string to intergers
            cards_played_digits = dict()
            for key,value in cards_played.items():
                digit = int(value[:2])
                cards_played_digits[key] = digit

            #determine the winners
            winners = dict()
            for key,value in cards_played_digits.items():
                if value == max(cards_played_digits.values()):
                    winners[key] = value
            return winners


        #if war is on, ask the player to choose the number of cards to risk
        def choose_your_risk(self, the_winners, each_players_hand):
            bets = []
            for each_player in the_winners:
                if each_player == 'Computer':
                    bets += [random.choice(range(len(each_players_hand[each_player])))]
                else:
                    while True:
                        #make sure they only enter numbers
                        try:
                            bid = int(input(f'{each_player}, please enter the number of cards you would like to risk:\n'))
                        except:
                            print(f'ERROR 03: {each_player}, please enter numbers only!')
                            continue
                        
                        #Compile all of the bets
                        if bid < len(each_players_hand[each_player]):
                            bets.append(bid)
                            break
                        else:
                            print(f'ERROR 04: {each_player}, you have {len(each_players_hand[each_player])} cards.\nPlease enter a number that is less than the smallest deck.\n')
                
                #Compile the length of each hand
                sum_length_hands = []
                for values in each_players_hand.values():
                    sum_length_hands += [len(values)-1]

                #Add the lengths to the bets
                bets += sum_length_hands

            return min(bets)


        #Collect the cards that are being risked
        def remove_risked_cards(self, each_players_hand, the_bid, risked_card_holder):
            print(f'LINE 104: Bets are: {the_bid}')
            for numb in range(the_bid):
                for hand in each_players_hand.values():
                    if len(hand) == 0:
                        pass
                    else:
                        risked_card_holder += [hand.pop(0)]
            
            return risked_card_holder, each_players_hand
        

        #Print a visual representation of the cards
        def print_the_cards(self, cards):

            # #make the card
            def print_the_card(player_card):
                
                the_card =int(player_card[:2])
                the_suit = player_card[2:]


                deck_key = {
                2 : ' Two ',
                3 : 'Three',
                4 : 'Four ',
                5: 'Five ',
                6: ' Six ',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine ',
                10: ' Ten ',
                11: 'Jack ',
                12: 'Queen',
                13: 'King ',
                14: ' Ace '}



                print_player_card = f""" 
                -------------------
                |                  |
                | {deck_key[the_card]}            |
                |        of        |
                | {the_suit}         |
                |                  |
                -------------------
                """
                return (print_player_card)

            #For each player, print the card
            for player,card in cards.items():
                print(f'{player} played: {print_the_card(card)}')    
            print('\n')
    

        #Print the number of cards per hands
        def cards_per_hands(self, all_hands):
            for player, hand in all_hands.items():
                print(f'{player} has {len(hand)} cards.')
            print('\n')


    class Game:

        def game_on(self, each_players_hand):
            answers = []
    
            for each_player in each_players_hand:
                if each_player == 'Computer':
                    answers += ['Y']
                else:
                    while True:
                        answer = input(f'{each_player}, would you like to keep playing? Enter Y or N:\n').upper()
                        if answer in ['Y', 'N']:
                            answers += answer
                            break
                        else:
                            print(f'ERROR 05: {each_player}, you have entered an invalid answer.\n')
                
            return 'N' not in answers

        def print_announcements(self, annoucement):
            print('\n')
        print('*!'*30)
            print('\n')
            print(annoucement)
            print('\n')
            print('*!'*30)
            print('\n')

    the_players = Player()
    #ask number of players
    numb_players = the_players.number_of_players()
    #ask their names
    name_of_players, numb_players = the_players.players_names(numb_players)
    print('\n')
    print('*'*50)

    #Create then distribute the deck
    the_deck = Deck()
    each_players_hand = the_deck.distribute_deck(name_of_players)

    game_is_on = True
    
    while game_is_on:
        
        #Ask each player to put out a card
        the_cards = Card()

        cards_played, each_players_hand = the_cards.play_your_card(each_players_hand)

        print('\n')
        #print the cards played
        the_cards.print_the_cards(cards_played)
        
        #Get the players with the highest cards - AKA, the winners
        any_winners = the_cards.winning_players(cards_played)

        #store the played card in the risked_cards pile
        risked_card_holder = []
        for card in cards_played.values():
            risked_card_holder += [card]

        #Determine if there is one winner or war
        the_game = Game()
        while True:
            if len(any_winners) == 1:
                for the_winner in any_winners:
                    
                    #Add the played cards to the winner's hand
                    each_players_hand[the_winner] += risked_card_holder
                    
                    #Announce the round's winner
                    print(f'\n***** {the_winner} has won this round! *****\n')
                    print("*"*30)
                
                    #print the size of each player's hands
                    the_cards.cards_per_hands(each_players_hand)
                
                ##remove players with empty hands, split in two steps 
                # because you cannot iterate in changing dictionnary length
                empty_handers =[]
                #get the a list of the players with empty hands
                for each_player, hand in each_players_hand.items():
                    if len(hand) == 0:
                        empty_handers += [each_player]
                #remove the players with empty hands
                for the_empty_handers in empty_handers:
                    each_players_hand.pop(the_empty_handers)

                restarting = False
                #check if only one player has cards, then there is a game winner
                if len(each_players_hand) == 1:
                    for the_winner in each_players_hand:
                        the_game.print_announcements(f'{the_winner} has won the Game!!\nCongratulations to the {the_winner}!')

                    #Re-create then re-distritube the deck
                    each_players_hand = the_deck.distribute_deck(name_of_players)
                    
                    restarting = True
                break
                
            else:
                while len(any_winners)>1:
                    #Announce the tie
                    print('\n!!!!!!It is a tie! It is a WAR!!!!!!\n')
                    
                    #print the number of cards for players
                    the_cards.cards_per_hands(each_players_hand)

                    #make sure that if the player only has 1 card left, to move on to playing without betting
                    for each_player in any_winners:
                        hand = each_players_hand[each_player]
                        if len(hand) <= 1:
                            break
                    else:
                        #if war is on, ask the player to choose the number of cards to risk
                        the_bets = the_cards.choose_your_risk(any_winners, each_players_hand)
                        
                        #Collect the cards that are being risked
                        risked_card_holder, each_players_hand = the_cards.remove_risked_cards(each_players_hand, the_bets, risked_card_holder)

                    #Ask the winners to now play
                    cards_played, each_players_hand = the_cards.play_your_card(each_players_hand)
                    
                    #print the cards played
                    the_cards.print_the_cards(cards_played)
                    
                    #check for winners again
                    any_winners = the_cards.winning_players(cards_played)
                    for card in cards_played.values():
                        risked_card_holder += [card]
            
        #Ask the players if they want to keep playing
        
        game_is_on = the_game.game_on(each_players_hand)
        if game_is_on:
            if restarting:
                the_game.print_announcements('\nThe game has been reset and is restarting!\n')

                restarting = False

        else:
            the_game.print_announcements(f'You have choosen to end the game. Thank you for playing! Come back again!\n')

            


        


            
war_game()



