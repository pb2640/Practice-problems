class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        # parse the sentence
        # if the letter is in sentence remove it from the pan set
        # if not it has already been covered
        # check len of set after every letter, if zero return true
        # clever sol

        pan = set()
        for char in sentence:
            pan.add(char)

        if len(pan) == 26:
            return True
        else:
            return False
