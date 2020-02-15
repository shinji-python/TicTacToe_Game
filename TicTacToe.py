from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(board[1]+'|'+board[2]+'|'+ board[3])
    print(board[4]+'|'+board[5]+'|'+ board[6])
    print(board[7]+'|'+board[8]+'|'+ board[9])


def player_input():
    marker = ''

    # Leave marker open while player selects marker

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, pick X or O:')

        # Assign marker

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return mark == board[1] == board[2] == board[3] or mark == board[1] == board[4] == board[7] or mark == board[7] == \
           board[8] == board[9] or mark == board[9] == board[6] == board[3] or mark == board[1] == board[5] == board[
               9] or mark == board[3] == board[5] == board[7]


def choose_first():
    random_num=random.randint(1,2)
    if random_num ==1:
        return 'Player 1 goes'
    else:
        return 'Player 2 goes'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    return ' ' not in board


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('What position does player choose (1-9)?:'))

    return position

def replay():
    play_again=''
    while play_again != 'Yes' and play_again != 'No':
        play_again=input('Do you want to play again?:')
    return play_again == 'Yes'


print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here

    # clear positions in the board
    board = [' '] * 10

    # Assign markers for each player
    player1_marker, player2_marker = player_input()

    # Decide which player goes first
    turn = choose_first()
    print(turn)

    # Ask to start the game
    play_game = input('Do you want to play the game? Yes or No:')
    if play_game == 'Yes':
        game_on = True
    else:
        game_on = False

    while game_on:
        # Player 1 Turn
        if turn == 'Player 1 goes':
            display_board(board)

            # Player picks a position
            position = player_choice(board)

            # Marker is placed
            place_marker(board, player1_marker, position)

            # Check if player has won
            if win_check(board, player1_marker):
                display_board(board)
                print('Player 1 has won!')
                game_on = False

            # Check if there was a tie
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Board is full and game is tied!')
                    game_on = False
                    break
                # Go to next player if no win or tie
                else:
                    turn = 'Player 2 goes'

        # Player2's turn.
        else:
            display_board(board)

            # Player picks a position
            position = player_choice(board)

            # Marker is placed
            place_marker(board, player2_marker, position)

            # Check if player has won
            if win_check(board, player2_marker):
                display_board(board)
                print('Player 2 has won!')
                game_on = False

            # Check if there was a tie
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Board is full and game is tied!')
                    game_on = False
                    break
                # Go to next player if no win or tie
                else:
                    turn = 'Player 1 goes'

    if not replay():
        break