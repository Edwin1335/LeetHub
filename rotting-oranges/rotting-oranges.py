from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        rotten_q = deque()
        found_oranges = False
        seconds = -1
        for r in range(row):
            for c in range(col):
                if grid[r][c] in [1, 2]:
                    found_oranges = True
                    
                if grid[r][c] == 2:
                    rotten_q.append((r, c))
                
        if not found_oranges:
            print("Not Found")
            return 0
        
        while rotten_q:
            seconds += 1
            print(rotten_q, seconds)
            for _ in range(len(rotten_q)):
                x, y = rotten_q.popleft()
                rotten_q += self.rot_neighbors(x, y, row, col, grid)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return -1
                
        return seconds
    
    def rot_neighbors(self, r, c, rl, cl, grid):
        check_loc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        out = []
        for x, y in check_loc:
            newRow = x + r
            newCol = y + c
            if rl > newRow >= 0 and cl > newCol >= 0 and grid[newRow][newCol] == 1:
                grid[newRow][newCol] = 2
                out.append((newRow, newCol))
        return out
        
        