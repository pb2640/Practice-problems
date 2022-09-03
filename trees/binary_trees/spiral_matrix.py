class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        i, j = 0, 0
        ans = []
        # direction reference
        ref = {"right": "down", "down": "left", "left": "up", "up": "right"}
        direction = "right"
        while len(visited) < len(matrix) * (len(matrix[0])):
            ans.append(matrix[i][j])
            visited.add((i, j))
            if direction == "right":
                # check if next ele exists and was not visited
                if j < len(matrix[i]) - 1 and (i, j + 1) not in visited:
                    j += 1
                else:
                    i += 1
                    direction = ref[direction]
                    continue
            if direction == "down":
                # check if next ele exists and was not visited
                if i < len(matrix) - 1 and (i + 1, j) not in visited:
                    i += 1
                else:
                    j -= 1
                    direction = ref[direction]
                    continue
            if direction == "left":
                # check if next ele exists and was not visited
                if j > 0 and (i, j - 1) not in visited:
                    j -= 1
                else:
                    i -= 1
                    direction = ref[direction]
                    continue
            if direction == "up":
                # check if next ele exists and was not visited
                if i > 0 and (i - 1, j) not in visited:
                    i -= 1
                else:
                    j += 1
                    direction = ref[direction]
                    continue
        return ans
