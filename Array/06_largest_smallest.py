# ============================================================================
# Name        : 06_largest_smallest.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
def largest(arr):
    max=0
    n=0
    for i in arr:
        if max<arr[n]:
            max=arr[n]
        n+=1
    return(max)

def smallest(arr):
    min=100000
    n=0
    for i in arr:
        if min>arr[n]:
            min=arr[n]
        n += 1
    return(min)

if __name__ == '__main__':
    arr = list(map(int, input().split(' ')))
    print("arr",arr)
    largest_element= largest(arr)
    smallest_element= smallest(arr)
    print("The largest element of the array: ",largest_element)
    print("The smallest element of the array: ",smallest_element)




