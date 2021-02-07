'''
We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.

Example 1:

Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: 
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.
Note:

1 <= S.length = shifts.length <= 20000
0 <= shifts[i] <= 10 ^ 9
'''

class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        '''
        res = ''
        for i in range(len(S)):
            ascii_value = ord(S[i])          
            sum_value = sum(shifts[i:])
            print(ascii_value,sum_value)
            res = res + chr(ascii_value+sum_value)
        return res
        '''
        res = ""
        sum_val = sum(shifts) % 26
        for i , ch in enumerate(S):
            index_val = ord(ch) - ord('a')
            print(index_val)
            res = res + chr(ord('a')+(index_val +sum_val)%26)
            print(index_val+sum_val)%26
            sum_val = sum_val-shifts[i] %26
            print(sum_val)
        return res


	


        
   



        


a = "abc"
list1 = [3,5,9]
test = Solution()
out =  test.shiftingLetters(a,list1)
print(out)
