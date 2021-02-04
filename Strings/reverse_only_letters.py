class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        letters = [c for c in S if c.isalpha()]
        ans = ""
        for c in S:
            if c.isalpha():
                ans = ans + (letters.pop())
            else:
                ans = ans+c
        return ans
