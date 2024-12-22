# FEN Rules: https://www.chess.com/terms/fen-chess
class FEN:
    def read(self, fen_code):
        print(fen_code)
        return fen_code

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
                    row.append(board[i][j]["piece"])
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
