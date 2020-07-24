"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""


class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        h = {}
        list1 = []
        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]] = 1
                list1.append(nums[i])

            else:
                h[nums[i]] += 1
                list1.remove(nums[i])

        return (list1)



if __name__ == "__main__":
    test = Solution()
    arr = [1,2,1,3,2,5]
    out = test.singleNumber(arr)
    print(out)
