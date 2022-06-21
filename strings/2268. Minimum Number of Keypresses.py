class Solution:
    def minimumKeypresses(self, s: str) -> int:
        # strategy : be greedy. count the frequency of letters
        # map them accordingly
        ref = {}
        arr = []
        # O(n)
        for char in s:
            if char in ref:
                ref[char] += 1
            else:
                ref[char] = 1
        for char in ref:
            arr.append([char, ref[char]])
        # O(nlogn)
        arr.sort(key=lambda x: -x[1])
        keypad = {1: 9, 2: 9, 3: 9}
        ans = 0
        for char in arr:
            if keypad[1]:
                ans += char[1]
                keypad[1] -= 1
            elif keypad[2]:
                ans += char[1] * 2
                keypad[2] -= 1
            else:
                ans += char[1] * 3
                keypad[3] -= 1
        return ans
