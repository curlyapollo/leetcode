import random


class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        last = self.data[-1]
        ind = self.dict[val]
        self.dict[last] = ind
        self.data[ind] = last
        self.data.pop()
        self.dict.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()