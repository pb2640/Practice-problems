class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        hashmap = {}
        min_rounds = 0
        for task in tasks:
            if task in hashmap:
                hashmap[task] += 1
            else:
                hashmap[task] = 1

        for task in hashmap:
            # print(task)
            if hashmap[task] == 1:
                return -1
            else:
                n = hashmap[task]
                if n % 3 == 0:
                    min_rounds += n // 3
                elif n == 4:
                    min_rounds += n // 2
                else:
                    temp = (n - 2) // 3
                    min_rounds += temp
                    n = n - temp * 3
                    min_rounds += n // 2
        return min_rounds
