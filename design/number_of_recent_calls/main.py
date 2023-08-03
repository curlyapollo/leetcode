class RecentCounter:

    def __init__(self):
        self.calls = []

    def ping(self, t: int) -> int:
        count = 0
        self.calls.append(t)
        i = len(self.calls) - 1
        while i >= 0 and self.calls[i] + 3000 >= t:
            i -= 1
            count += 1
        self.calls = self.calls[i + 1:]
        return count
