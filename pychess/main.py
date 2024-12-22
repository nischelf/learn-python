#!/usr/bin/env python
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
            piece = board[i][j]["piece"]

            if piece is None:
                piece = " "

            piece_name = piece["name"] if isinstance(piece, dict) else piece

            # Apply color to the piece
            if piece_name in white_pieces:
                piece_color = Fore.BLUE
            elif piece_name in black_pieces:
                piece_color = Fore.RED
            else:
                piece_color = ""

            # Print the cell with the piece or empty space
            print(
                cell_color + piece_color + f" {piece_name} " + Style.RESET_ALL, end=""
            )
        print()  # End of row

    # Print column labels
    print("   " + "  ".join([chr(65 + i) for i in range(files)]))  # A-H


# Setup standard position via FEN
board = FEN.read("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", board)

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
                board[i][j]["piece"]["moved"] = True


whites_turn = True
move_number = 0

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
    move_number += 1

    print_board()
    print(FEN.export(board, whites_turn, str(move_number / 2 + 1)[0]))
