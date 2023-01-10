class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hash1, hash2 = {}, {}
        ele_hashset = set()
        n = len(arr)
        for i in range(n):
            if arr[i] in hash1:
                hash1[arr[i]] += 1
            else:
                hash1[arr[i]] = 1
        min_freq = float("inf")
        max_freq = -float("inf")
        for ele in hash1:
            if hash1[ele] in hash2:
                hash2[hash1[ele]].append(ele)
            else:
                hash2[hash1[ele]] = [ele]
            ele_hashset.add(ele)
            min_freq = min(min_freq, hash1[ele])
            max_freq = max(max_freq, hash1[ele])
        freq = min_freq
        # print(hash1,"\n")
        # print(hash2)
        while k and ele_hashset:
            if freq > max_freq:
                break
            while freq not in hash2:
                freq += 1
            while len(hash2[freq]) == 0:
                freq += 1
            remove_ele = hash2[freq].pop()
            if len(hash2[freq]) == 0:
                freq += 1
            if hash1[remove_ele] > k:
                break
            else:
                k -= hash1[remove_ele]
                ele_hashset.remove(remove_ele)
        return len(ele_hashset)
