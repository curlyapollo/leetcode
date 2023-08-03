import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for el in tokens:
            if el == '*':
                fst, sec = stack.pop(), stack.pop()
                stack.append(fst * sec)
            elif el == '/':
                sec, fst = stack.pop(), stack.pop()
                stack.append(math.trunc(fst / sec))
            elif el == '+':
                sec, fst = stack.pop(), stack.pop()
                stack.append(fst + sec)
            elif el == '-':
                sec, fst = stack.pop(), stack.pop()
                stack.append(fst - sec)
            else:
                stack.append(int(el))
        return stack[0]

print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))