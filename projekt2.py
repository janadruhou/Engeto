# Definice šachovnice
Board = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in Board:
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
        printBoard(Board)
        print("It's your turn," + turn + ".Which one to move?")

        move = input()

        if Board[move] == ' ':
            Board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nWhich one to move")
            continue

        # Lovest cout to win is 5, so since 5th move there will be check if any player won.
        if count >= 5:
            if Board['7'] == Board['8'] == Board['9'] != ' ':  # across the top
                printBoard(Board)
                print("\nGame Over.\n")
                print(" Player" + turn + " won.")
                break
            elif Board['4'] == Board['5'] == Board['6'] != ' ':  # across the middle
                printBoard(Board)
                print("\nGame Over.\n")
                print(" Player" + turn + " won.")
                break
            elif Board['1'] == Board['2'] == Board['3'] != ' ':  # across the bottom
                printBoard(Board)
                print("\nGame Over.\n")
                print(" Player" + turn + " won.")
                break
            elif Board['1'] == Board['4'] == Board['7'] != ' ':  # down the left side
                printBoard(Board)
                print("\nGame Over.\n")
                print(" Player" + turn + " won.")
                break
            elif Board['2'] == Board['5'] == Board['8'] != ' ':  # down the middle
                printBoard(Board)
                print("\nGame Over.\n")
                print(" Player" + turn + " won.")
                break
            elif Board['3'] == Board['6'] == Board['9'] != ' ':  # down the right side
                printBoard(Board)
                print("\nGame Over.\n")
                print(" Player" + turn + " won.")
                break
            elif Board['7'] == Board['5'] == Board['3'] != ' ':  # diagonal
                printBoard(Board)
                print("\nGame Over.\n")
                print(" Player" + turn + " won.")
                break
            elif Board['1'] == Board['5'] == Board['9'] != ' ':  # diagonal
                printBoard(Board)
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
game()
