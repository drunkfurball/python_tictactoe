'''
Tic Tac Toe by drunkfurball
4/3/2016
'''
def print_board(b):
    for n in b:
       print "%s|%s|%s" % (n[0],n[1],n[2])

def player_input(p):
    print
    while (True):
        print "%s's turn." % (p)
        pick = str(raw_input("Which space will you capture ['Q' to quit]?"))
        if pick=='q' or pick=='Q':
            game_over()
        pick = int(pick)
        pick -= 1
        if (0<=pick<=8)!=True:
            print "Invalid. Try again."
        elif board[pick/3][(pick%3)]=='X' or board[pick/3][(pick%3)]=='O':
            print "That square is already taken. Try again."
        else:
            break
    board[pick/3][(pick%3)] = p

def winner(b):
    for n in range(3):#horizontal
        if b[n][0]==b[n][1]==b[n][2]:
            return True
    for m in range(3):#vertical
        if b[0][m]==b[1][m]==b[2][m]:
            return True
    if (b[0][0]==b[1][1]==b[2][2]) or (b[0][2]==b[1][1]==b[2][0]):
        return True

def tie(b):
    for a in range(3):
        for c in range(3):
            if b[a][c] != 'X' and b[a][c] != 'O':
                return False
    return True

def game_over():
    print "Thanks for playing!"
    quit()



while (True):
    board = [[1,2,3],[4,5,6],[7,8,9]]
    player = 'X'
    while (True):
        print_board(board)
        player_input(player)
        if winner(board):
            print_board(board)
            print "%s wins!" % (player)
            break
        elif tie(board):
            print_board(board)
            print "The game ends in a draw."
            break
        else:
            if player=='X':
                player='O'
            else:
                player='X'
    yorn = raw_input("Would you like to play again ['N' to quit]?")
    if yorn == 'N' or yorn == 'n':
        break
game_over()
