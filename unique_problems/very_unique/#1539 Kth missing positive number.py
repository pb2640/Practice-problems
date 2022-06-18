# 1539 Kth missing positive number
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        store = []
        curr_num = 1

        for i in range(len(arr)):
            next_num = arr[i]
            while curr_num < next_num:
                store.append(curr_num)
                if len(store) == k:
                    return store[-1]
                curr_num += 1

            curr_num = next_num + 1

        while len(store) != k:
            store.append(curr_num)
            curr_num += 1
        # print(store)
        return store[-1]
