class HitCounter:

    def __init__(self):
        self.times = [0 for _ in range(300)]
        self.hits = [0 for _ in range(300)]

    def hit(self, timestamp):
        index = timestamp % 300
        if self.times[index] != timestamp:
            self.times[index] = timestamp
            self.hits[index] = 1
        else:
            self.hits += 1

    def getHits(self, timestamp):
        ans = 0
        for i in range(300):
            if timestamp - self.times[i] < 300:
                ans += self.hits[i]
        return ans


counter = HitCounter()

counter.hit(1)

counter.hit(2)

counter.hit(3)

print(counter.getHits(4))

counter.hit(300)

print(counter.getHits(300))

print(counter.getHits(301))
