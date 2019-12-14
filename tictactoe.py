# Function To Display the Board

def display_board(board):
# Check to see if it's a test board and only print out one board
    if len(board)==10:
        print('\n'*2)
        print(' '*6,'    |   |   ')
        print(' '*6,' ',board[6], '|',board[7],'|',board[8])
        print(' '*6,'____|___|___')
        print(' '*6,'    |   |   ')
        print(' '*6,' ',board[3], '|',board[4],'|',board[5])
        print(' '*6,'____|___|___')
        print(' '*6,'    |   |   ')
        print(' '*6,' ',board[0], '|',board[1],'|',board[2])
        print(' '*6,'    |   |   ')
        print('\n'*4)
    else:
        print('\n'*100)
        print(' '*6,'    |   |   ',' '*20,'    |   |   ')
        print(' '*6,' ',board[6], '|',board[7],'|',board[8],' '*21,' ','7', '|','8','|','9')
        print(' '*6,'____|___|___',' '*20,'____|___|___')
        print(' '*6,'    |   |   ',' '*20,'    |   |   ')
        print(' '*6,' ',board[3], '|',board[4],'|',board[5],' '*21,' ','4', '|','5','|','6')
        print(' '*6,'____|___|___',' '*20,'____|___|___')
        print(' '*6,'    |   |   ',' '*20,'    |   |   ')
        print(' '*6,' ',board[0], '|',board[1],'|',board[2],' '*21,' ','1', '|','2','|','3')
        print(' '*6,'    |   |   ',' '*20,'    |   |   ')
        print('\n'*4)

# A function to ask the player for which box they want to mark
def ask_player(player,board):
    while True:
        if player=='p1':
            strposition=input('Player 1:  What square would you like to mark?    ')
        elif player=='p2':
            strposition=input('Player 2:  What square would you like to mark?    ')
        try:
            position=int(strposition)
        except:
            print('Bad input.  Please only enter an integer from 1 to 9.')
            continue
        if position not in range(1,10) :
            print('Bad input.  Please only enter an integer from 1 to 9.')
            continue
        if board[position-1] != ' ':
            print('This space is taken.  Please pick an open space.')
            continue
        else:
            return position

# Check to see if there is a winner
def check_winner(board):
    space=False
    rows=[str(board[0]+board[1]+board[2]),str(board[3]+board[4]+board[5]),str(board[6]+board[7]+board[8])]
    columns=[str(board[0]+board[3]+board[6]),str(board[1]+board[4]+board[7]),str(board[2]+board[5]+board[8])]
    diagonals=[str(board[0]+board[4]+board[8]),str(board[6]+board[4]+board[2])]
    for check in rows:
        if check=='XXX' or check=='OOO':
            print('Congratulations!  You won!')
            return True
    for check in columns:
        if check=='XXX' or check=='OOO':
            print('Congratulations!  You won!')
            winner==True
            return True
    for check in diagonals:
        if check=='XXX' or check=='OOO':
            print('Congratulations!  You won!')
            winner==True
            return True
    for c in board:
        if c==' ':
            space=True
    if space==True:
        return False
    elif space==False:
        print("It's a tie!  Try again!")
        return True

# Ask to play ask to play again
def ask_playagain():
    while True:
        playagain=input('Would you like to play again?')
        if playagain=='y' or playagain=='Y':
            return True
        elif playagain=='n' or playagain=='N':
            print('I hope this game was fun and you want to play it later!')
            return False
        else:
            print('Bad input.  Please enter either Y or N.')

# Start The Game
keepplaying=True
while keepplaying==True:
    while True:
        pinput=input('Player 1:  Would you like X or O?    ')
        if pinput == 'x' or pinput =='X':
            players={'p1':'X','p2': 'O'}
            break
        elif pinput == 'o' or pinput == 'O':
            players={'p1':'O','p2': 'X'}
            break
        else:
            print('Bad input.  Please only enter X or O')

# Instructions
    print('\n'*4)
    print('Instructions:')
    print('Enter the number of the position you would like to mark based on the pattern')
    print('below when it is your turn.')
    test_board=list(range(1,11))
    display_board(test_board)

# Initialize the game
    import random
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    flip=random.randint(0,1)
    if flip==0:
        player='p1'
    else:
        player='p2'
    winner=False

# Run the game
    while winner==False:
        pos=ask_player(player,board)
        board[pos-1]=players[player]
        display_board(board)
        if check_winner(board)==True:
            winner=True
        if player=='p1':
            player='p2'
        elif player=='p2':
            player='p1'
    keepplaying=ask_playagain()
