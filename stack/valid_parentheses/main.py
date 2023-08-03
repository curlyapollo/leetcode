class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for el in s:
            if el == '(' or el == '[' or el == '{':
                stack.append(el)
            else:
                if len(stack) == 0:
                    return False
                if el == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                if el == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                if el == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0