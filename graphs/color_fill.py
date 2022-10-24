class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        visited = set()
        q = []
        q.append((sr, sc))
        visited.add((sr, sc))
        initial_color = image[sr][sc]

        while q:
            curr = q.pop()
            curr_i, curr_j = curr[0], curr[1]

            # up
            if (
                curr_i > 0
                and image[curr_i - 1][curr_j] == initial_color
                and (curr_i - 1, curr_j) not in visited
            ):
                q.append((curr_i - 1, curr_j))
                visited.add((curr_i - 1, curr_j))
            # down
            if (
                curr_i < len(image) - 1
                and image[curr_i + 1][curr_j] == initial_color
                and (curr_i + 1, curr_j) not in visited
            ):
                q.append((curr_i + 1, curr_j))
                visited.add((curr_i + 1, curr_j))
            # left
            if (
                curr_j > 0
                and image[curr_i][curr_j - 1] == initial_color
                and (curr_i, curr_j - 1) not in visited
            ):
                q.append((curr_i, curr_j - 1))
                visited.add((curr_i, curr_j - 1))
            # right
            if (
                curr_j < len(image[0]) - 1
                and image[curr_i][curr_j + 1] == initial_color
                and (curr_i, curr_j + 1) not in visited
            ):
                q.append((curr_i, curr_j + 1))
                visited.add((curr_i, curr_j + 1))

            image[curr_i][curr_j] = color
        return image
