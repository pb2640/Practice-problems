class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_island = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                pos = (i, j)
                isl = grid[i][j]
                if pos not in visited and isl == "1":
                    num_island += 1
                    visited.add(pos)
                    q = [pos]

                    while q:
                        a, b = q.pop()
                        if (
                            a > 0
                            and (a - 1, b) not in visited
                            and grid[a - 1][b] == "1"
                        ):
                            visited.add((a - 1, b))
                            q.append((a - 1, b))
                        if (
                            b > 0
                            and (a, b - 1) not in visited
                            and grid[a][b - 1] == "1"
                        ):
                            visited.add((a, b - 1))
                            q.append((a, b - 1))
                        if (
                            a < len(grid) - 1
                            and (a + 1, b) not in visited
                            and grid[a + 1][b] == "1"
                        ):
                            visited.add((a + 1, b))
                            q.append((a + 1, b))
                        if (
                            b < len(grid[a]) - 1
                            and (a, b + 1) not in visited
                            and grid[a][b + 1] == "1"
                        ):
                            visited.add((a, b + 1))
                            q.append((a, b + 1))
        return num_island
