# unsuccessful attemp
class Solution:
    def decodeString(self, s: str) -> str:
        ss = []
        ns = []
        ans = ""
        i = 0
        num = ""
        while i < len(s):
            if ord(s[i]) > 47 and ord(s[i]) < 58:
                while s[i] != "[":
                    num += s[i]
                    i += 1
                ns.append(int(num))
                num = ""
            if s[i] == "[":
                # fill stack with str
                while s[i] != "]":
                    if ord(s[i]) > 47 and ord(s[i]) < 58:
                        num = ""
                        while s[i] != "[":
                            num += s[i]
                            i += 1
                        ns.append(int(num))

                    else:
                        ss.append(s[i])
                        i += 1
            if s[i] == "]":
                temp_str = ""
                while ss:
                    char = ss.pop()
                    if char == "[":
                        break
                    else:
                        temp_str = "" + char + temp_str
                ans += ns.pop() * temp_str
            else:
                ans += s[i]
            i += 1
        return ans
