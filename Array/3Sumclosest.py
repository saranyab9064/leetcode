#============================================================================
# Name        : 3Sumclosest.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
#============================================================================
#Given array nums = [-1, 2, 1, -4], and target = 1.

#The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        print(target)
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(i+2, len(nums)):
                        a = nums[i];
                        b = nums[j];
                        c = nums[k];
                        if a+b+c == target:
                            print([a, b, c])
                            return 1



if __name__ == '__main__' :
    nums = [-1, 2, 1, -4]
    target = 2
    Sum = Solution()
    res = Sum.threeSumClosest(nums,target+1)
    print(res)
    if res!=1:
        res = Sum.threeSumClosest(nums, target-1)
