
# ============================================================================
# Name        : 43_Reduce_Array_Size_to_half.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.



Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.
Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.
Example 3:

Input: arr = [1,9]
Output: 1
Example 4:

Input: arr = [1000,1000,3,7]
Output: 1
Example 5:

Input: arr = [1,2,3,4,5,6,7,8,9,10]
Output: 5


Constraints:

1 <= arr.length <= 10^5
arr.length is even.
1 <= arr[i] <= 10^5
"""

class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # create a empty dict
        h = {}
        # run for loop and store the count in dict
        for i in range(0,len(arr)):
            if arr[i] in h:
                h[arr[i]] += 1
            else:
                h[arr[i]] = 1
        # create a empty list
        arr2 =[]
        # iterate k and value in dict and store all the values in created list
        for k,value in h.items():
            arr2.append(value)
            # arrange in descending order
        arr2.sort(reverse=True)
        # inititate sum and count as zero
        sum = 0
        count = 0
        # check if sum of values in list >=length/2 and incr the count
        for i in arr2:
            sum += i
            count = count+1
            if sum >=len(arr)//2:
                  break

        return(count)









if __name__ == "__main__":
    test = Solution()
    arr = [9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]
    res = test.minSetSize(arr)
    print(res)
