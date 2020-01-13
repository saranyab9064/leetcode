#============================================================================
# Name        : 03_string_to_int.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
#===========================================================================
"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number,
 which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number,
 or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within
the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values,
 INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:

Input: "42"
Output: 42

Example 2:

Input: "-42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Therefore INT_MIN (−231) is returned.
"""
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        min_a, max_b = -2147483647, 2147483647
        str = str.strip(" ")
        if not str:
            return 0
        sign = ""
        if str[0] == "-":
            sign = "-"
            str = str[1:len(str)]
        elif str[0] == "+":
            str = str[1:len(str)]
        if  not str or not str[0].isnumeric():
            return 0
        res = ""
        for i in str:
            if i.isnumeric():
                res += i
                continue
            break
        res = int(sign + res)
        res = max(res , min_a)
        res = min(res, max_b)
        return res




class Solution1(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        b = str.strip( " ")
        print(b)

        if b[0].isnumeric():
          for i in range(0,len(b)):
            min = -2147483647
            max = 2147483647
            print(b[i])
            if b[i].isnumeric():
                 print(int(b[i]))
                 a = int(b[i])
                 if a in range(min,max):
                  return a
                 elif a>min:
                   return min

        elif b[0].isalpha():
            return 0



if __name__ == "__main__" :
        string = Solution()
        a = string.myAtoi(str = "  214")
        print(a)
