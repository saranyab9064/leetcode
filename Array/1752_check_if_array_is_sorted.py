class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # find the minimum element 
        min_ele,min_index = nums[0],-1
        flag1= 1
        for i in range(1,len(nums)):
            if nums[i] < min_ele:
                min_ele = nums[i]
                min_index = i
        print(min_ele,min_index)
        # find whether the element is in ascending order from 0 to min_index
        for i in range(1,min_index):
            if nums[i] < nums[i-1]:
                flag1 = 0
                break
        flag2= 2
        # find whether the element is in asending order from min_index to len(nums)
        for i in range(min_index+1,len(nums)):
            if nums[i] < nums[i-1]:
                flag2 = 0
                break
        print(flag1,flag2)
        # if both the conditions satifies the ascending order 
        # then check the last ele < first el
        if (flag1 and flag2 and nums[len(nums)-1]<nums[i]):
              return True
        else: 
            return False
test = Solution()
arr  = [3,4,5,1,2]
out = test.check(arr)
print(out)
            
