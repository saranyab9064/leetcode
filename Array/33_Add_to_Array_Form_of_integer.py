
# ============================================================================
# Name        : 33_Add_to_Array_Form_of_integer.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================

"""
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.



Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
Example 4:

Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000


Note：

1 <= A.length <= 10000
0 <= A[i] <= 9
0 <= K <= 10000
If A.length > 1, then A[0] != 0
"""
class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        # convert list to str
        string_a = str(A)
        # initiate empty str
        string_b = ""
        # check each element in string_a is str and append it
        for i in string_a:
            if i.isnumeric():
                string_b +=i
        # create a temp varible and store the int val
        temp =  int(string_b)+K
        # we need to convert it back to string after adding two stings
        string_c = str(temp)
        # return type is list so we need to create an empty list
        list_1=[]
        # iterate and append it to list
        for j in range(len(string_c)):
            list_1.append(int(string_c[j]))
        return(list_1)

if __name__ == "__main__":
    test = Solution()
    a = [1, 2, 9]
    k = 806
    res = test.addToArrayForm(a,k)
    print(res)
