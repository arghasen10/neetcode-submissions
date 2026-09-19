class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            S = {}
            for col in range(9):
                if board[row][col] != ".":
                    if board[row][col] in S:
                        return False
                    S[board[row][col]] = 1
        
        for row in range(9):
            S = {}
            for col in range(9):
                if board[col][row] != ".":
                    if board[col][row] in S:
                        return False
                    S[board[col][row]] = 1

        for i in range(3):
            for j in range(3):
                S = {}
                for row in range(2*i+i, 2*i+i+3):
                    for col in range(2*j+j, 2*j+j+3):
                        if board[row][col] != ".":
                            if board[row][col] in S:
                                return False
                            S[board[row][col]] = 1

        return True