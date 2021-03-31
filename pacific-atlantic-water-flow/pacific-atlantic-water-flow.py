class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return None
        def bfs(points):
            visited = set(points)
            neighbors = [[1,0],[-1,0],[0,-1],[0,1]]
            while points:
                i,j = points.pop()
                for n1,n2 in neighbors:
                    p1 = i+n1
                    p2 = j+n2
                    if 0 <= p1 < row and 0 <= p2 < col and (p1,p2) not in visited and matrix[p1][p2] >= matrix[i][j]:
                        visited.add((p1,p2))
                        points.append((p1,p2))
            return visited

        row = len(matrix)
        col = len(matrix[0])

        pacific = []
        atlantic = []

        for i in range(row):
            pacific.append((i,0))
            atlantic.append((i,col-1))

        for j in range(col):
            pacific.append((0,j))
            atlantic.append((row-1,j))

        pacific = bfs(pacific)
        atlantic = bfs(atlantic)

        ans = pacific.intersection(atlantic)
        return ans

 
            