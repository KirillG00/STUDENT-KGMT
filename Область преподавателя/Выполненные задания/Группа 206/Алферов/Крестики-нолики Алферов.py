import random

def create_board():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

def print_board(board):
    for row in board:
        print('|'.join(row))
    print('\n')

def player_move(board, row, col):
    if board[row][col] == ' ':
        board[row][col] = 'X'
        return True
    else:
        return False

def computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 'O'

def check_win(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]): # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]): # Check columns
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]): # Check diagonals
        return True
    return False

def main():
    board = create_board()
    print_board(board)

    while True:
        row = int(input("Выберите линию (0-2): "))
        col = int(input("Выберите строку (0-2): "))

        if player_move(board, row, col):
            print_board(board)

            if check_win(board, 'X'):
                print("Игрок победил!")
                break

            computer_move(board)
            print_board(board)

            if check_win(board, 'O'):
                print("ИИ победил!")
                break

if __name__ == "__main__":
    main()
