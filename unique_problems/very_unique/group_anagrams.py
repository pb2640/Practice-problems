class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        take w1, w2
        build a hashmap from w1, take letter l in w2, if letter in hashmap and by the end of iteration all keys are zero 
        add w2 to the temp array and remove w2 from array and w1 by then end of iterating strs
        do the same till you iterate over all words in strs
        
        Problem with above code: O(n^2k)
        
        try:
        sort the word -> returns list, convert to tuple now this tuple as a key and append the word 
        if the sorted tuple is present in hashmap
        return values of this hashmap
        '''
        ans = {}
        for word in strs:
            #sort the word
            sword = tuple(sorted(word))
            if sword in ans:
                ans[sword].append(word)
            else:
                ans[sword] = [word]
        
        
            
        return ans.values()
        # ans = []
        # for i in range(len(strs)):
        #     w1 = strs[i]
        #     # if word is marked, it has been compared with other words so skip it
        #     if w1 == 1:
        #         continue
        #     # create a hashmap to check if letters present in w1 are present in w2
        #     hashmap_orig = {}
        #     for letter in w1:
        #         if letter in hashmap_orig:
        #             hashmap_orig[letter] += 1
        #         else:
        #             hashmap_orig[letter] = 1
        #     arr = []
        #     flag = 0
        #     # iterate over rest of the words
        #     for j in range(i + 1, len(strs)):
        #         hashmap = hashmap_orig.copy()
        #         w2 = strs[j]
        #         if w2 == 1:
        #             continue
        #         for letter in w2:
        #             if letter in hashmap:
        #                 hashmap[letter] -= 1
        #             else:
        #                 # compare with other word
        #                 flag = 1
        #                 break
        #         if flag:
        #             flag = 0
        #             continue
        #         for letter in hashmap:
        #             if hashmap[letter] != 0:
        #                 flag = 1
        #                 break
        #         if flag:
        #             flag = 0
        #             continue
        #         arr.append(strs[j])
        #         strs[j] = 1
        #     arr.append(strs[i])
        #     ans.append(arr)

        # return ans
