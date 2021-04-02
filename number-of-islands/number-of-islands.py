from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        islands = 0
        
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == "1":
                    islands += 1
                    self.BFS(row, col, grid)
        return islands
    
    def BFS(self, row, col, grid):
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        row_len = len(grid)
        col_len = len(grid[0])
        q = deque()
        q.append((row, col))
        
        while q:
            row, col = q.popleft()
            for x, y in directions:
                newRow = row + x
                newCol = col + y
                if row_len > newRow >= 0 and col_len > newCol >= 0 and grid[newRow][newCol] == "1":
                    grid[newRow][newCol] = "0"
                    q.append((newRow, newCol))