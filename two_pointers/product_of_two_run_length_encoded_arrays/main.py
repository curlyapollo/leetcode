from typing import List


class Solution:
    def findRLEArray(self, encode1: List[List[int]], encode2: List[List[int]]) -> List[List[int]]:
        ans = []
        j = 0
        for val_i, freq_i in encode1:
            while freq_i:
                freq_cur = min(freq_i, encode2[j][1])
                val_cur = val_i * encode2[j][0]
                if ans and ans[-1][0] == val_cur:
                    ans[-1][1] += freq_cur
                else:
                    ans.append([val_cur, freq_cur])
                freq_i -= freq_cur
                encode2[j][1] -= freq_cur
                if not encode2[j][1]:
                    j += 1
        return ans