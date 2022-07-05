class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        1.Reverse the array plainly
        2.reverse each word
        """
        l = 0
        r = len(s) - 1
        # plain reverse
        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
        # print(s)
        # reverse each word
        stop = 0
        start = 0

        while stop < len(s) - 1:
            # find start and stop indexes in string
            while stop < len(s) - 1 and s[stop + 1] != " ":
                # print(stop)
                stop += 1
            ref = stop
            while start < stop:
                # swap
                temp = s[start]
                s[start] = s[stop]
                s[stop] = temp
                start += 1
                stop -= 1
            # print(s)

            start, stop = ref + 2, ref + 2

        """
        Do not return anything, modify s in-place instead.
        """
