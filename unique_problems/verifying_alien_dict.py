class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {}  #         create a reference dictionary
        for i in range(len(order)):
            hashmap[order[i]] = i

        # create a windiw function to compare to words, keep doing until you exhaust all words and
        # then return true, if any vioalation occurs return false
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            flag = 0
            f = 0  # iterator for the first word
            s = 0  # iterator for the second word
            while f < len(w1) and s < len(w2):
                if hashmap[w1[f]] > hashmap[w2[s]]:
                    return False
                elif hashmap[w1[f]] == hashmap[w2[s]]:
                    f += 1
                    s += 1
                else:
                    flag = 1
                    break  # the first words letter is smaller lexographically wrt the ssecond word
            if len(w1) > len(w2) and not flag:
                return False

        return True
