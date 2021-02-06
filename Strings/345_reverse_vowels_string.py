'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_list = list(s)
        # intialise two pointers p and q
        p = 0
        q = len(s) - 1
        vowels = [ 'a','e','i','o','u','A','E','I','O','U']

        while p < q:
            print(p,q)
            if str_list[p] not in  vowels:
                p = p + 1
            elif str_list[q] not in vowels:
                q = q - 1
            else:
                str_list[p],str_list[q] = str_list[q],str_list[p]
                p = p + 1
                q = q - 1
        return "".join(str_list)


        

test = Solution()
str1 = "hello"
out = test.reverseVowels(str1)
