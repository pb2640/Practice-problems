"""
lets say you find a piece of land in your grid, first check if that piecve has been 
counted already as a part of an island .
if yes skip not next piece and recurse 
else
do a bfs 
    
    """


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for i in range(len(grid)):

            for j in range(len(grid[i])):
                q = []
                coord = (i, j)
                ele = grid[i][j]
                if coord in visited or ele == "0":
                    continue
                else:
                    q.append(coord)

                    while q:
                        coord = q.pop(0)
                        visited.add(coord)
                        idx, jdx = coord
                        # check if its not a corner ele
                        # left
                        if jdx > 0:
                            ele = grid[idx][jdx - 1]
                            coord = (idx, jdx - 1)
                            if ele == "1" and coord not in visited:
                                q.append(coord)
                                visited.add(coord)
                        # upper
                        if idx > 0:
                            ele = grid[idx - 1][jdx]
                            coord = (idx - 1, jdx)
                            if ele == "1" and coord not in visited:
                                q.append(coord)
                                visited.add(coord)
                        # right
                        if jdx < len(grid[idx]) - 1:
                            ele = grid[idx][jdx + 1]
                            coord = (idx, jdx + 1)
                            if ele == "1" and coord not in visited:
                                q.append(coord)
                                visited.add(coord)
                        # lower
                        if idx < len(grid) - 1:
                            ele = grid[idx + 1][jdx]
                            coord = (idx + 1, jdx)
                            if ele == "1" and coord not in visited:
                                q.append(coord)
                                visited.add(coord)
                    count += 1
        return count
