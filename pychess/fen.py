import pieces

create_piece = pieces.create_piece

# FEN Rules: https://www.chess.com/terms/fen-chess


class FEN:
    def read(self, fen_code, board):
        # TODO: pass data castle rights
        # fen_data = fen_code.split(" ")
        pieces_on_Board = fen_code.split(" ")[0]
        pieces_on_row = pieces_on_Board.split("/")
        # print(type(pieces_on_row))
        print(pieces_on_row)
        for row_idx, row in enumerate(pieces_on_row):
            col_idx = 0
            for char in row:
                if char.isdigit():
                    # Empty squares
                    col_idx += int(char)
                elif char.isalpha():
                    # Piece placement
                    if char == "k":
                        board[row_idx][col_idx]["piece"] = create_piece(char)
                    else:
                        board[row_idx][col_idx]["piece"] = create_piece(char)
                    col_idx += 1
        return board

    def export(self, board, whites_turn, fullmove_number):
        code = []
        count = 0

        for i in range(8):
            row = []
            for j in range(8):
                if board[i][j]["piece"] is None:
                    count += 1
                    # print(count)
                    if count == 8 or j == 7:
                        row.append(count)
                        count = 0
                else:
                    if count > 0:
                        row.append(count)
                        count = 0
                    row.append(board[i][j]["piece"]["name"])
            code.append(row)

        # print(code)

        fen_str = str()

        for r in code:
            joined_string = "".join(map(str, r))
            fen_str += joined_string + "/"

        fen_str = fen_str[:-1]
        if whites_turn:
            fen_str += " w"
        else:
            fen_str += " b"

        # TODO: Castle Rights, En Passant, Halfmove Clock
        fen_str += " - - 0 " + fullmove_number
        return fen_str
