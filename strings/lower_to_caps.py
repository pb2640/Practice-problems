class Solution:
    def toLowerCase(self, s: str) -> str:
        # for every letter check if it is upper
        is_upper  = lambda x: 'A'<=x<='Z'
        ans = ""
        for letter in s:
            if(is_upper(letter)):
                ans+=chr(ord(letter)+32)
            else:
                ans+=letter
        return ans
        # big = "QWERTYUIOPASDFGHJKLZXCVBNM"
        # small = "qwertyuiopasdfghjklzxcvbnm"
        # big  =  set(big)
        # small = set(small)
        # ans = ""
        # for letter in s:
        #     if letter in big:
        #         ans+=letter.lower()
        #     else:
        #         ans+=letter
        # return ans
        