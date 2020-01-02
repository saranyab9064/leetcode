# ============================================================================
# Name        : twosum.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
def twosum():
 nums = [4,5,6,7,0,1,2]
 target = 5
 n=len(nums)
 b= range(0,n)

 for i in nums:
    if nums == target:
        a=i
        i=i+1
        return a
    else:
        return -1

if __name__ == '__main__':
    index=twosum()
    print(index)
