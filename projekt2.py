# Definice šachovnice
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


# Definice hry
def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Which one to move?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nWhich one to move")
            continue

        # Lovest cout to win is 5, so since 5th move there will be check if any player won.
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" Player" + turn + " won.")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" Player" + turn + " won.")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" Player" + turn + " won.")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" Player" + turn + " won.")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" Player" + turn + " won.")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" Player" + turn + " won.")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" Player" + turn + " won.")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" Player" + turn + " won.")
                break

                # If there will be 9 turns game will end with a tie.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Change of players
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

if __name__ == "__main__":
    game()
