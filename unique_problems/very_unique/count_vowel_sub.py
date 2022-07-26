# unsuccessful att.
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans = 0
        vowels = {"a", "e", "i", "o", "u"}
        i = 0
        while i < len(word):
            letter = word[i]
            if letter not in vowels:
                i += 1
                continue
                # look for subs from other letter
            """
            first try to find a valid subs, once done
            if upcomin letters in vowels add one to the answer
            keep doing until you encounter end of str or a consonant
            """
            # you have a vowel now
            check = set(list("aeiou"))
            while i < len(word) and word[i] in vowels:
                letter = word[i]
                if letter not in vowels:
                    break
                if len(check) > 0:
                    if letter in check:
                        check.remove(letter)
                if len(check) == 0:
                    ans += 1
                i += 1

            i += 1
        return ans
