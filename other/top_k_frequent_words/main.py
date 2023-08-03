from typing import List
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict1 = {}
        for el in words:
            if el in dict1:
                dict1[el] += 1
            else:
                dict1[el] = 1
        srt = sorted(dict1, key=lambda x: [-dict1[x], x])
        return srt[:k]

    #using heap
    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        dict1 = {}
        ans = []
        for el in words:
            if el in dict1:
                dict1[el] += 1
            else:
                dict1[el] = 1
        maxheap = []
        for el in dict1:
            heapq.heappush(maxheap, [-dict1[el], el])
        for i in range(k):
            ans.append(heapq.heappop(maxheap)[1])
        return ans