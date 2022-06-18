class Solution:
    def countPoints(self, rings: str) -> int:
        checked = set()
        ans = 0
        hashmap = {}
        for i in range(10):
            hashmap[i] = set()
        for i in range(0, len(rings) - 1, 2):
            # get pole num
            pole = int(rings[i + 1])
            color = rings[i]
            hashmap[pole].add(color)
            if len(hashmap[pole]) == 3 and pole not in checked:
                checked.add(pole)
                ans += 1
        return ans
