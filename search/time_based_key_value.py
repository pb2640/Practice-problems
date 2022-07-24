class TimeMap:
    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp in self.hashmap:
            if key in self.hashmap[timestamp]:
                self.hashmap[timestamp][key].append(value)
            else:
                self.hashmap[timestamp][key] = []
        else:
            self.hashmap[timestamp] = {}
            self.hashmap[timestamp][key] = [value]

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        # print(self.hashmap)
        for i in range(timestamp, -1, -1):
            if i in self.hashmap:
                if key in self.hashmap[i]:
                    return self.hashmap[i][key][-1]
        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
