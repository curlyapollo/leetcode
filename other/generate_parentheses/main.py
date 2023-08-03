from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        runningStack = []
        validParentheses = []

        def backtrack(openBracketCount, closeBracketCount):
            if openBracketCount == closeBracketCount == n:
                validParentheses.append("".join(runningStack))
                return

            if openBracketCount < n:
                runningStack.append("(")
                backtrack(openBracketCount + 1, closeBracketCount)
                runningStack.pop()

            if closeBracketCount < openBracketCount:
                runningStack.append(")")
                backtrack(openBracketCount, closeBracketCount + 1)
                runningStack.pop()

        backtrack(0, 0)
        return validParentheses

s = Solution()
print(s.generateParenthesis(3))