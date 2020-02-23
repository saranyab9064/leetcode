
# ============================================================================
# Name        : 29_Reverse_Words_in_a_String.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ==========================================================================
"""
Given an input string, reverse the string word by word.

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.


Follow up:

For C programmers, try to solve it in-place in O(1) extra space.

"""
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        first solution
        s = s.split(' ')
        print(s)
        list1 = []
        for i in s:
          list1.insert(0,i)
          print(list1)
        return (" ".join(list1))
        """
        # optimised one
        s = s.split()
        l = s[::-1]
        out = ' '.join(l)
        print(out)
        return out



if __name__ == "__main__":
    test = Solution()
    Input = "the sky is blue"
    res = test.reverseWords(Input)
    print(res)
