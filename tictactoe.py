
def tic_tac_toe():
    # ask the player the number of players 1 or 2
    #Make sure you validate their entry
    def number_of_players():
        while True:
            numb_player = input('Enter 1 or 2 for the number of players:\n')
            if numb_player in ['1', '2']:
                return numb_player
            else:
                print(f'Error: 001 - "{numb_player}" is an invalid entry.\nPlease enter 1 or 2 to play')

    #ask player 1 their symbol then assign the remaining symbol to player 2
    def player_symbols(player_name):
        choices = ["@","X"]
        while True:
            player1_symb = input(f'{player_name}, please enter "{choices[0]}" or "{choices[-1]}" for your symbol:\n').upper()
            
            if player1_symb not in choices:
                print(f'Error: 002 - {player1_symb} is an invalid entry.\nPlease enter "{choices[0]}" or "{choices[-1]}" to play.\n')
            else:
                choices.remove(player1_symb)
                player2_symb = choices[0]
                return player1_symb, player2_symb

    #Ask player to pick a play by entering a number between 1-9
    def pick_a_play(current_board, player):
        while True:
            current_play = input(f'{player}, please enter a number between 1 through 9 to play:\nTo exit the game, enter "EXIT".\n')
            try:
                if current_play.upper() == 'EXIT':
                    return current_play
                else:
                    if int(current_play) in current_board:
                        return current_play
                    else:
                        print(f'Error: 003 - Your entry,"{current_play}", is unavailable.\n')
            except:
                print(f'Error: 004 - Your entry,"{current_play}", is an invalid position.\n')

    #remove player's position from the board and replace it with the player's symbol
    def update_stats(current_board, players_symbol, picked_position, playable_positions):
        #Update the table
        playable_positions.remove(int(picked_position))

        #Update the player's own table plays so far
        for numb in range(8):
            current_board[numb] = current_board[numb].replace(picked_position, players_symbol)
        return current_board, playable_positions

    # a function to help print each line of the board
    def line_print(a_list):
        for an_item in a_list:
            print(an_item, end="|")
        return('\n-----')

    def blocking_finding_wins(the_updated_board, player1_symbol, player2_symbol):
    #take the updated board and check each answer

        #First sort each answer. The result will be a list 
        # that needs to be combined into a string
        def check_player(symbol):
            #First sort each answer.
            for each_answer in the_updated_board:
                each_answer = sorted(each_answer)
                #The result will be a list. Check to see if computer's play has 
                # 2 symbols there. If so, be combined the list into a string
                if each_answer.count(symbol) == 2:
                    each_answer = ''.join(each_letter for each_letter in each_answer)
                    #the new string will put the number on first position
                    #if this first position is number and not the other player's symbol, 
                    #make this the new computer's play
                    if each_answer[0].isdigit():
                        play_this_position = each_answer[0]
                        return play_this_position
            else:
                return False
        
        #check if computer has a win first
        player2_wins = check_player(player2_symbol) 
        if player2_wins != False:
            current_play = player2_wins
        #if computers has no winning position to play,
        #check if there is a position that should be blocked
        else:
            player1_wins = check_player(player1_symbol)
            if player1_wins != False:
                current_play = player1_wins
            #if there is no position to be block
            else:
                current_play = False
            
        return current_play
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
    #### START THE GAME
#-------------------------------------------------------------------------------------

    #The board content at the start of the game
    available_positions = list(range(1,10))
    current_table = ['147','258','369','123', '456', '789', '159', '357']

    ## Get the number of players and their names
    numb_players = number_of_players()
    player1 = input('Please enter your name:\n')
    if numb_players == '1':
        player2 = 'Computer'
    else:
        player2 = input('Please enter your name:\n')

    #Ask Player 1 to choose a symbol
    player1_symbol, player2_symbol = player_symbols(player1)

    #Start with no winner
    no_winner = True

    #in case there is only one player, import the random module to choose
    #the computer's play
    import random

    #print the current board
    the_lines = map(line_print, current_table[3:6])
    for each_line in the_lines:
        print(each_line)
    print('\n')

    #Play the game as long as there are no winners.
    while no_winner:
       
        #keep going if there are still open positions
        if available_positions != []:
            #Ask current player to play depending on the number of players
            if len(available_positions) % 2 == 0:
                current_symbol = player2_symbol
                if numb_players == '1':
                    find_wins_blocks = blocking_finding_wins(current_table, player1_symbol, player2_symbol)
                    if find_wins_blocks != False:
                        current_play = find_wins_blocks
                    else:
                        current_play = str(random.choice(available_positions))
                else:
                    current_play = pick_a_play(available_positions, player2)
            else:
                current_symbol = player1_symbol
                current_play = pick_a_play(available_positions, player1)
            
           
            ### If current_play is "Exit", end the game
            if current_play.upper() == "EXIT":
                print("\nYou have chosen to end the game.\nThank you for playing.\nCome back again soon.\n")            
            else:

                #Update the stats based on who is playing
                current_table, available_positions= update_stats(current_table,current_symbol,current_play,available_positions)

                #Check if there is a winner
                if player1_symbol*3 in current_table:
                    print(f'{player1} has won the Game!\nCongratulations to {player1}.')
                    no_winner = False
                
                elif player2_symbol*3 in current_table:
                    print(f'{player2} has won the Game!\nCongratulations to {player2}.')
                    no_winner = False
            
        #if there are no more open positions, then game is over and it is a tie.
        else:
            print('It is a tie!! Game over!')
            no_winner = False
        
        #print the current board
        the_lines = map(line_print, current_table[3:6])
        for each_line in the_lines:
            print(each_line)
        print('\n')

        #if the game ends, ask them to play again or end the game
        # if no_winner == False:
        while no_winner == False:
            playe_again = input('Would like to play again? Enter "Y" or "N":\n').upper()
            if playe_again == 'Y':
                #Reset the board content to the start of the game
                available_positions = list(range(1,10))
                current_table = ['147','258','369','123', '456', '789', '159', '357']
                no_winner = True
                break
            elif playe_again == 'N':
                print('Thank you for playing.\nCome back again!')
                break
            else:
                print('Error 005: Invalid Enter. Please enter "Y" or "N"')

        # print(f'LINE 197: TEST TEST TEST TEST; no_winner: {no_winner}')
        ##if they wanted to exit
        if current_play == 'EXIT':
            while True:
                playe_again = input('Are you sure you want to exit?\nEnter "EXIT" to end game or "Continue" to keep playing:\n').upper()
                if playe_again == 'EXIT':
                    no_winner = False
                    break
                elif playe_again == 'CONTINUE':
                    no_winner = True
                    break
                else:
                    print('Error 006: Invalid Enter. Please enter "EXIT" or "CONTINUE"')
    

tic_tac_toe()



