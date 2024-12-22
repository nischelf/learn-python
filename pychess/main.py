import argparse
from colorama import Back, Fore, Style, init

# Initialize colorama
init(autoreset=True)

# PRINT BOARD
files = 8
ranks = 8
row_count = 8

for i in range(ranks):  # Rows of the board
    row = ""
    print("%d\r", row_count, end="")
    row_count -= 1
    for j in range(files):  # Columns of the board
        if (i + j) % 2 == 0:  # Alternate black and white cells
            row += Back.WHITE + "   " + Style.RESET_ALL
        else:
            row += Back.BLACK + "   " + Style.RESET_ALL
    print(row)
print("   A  B  C  D  E  F  G  H")
