from typing import List

# идея: идем по префиксным суммам и сохраняем в словарь остатки сумм, если остаток уже есть в словаре,
# то при вычете этих сумм, будет делиться, соответственно, если между ними расстояния 2 или больше, то подходит
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pref = 0
        remainders = {0: -1}
        for i in range(len(nums)):
            pref += nums[i]
            if pref % k in remainders:
                if i - remainders[pref % k] >= 2:
                    return True
            # если уже есть, то оставляем самый старый, чтобы если что был подлиннее массив
            else:
                remainders[pref % k] = i

        return False


print(Solution().checkSubarraySum([5,0,0,0], 3))