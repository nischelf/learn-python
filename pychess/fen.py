class FEN:
    def read(self, fen_code):
        print(fen_code)
        return fen_code

    def export(self, board):
        code = []
        count = 0

        for i in range(8):
            for j in range(8):
                if board[i][j]["piece"] is None:
                    count += 1
                    # print(count)
                    if count == 8 or j == 7:
                        code.append(count)
                        count = 0
                else:
                    if count > 0:
                        code.append(count)
                        count = 0
                    code.append(board[i][j]["piece"])

        print(code)
        return code
