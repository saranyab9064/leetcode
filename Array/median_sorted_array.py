"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums = sorted(nums)
        print(nums)
        length = len(nums)
        if (length % 2) == 0:
            length = length / 2
            median = (nums[int(length)] + nums[int(length - 1)]) / 2
            print(median)
            return median
        else:
            length = length / 2
            median = nums[int(length)]
            print(median)
            return median


if __name__ == '__main__':
    nums1 = [1,8]
    nums2 = [3, 4]
    median = Solution()
    median.findMedianSortedArrays(nums1, nums2)


