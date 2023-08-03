class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([el[::-1] for el in s.split()])