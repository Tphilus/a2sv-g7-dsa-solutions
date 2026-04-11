class RecentCounter:

    def __init__(self):
        self.queue = []
        self.counts = 0

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[self.counts] < t - 3000:
            self.counts += 1
        
        return len(self.queue) - self.counts


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)