class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        arr = [0] * 26
        time = 0
        for task in tasks:
            arr[ord(task) - 65] += 1
        arr.sort()
        max_freq = arr.pop()
        max_idle = (max_freq - 1) * n
        while arr and max_idle > 0:
            max_idle -= min(max_freq - 1, arr.pop())
        max_idle = max(0, max_idle)
        return max_idle + len(tasks)
