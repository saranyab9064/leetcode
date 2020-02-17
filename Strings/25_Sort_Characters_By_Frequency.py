
# ============================================================================
# Name        : 25_Sort_Characters_By_Frequency.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================

"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # create an empty dictionary
        h = {}
        #  iterate each element with their count and store each element,count in dict
        for i in range(0,len(s)):
            if s[i] in h:
                h[s[i]] += 1
            else:
                h[s[i]] = 1
        print(h)
        # create an empty string
        output = ""
        # create a new dict and list all the values in descending order
        # for ascending order set reverse as False
        newDict = sorted(h.items(), key=lambda kv: kv[1], reverse=True)
        print(newDict)
        # iterate key and value in newDict
        for k, v in newDict:
            # iterate i based on value of the character eg if v for i is 2 then i will be 0,1
            # Likewise generate i range for all the values in the newDict

            for i in range(v):
                print(i,k)
                # append each value to string
                output += k
        return (output)



if __name__ == "__main__":
    test = Solution()
    s = "trree"
    res = test.frequencySort(s)
    print(res)
