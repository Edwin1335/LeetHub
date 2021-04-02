from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and self.DFS(row, col, board, word, 0):
                    return True
        return False
    
    def DFS(self, row, col, board, word, index):
            if index == len(word):
                return True
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or word[index] != board[row][col]:
                return False
            
            temp = board[row][col]
            board[row][col] = "#"
            
            res = \
            self.DFS(row+1, col, board, word, index + 1) or \
            self.DFS(row-1, col, board, word, index + 1) or \
            self.DFS(row, col+1, board, word, index + 1) or \
            self.DFS(row, col-1, board, word, index + 1)
            
            board[row][col] = temp
            return res
            
            