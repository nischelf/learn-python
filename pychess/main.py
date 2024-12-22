from colorama import Back, Fore, Style, init
import fen

FEN = fen.FEN()

# Initialize colorama
init(autoreset=True)

files = 8
ranks = 8
row_count = ranks
board = []

# Populate the board with field names and placeholders for pieces
for i in range(ranks):
    row = []
    for j in range(files):
        # Use chess notation for each cell (e.g., A1, B2, etc.)
        # Convert ASCII to character. 65 is 'A' and then 65 + 1 -> B
        field_name = f"{chr(65 + j)}{ranks - i}"
        row.append({"field": field_name, "piece": None})
    board.append(row)


def print_board():
    # Piece colors
    white_pieces = "PNRBKQ"
    black_pieces = "pnrbkq"

    # Display the board
    for i in range(ranks):
        print(f"{ranks - i} ", end="")  # Print row label
        for j in range(files):
            if (i + j) % 2 == 0:
                cell_color = Back.WHITE
            else:
                cell_color = Back.BLACK

            # Get the piece or empty space
            piece = board[i][j]["piece"] or " "

            # Apply color to the piece
            if piece in white_pieces:
                piece_color = Fore.BLUE
            elif piece in black_pieces:
                piece_color = Fore.RED
            else:
                piece_color = ""

            # Print the cell with the piece or empty space
            print(cell_color + piece_color + f" {piece} " + Style.RESET_ALL, end="")
        print()  # End of row

    # Print column labels
    print("   " + "  ".join([chr(65 + i) for i in range(files)]))  # A-H


# Place some example pieces
board[0][4]["piece"] = "k"  # Black King
board[0][0]["piece"] = "r"  # Black rook
board[0][1]["piece"] = "n"  # Black knight
board[7][4]["piece"] = "K"  # White King
board[7][0]["piece"] = "R"  # White rook
board[7][1]["piece"] = "N"  # White knight

print_board()


def move_piece(current, target):
    piece = str()
    # print(board)
    for i in range(ranks):
        for j in range(files):
            if board[i][j]["field"] == current:
                piece = board[i][j]["piece"]
                board[i][j]["piece"] = None

    for i in range(ranks):
        for j in range(files):
            if board[i][j]["field"] == target:
                board[i][j]["piece"] = piece


whites_turn = True

while True:
    if whites_turn:
        print("White to move")
        whites_turn = False
    else:
        print("Black to move")
        whites_turn = True

    move = input("Input your move. Like this b1xc3: ")
    moves = move.split("x")

    if moves[0] == moves[1]:
        print("Invalid move")
        continue

    move_piece(moves[0].upper(), moves[1].upper())

    print_board()
    print(FEN.export(board, whites_turn))
