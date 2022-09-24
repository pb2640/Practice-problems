class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        rotten_coords = set()
        rot = 0  # track initial rotten oranges
        fresh = 0  # track initital fresh
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i, j))
                    rotten_coords.add((i, j))
                    rot += 1
                if grid[i][j] == 1:
                    fresh += 1
        potential_rotten = rot + fresh
        if not q:
            return -1
        t = 0
        new_q = []

        rotten_checked = set()
        while True:
            if q:
                new_q = []
                while q:
                    coord = q.pop()
                    if coord in rotten_checked:
                        continue
                    rotten_checked.add(coord)
                    i, j = coord
                    # one above
                    if (
                        i > 0
                        and grid[i - 1][j] != 0
                        and (i - 1, j) not in rotten_checked
                    ):
                        rotten_coords.add((i - 1, j))
                        new_q.append((i - 1, j))
                        grid[i - 1][j] = 2
                    # one below
                    if (
                        i < len(grid) - 1
                        and grid[i + 1][j] != 0
                        and (i + 1, j) not in rotten_checked
                    ):
                        rotten_coords.add((i + 1, j))
                        new_q.append((i + 1, j))
                        grid[i + 1][j] = 2
                    # one left
                    if (
                        j > 0
                        and grid[i][j - 1] != 0
                        and (i, j - 1) not in rotten_checked
                    ):
                        rotten_coords.add((i, j - 1))
                        new_q.append((i, j - 1))
                        grid[i][j - 1] = 2
                    # one right

                    if (
                        j < len(grid[i]) - 1
                        and grid[i][j + 1] != 0
                        and (i, j + 1) not in rotten_checked
                    ):
                        rotten_coords.add((i, j + 1))
                        new_q.append((i, j + 1))
                        grid[i][j + 1] = 2

                t += 1
                # check if every orange in grid rotten, if yes break
                if len(rotten_coords) == potential_rotten:
                    break
            else:
                if new_q:
                    q = new_q
                else:
                    break
        return t
