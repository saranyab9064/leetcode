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
    nums1 = [1, 2]
    nums2 = [3, 4]
    median = Solution()
    median.findMedianSortedArrays(nums1, nums2)


