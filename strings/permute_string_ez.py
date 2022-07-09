class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ref = {}
        for letter in s:
            if letter in ref:
                ref[letter]+=1
            else:
                ref[letter] = 1
        ans = ""
        for letter in order:
            if letter in ref:
                ans+=letter*ref[letter]
                ref.pop(letter)
        for letter in ref:
            ans+=letter*ref[letter]
        return ans
        