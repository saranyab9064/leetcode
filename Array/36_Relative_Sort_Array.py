# ============================================================================
# Name        : 36_Relative_Sort_Array.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ==========================================================================
"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.



Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
"""

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # create a dict
        h ={}
        # store the count for each element in dict
        for i in range(len(arr1)):
            if arr1[i] in h:
                h[arr1[i]] += 1
            else:
                h[arr1[i]] = 1
        # create two empty lists
        arr3 = []
        temp = []
        # iterate each element in arr2
        for i in arr2:
            # iterate j for range of count for each element
            for j in range(h[i]):
                # append resp element to temp list as per count
                temp.append(i)
            # after appending to temp list , reset the count value to 0
            h[i] = 0
        # for key ,value in dict
        for k,v in h.items():
            # if count is more than 0
             if v:
        # run for loop and append the element based on count to new list
               for i in range(v):
                arr3.append(k)
        # sort the new list and merge to previous list
        arr3.sort()
        temp.extend(arr3)
        return (temp)


if __name__ == "__main__":
    test = Solution()
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    res = test.relativeSortArray(arr1, arr2)
    print(res)
