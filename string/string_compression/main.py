class Solution:
    def compress(self, chars) -> int:
        ans = [chars[0]]
        cnt = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                cnt += 1
            else:
                if cnt > 1:
                    for el in str(cnt):
                        ans.append(el)
                cnt = 1
                ans.append(chars[i])
        if cnt > 1:
            for el in str(cnt):
                ans.append(el)
        chars.clear()
        for i in range(len(ans)):
            chars.append(str(ans[i]))
        return len(chars)

chars = ["a","a","b","b","c","c","c"]
c = Solution()
print(chars[:c.compress(chars)])