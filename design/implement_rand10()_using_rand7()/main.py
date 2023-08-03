# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        v1 = rand7()
        v2 = rand7()
        while v1 > 5:
            v1 = rand7()
        while v2 == 7:
            v2 = rand7()
        return v1 if v2 < 4 else v1 + 5