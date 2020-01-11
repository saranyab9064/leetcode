# ============================================================================
# Name        : 12_twosum.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
def twosum():
 nums = [4,5,6,7,0,1,2]
 target = 5

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                     return([i,j])
        else:
            return -1

if __name__ == '__main__':
    index=twosum()
    print(index)
