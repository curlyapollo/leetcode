class Solution(object):
    def summaryRanges(self, nums):
        ptr1 = 0
        ptr2 = 1
        if len(nums) < 2:
            return list(map(str, nums))
        ans = []
        while ptr2 < len(nums):
            if nums[ptr2 - 1] != nums[ptr2] - 1:
                if ptr1 == ptr2 - 1:
                    ans.append(str(ptr1))
                else:
                    ans.append(str(nums[ptr1]) + '->' + str(nums[ptr2 - 1]))
                ptr1 = ptr2
            ptr2 += 1
        if ptr1 == ptr2 - 1:
            ans.append(str(ptr1))
        else:
            ans.append(str(nums[ptr1]) + '->' + str(nums[ptr2 - 1]))
        return ans
