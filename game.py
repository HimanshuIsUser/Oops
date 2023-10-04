def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        try:
            row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

            if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
                raise ValueError("Invalid input. Try again.")

            board[row][col] = current_player
        except ValueError as e:
            print(e)
            continue

        print_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player} wins! Congratulations!")
            break

        if is_full(board):
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
