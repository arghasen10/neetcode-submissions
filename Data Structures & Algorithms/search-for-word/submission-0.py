class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board or not board[0]:
            return False
        
        rows, cols = len(board), len(board[0])
        if len(word) > rows*cols:
            return False

        def dfs(row, col, index):
            if index == len(word):
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[index]:
                return False
            char = board[row][col]
            board[row][col] = None
            found = dfs(row+1, col, index+1) or dfs(row-1, col, index+1) or dfs(row, col+1, index+1) or dfs(row, col-1, index+1)
            board[row][col] = char
            return found
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False