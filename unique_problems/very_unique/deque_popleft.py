class HitCounter:
    def __init__(self):
        self.deque = collections.deque()

    def hit(self, timestamp: int) -> None:
        self.deque.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.deque and (timestamp - self.deque[0]) >= 300:
            self.deque.popleft()
        return len(self.deque)
