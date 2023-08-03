class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """

    def __init__(self, v1, v2):
        self.cur = 0
        self.list = []
        for i in range(min(len(v1), len(v2))):
            self.list.append(v1[i])
            self.list.append(v2[i])
        if len(v1) < len(v2):
            for i in range(len(v1), len(v2)):
                self.list.append(v2[i])
        else:
            for i in range(len(v2), len(v1)):
                self.list.append(v1[i])

    """
    @return: An integer
    """

    def _next(self):
        ans = self.list[self.cur]
        self.cur += 1
        return ans

    """
    @return: True if has next
    """

    def hasNext(self):
        return self.cur < len(self.list)


zi = ZigzagIterator([1, 2], [3, 4, 5, 6])
while zi.hasNext():
    print(zi._next())