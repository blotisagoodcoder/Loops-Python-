board = {
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' ',}

board_keys=[]

for key in board:
    board_keys.append(key)

def printBoard():
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('==-*-==')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('==-*-==')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('==-*-==')
def game():
    turn = 'x'
    count = 0
    for i in range (10):
        printBoard(board)
        print("YOUR TURN! FIGHT!," + turn + "Move?")
        move = input()
        if board[move] == ' ':
            board[move] = turn
            count += 1 
        else: 
            print("DUMBAHH ITS ALR FILLED!")
            continue
        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ':
                printBoard(board)
                print("\nGame Over! loser\n")
                print(" **** " - +turn +"won. ****")
                break
            elif board['4'] == board['5'] == board['6'] != ' ':
                printBoard(board)
                print("\nGame Over! loser\n")
                print(" **** " - +turn +"won. ****")
                break
            elif board['1'] == board['2'] == board['3'] != ' ':
                printBoard(board)
                print("\nGame Over! loser\n")
                print(" **** " - +turn +"won. ****")
                break
            elif board['2'] == board['5'] == board['8'] != ' ':
                printBoard(board)
                print("\nGame Over! loser\n")
                print(" **** " - +turn +"won. ****")
                break
            elif board['3'] == board['6'] == board['9'] != ' ':
                printBoard(board)
                print("\nGame Over! loser\n")
                print(" **** " - +turn +"won. ****")
                break
            elif board['7'] == board['5'] == board['3'] != ' ':
                printBoard(board)
                print("\nGame Over! loser\n")
                print(" **** " - +turn +"won. ****")
                break
            elif board['1'] == board['5'] == board['9'] != ' ':
                printBoard(board)
                print("\nGame Over! loser\n")
                print(" **** " - +turn +"won. ****")
                break
            if count == 9:
                print("\nGAME OVER LOSER\n")
                print("ITS A TIE! DAMNI-")

            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

            restart = input("LETS PLAY AGAIN LOSER!! ILL WIN NEXT TIMME! (y/n)")
            if restart == 'y' or restart == 'Y':
                for key in board_keys:
                    board[key] = " "

                game()
        
        if __name__ == "__main__":
            game()