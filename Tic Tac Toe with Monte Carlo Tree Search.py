# a3.py
import random
import copy


# helper function for cpuPlays function
# function which helps us to display the board on the console
def drawBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print("-+-+-")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("-+-+-")
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("")
    return


# helper function for cpuPlays function
def possiblePositions(board):
    # returns the index where the board is empty
    possible_moves = []
    for i in range(1, 10):
        if board[i] == ' ':
            possible_moves.append(i)
    return possible_moves


# helper function for cpuPlays function
def try_move(board, position, player):
    symbol = ''
    if player == 'Computer':
        symbol = '0'
    if player == 'Player':
        symbol = 'X'
    board[position] = symbol


# helper function for cpuPlays function
def checkWin_(board):
    if board[1] == board[2] == board[3] != ' ':  # across the top
        return True
    elif board[3] == board[5] == board[7] != ' ':  # diagonal
        return True
    elif board[1] == board[5] == board[9] != ' ':  # diagonal
        return True
    elif board[4] == board[5] == board[6] != ' ':  # across the middle
        return True
    elif board[7] == board[8] == board[9] != ' ':  # across the bottom
        return True
    elif board[1] == board[4] == board[7] != ' ':  # down the left side
        return True
    elif board[2] == board[5] == board[8] != ' ':  # down the middle
        return True
    elif board[3] == board[6] == board[9] != ' ':  # down the right side
        return True
    else:
        return False


# Gets best possible option by performing random play-outs
def cpuPlays(board):
    allowedMoves = possiblePositions(board)
    moves_score = {}
    for i in allowedMoves:
        moves_score.setdefault(i, 0)  # initial score set zero
        
    for move in allowedMoves:  # looping through every allowed possible move
        demo_board = copy.deepcopy(board)
        position_comp = move
        try_move(demo_board, position_comp, 'Computer')
        
        for i in range(5000):
            demo_board_ = copy.deepcopy(demo_board)
            while len(possiblePositions(demo_board_)) != 0:
                move_ = possiblePositions(demo_board_)
                
                position_player = random.choice(move_)

                try_move(demo_board_, position_player, 'Player')
                if checkWin_(demo_board_):
                    moves_score[move] -= 10
                    break
                    
                if len(possiblePositions(demo_board_)) == 0:
                    moves_score[move] += 5
                    break
                    
                position_comp = random.choice(allowedMoves)
                
                try_move(demo_board_, position_comp, "CPU")
                if checkWin_(demo_board_):
                    moves_score[move] += 1
                    break
                    
    return max(moves_score, key=moves_score.get)  # return the biggest score


# This functions checks winning conditions in the board
def checkWin(board, turn):
    if board[1] == board[2] == board[3] != ' ':  # across the top
        drawBoard(board)
        print("\nGame Over.\n")
        print("Congratulations! Team " + turn + " won.")
        return True
    elif board[3] == board[5] == board[7] != ' ':  # diagonal
        drawBoard(board)
        print("\nGame Over.\n")
        print("Congratulations! Team " + turn + " won.")
        return True
    elif board[1] == board[5] == board[9] != ' ':  # diagonal
        drawBoard(board)
        print("\nGame Over.\n")
        print("Congratulations! Team " + turn + " won.")
        return True
    elif board[4] == board[5] == board[6] != ' ':  # across the middle
        drawBoard(board)
        print("\nGame Over.\n")
        print("Congratulations! Team " + turn + " won.")
        return True
    elif board[7] == board[8] == board[9] != ' ':  # across the bottom
        drawBoard(board)
        print("\nGame Over.\n")
        print("Congratulations! Team " + turn + " won.")
        return True
    elif board[1] == board[4] == board[7] != ' ':  # down the left side
        drawBoard(board)
        print("\nGame Over.\n")
        print("Congratulations! Team " + turn + " won.")
        return True
    elif board[2] == board[5] == board[8] != ' ':  # down the middle
        drawBoard(board)
        print("\nGame Over.\n")
        print("Congratulations! Team " + turn + " won.")
        return True
    elif board[3] == board[6] == board[9] != ' ':  # down the right side
        drawBoard(board)
        print("\nGame Over.\n")
        print("Congratulations! Team " + turn + " won.")
        return True
    else:
        return False


def humanPlays(board, turn):
    print(" Its your turn player " + turn + ". Where do you want to place your " + turn + "?")
    str_move = input()
    move = int(str_move)
    while move == 0 or move > 9:
        print("Invalid")
        str_move = input()
        move = int(str_move)
    return move


def game():

    # Welcome Message
    print("\nHello! Welcome to Tic-Tac-Toe.\nGiven below are the position numbers for each cell.\nEnter the position "
          "number when asked to play.\nYou will be X and computer will be O.")
    print("You are only allowed to enter the numbers between one to nine and nothing else\n")
    print('1|2|3')
    print("-+-+-")
    print('4|5|6')
    print("-+-+-")
    print('7|8|9')

    print("\nLETS PLAY!\n")

    # initialize the board with empty spaces first
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}

    turn_no = 0
    play = True

    turn = 'X'

    while play is True:
        drawBoard(board)
        # move played by human
        move = humanPlays(board, turn)

        if board[move] == ' ':
            board[move] = turn
            turn_no += 1
        else:
            print("\nThat place is occupied.\nPlease give another input.\n")
            continue

        # Now we will check if the player won if the number of turns exceed 5.
        if turn_no >= 5:
            b = checkWin(board, turn)
            if b is True:
                play = False
                print("My algorithm sucks!")
                break

        # If in nine turns no one wins it will be a tie.
        if turn_no == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
            play = False
            return

        # Now we have to change the playing team after every turn.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        print(" After CPU's turn\n")

        # CPU's turn
        move = cpuPlays(board)
        board[move] = turn
        turn_no += 1

        # Now we will check if the CPU won if the number of turns exceed 5.
        if turn_no >= 5:
            b = checkWin(board, turn)
            if b is True:
                play = False
                break

        # If in nine turns no one wins it will be a tie.
        if turn_no == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
            play = False
            return

        # Now we have to change the playing team after every turn.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


if __name__ == "__main__":
    game()
