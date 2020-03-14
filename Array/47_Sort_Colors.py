
# ============================================================================
# Name        : 47_Sort_Colors.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ==========================================================================
"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # initialise red ,white as zero and blue as last element in array
        red = 0
        white = 0
        blue = len(nums) - 1

        while white <= blue:

            current_ele = nums[white]
            # check is curr is 0, then  swap the red and white element & incr both
            if current_ele == 0:
                nums[white] = nums[red]
                nums[red] = nums[white]
                nums[red] = 0
                red = red + 1
                white = white + 1
            # if curr ele is 1 then simply incr white
            elif current_ele == 1:
                white = white + 1
            # if curr ele is 2 then assign the value and decr the blue
            else:
                nums[white] = nums[blue]
                nums[blue] = 2
                blue = blue - 1
        print(nums)       





if __name__ == '__main__':
    n = [2,0,2,1,1,0]
    test = Solution()
    test.sortColors(n)
