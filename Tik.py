board = [' 'for x in range(10) ]

def insertLetter(pos, letter):
    board[pos] = letter

def isSpaceFree(pos):
    return (board[pos]==' ')

def board_dia(board):
    print("   |   |   ")
    print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    print("   |   |   ")

def isboardFull():
    if board.count(' ')>=1:
        return False
    else: 
        return True

def winner(b,l):
    return ((b[1]==l and b[2]==l and b[3]==l)or
    (b[4]==l and b[5]==l and b[6]==l) or 
    (b[7]==l and b[8]==l and b[9]==l) or
    (b[1]==l and b[4]==l and b[7]==l) or 
    (b[2]==l and b[5]==l and b[8]==l) or
    (b[3]==l and b[6]==l and b[9]==l) or 
    (b[1]==l and b[5]==l and b[9]==l) or 
    (b[7]==l and b[5]==l and b[3]==l))

def playermove():
    run = True
    while run:
        move = input("Please press any number B/W one to nine: ")
        try:
            move = int(move)
            if (move < 10) and (move > 0):
                if isSpaceFree(move):
                    run = False
                    insertLetter(move, "X")
                else:
                    print("Be careful, This place already occupied")
            else:
                print("Wrong key pressed, Please pressed B/W 1-9 only")
        
        except:
            print("Please press a number.")

def computermove():
    possiblemoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0 ] 
    
    move = 0
    for let in ['O', 'X']:
        for i in possiblemoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if winner(boardcopy, let):
                move = i
                return move

    corners = []
    for j in possiblemoves:
        if j in [1, 3, 7, 9]:
            corners.append(j)
    if len(corners) > 0:
        move = selectRandom(corners)
        return move
    
    if 5 in possiblemoves:
        move = 5
        return move

    middle = []
    for i in possiblemoves:
        if i in [2, 4, 6, 8]:
            middle.append(i)
    if len(middle) > 0:
        move = selectRandom(middle)
        return move

def selectRandom(list1):
    import random

    length = len(list1)
    getrandom = random.randrange(0, length)
    return list1[getrandom]

def main():
    print("welcome to the TIK TAK TOE")
    board_dia(board)

    while not(isboardFull()):
        if not(winner(board, 'O')):
            playermove()
            board_dia(board)
        else:
            print()
            print("||||  Sorry, You loose by computer!")
            print()
            break
        
        if not(winner(board, 'X')):
            move = computermove()
            if move not in [x for x in range(1,10)]: 
                print(" ")
            else: 
                insertLetter(move, 'O')
                print('Computer placed "O" on position', move,':')
                board_dia(board)
        else: 
            print()
            print("||||  Oooohu!, You Win")
            print()
            break
        
        if (board.count(' ') == 1) or not(board.count(' ') < 9):
            print()
            print("||||  Tie Game")
            print()
            break

while True:
    userWant = str(input("Are you ready for start the game. [ Y / N ]:  "))
    if userWant.lower()== "y" : 
        board = [' 'for x in range(10) ]
        print("------------------------")
        main()
    else:
        break

