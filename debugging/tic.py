#!/usr/bin/python3
def print_board(board):
    """
    Prints the current state of the tic-tac-toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner on the board.

    Returns:
        bool: True if there is a winner, False otherwise.
    """
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """
    Checks if the board is full.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to play the tic-tac-toe game.
    """
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}, it's your turn!")

        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter a number between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            board[row][col] = current_player

            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            # Switch players
            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    tic_tac_toe()
