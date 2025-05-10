def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while not check_winner(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

            # Ensure the input is within bounds
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter numbers between 0 and 2.")
                continue

            if board[row][col] == " ":
                board[row][col] = player
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("That spot is already taken! Try again.")

        except ValueError:
            print("Invalid input. Please enter integers for row and column.")

        # Check for a tie (board is full)
        if is_full(board) and not check_winner(board):
            print_board(board)
            print("The game is a tie!")
            break

    print_board(board)
    # Fixing the winner message to display the player who just made the winning move
    if check_winner(board):
        if player == "X":
            print("Player O wins!")
        else:
            print("Player X wins!")

if __name__ == "__main__":
    tic_tac_toe()