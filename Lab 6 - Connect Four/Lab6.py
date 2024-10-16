def initialize_board(num_rows, num_cols):
    board = []
    for i in range(num_rows):
        lines = []
        for j in range(num_cols):
            lines.append("- ")
        board.append(lines)
    return board
def all_chips_filled(board):
    for row in board:
        for cell in row:
            if cell == "- ":
                return False
    return True

def print_board(board):
    print()
    for i in board:
        for j in i:
            print(j, end="")
        print()

def insert_chip(board, col, chip_type):
    for rows in range(len(board) - 1, -1, -1):
        if board[rows][col] == "- ":
            board[rows][col] = chip_type
            return rows
    return None

def check_if_winner(board, col, row, chip_type):
    count = 0
    for i in range(len(board)):
        if board[i][col] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    count = 0
    for i in range(len(board[0])):
        if board[row][i] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    count = 0
    for i in range(-3, 1):
        if (row + i >= 0 and row + i < len(board)) and (col - i >= 0 and col - i < len(board[0])):
            if board[row + i][col - i] == chip_type:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    count = 0
    for i in range(-3, 1):
        if (row + i >= 0 and row + i < len(board)) and (col + i >= 0 and col + i < len(board[0])):
            if board[row + i][col + i] == chip_type:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    return False

def main():
    try:
        height = int(input("What would you like the height of the board to be? "))
        length = int(input("What would you like the length of the board to be? "))
    except EOFError:
        print("No input provided for board dimensions. Exiting.")
        return

    board = initialize_board(height, length)
    print_board(board)

    print("Player 1: x")
    print("Player 2: o")

    while True:
        try:
            if all_chips_filled(board):
                print("Draw. Nobody wins.")
                break
            while True:
                player1_col = int(input("Player 1: Which column would you like to choose? "))
                if 0 <= player1_col < length:
                    break
                print(f"Invalid input. Please enter a number between 0 and {length - 1}.")

            row = insert_chip(board, player1_col, "x ")
            if row is None:
                print(f"Column {player1_col} is full. Choose a different column.")
                continue

            print_board(board)
            if check_if_winner(board, player1_col, row, "x "):
                print("Player 1 won the game!")
                break

            while True:
                player2_col = int(input("Player 2: Which column would you like to choose? "))
                if 0 <= player2_col < length:
                    break
                print(f"Invalid input. Please enter a number between 0 and {length - 1}.")

            row = insert_chip(board, player2_col, "o ")
            if row is None:
                print(f"Column {player2_col} is full. Choose a different column.")
                continue

            print_board(board)
            if check_if_winner(board, player2_col, row, "o "):
                print("Player 2 won the game!")
                break
        except EOFError:
            print("Draw. Nobody wins.")
            break

if __name__ == "__main__":
    main()
