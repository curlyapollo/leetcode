class Solution:
    # def simplifyPath(self, path: str) -> str:
    #     return __import__('os').path.abspath(path) -- смешное

    def simplifyPath(self, path: str) -> str:
        stack = []
        for el in path.split('/'):
            if el not in "..":
                stack.append(el)
            elif el == "..":
                if stack:
                    stack.pop()
        return "/" + '/'.join(stack)