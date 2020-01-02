

def Rotate(arr,d,r):
    n=0
    for i in arr:
        n+=1
    if r == 'l':
      for x in range(d):
        left_rotation(arr,n)
    else:
        right_rotation(arr,n)

# ============================================================================
# Name        : rotate_arr.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
def left_rotation(arr,n):
    first_element = arr[0]
    for i in range(n - 1):
            arr[i] = arr[i + 1]
    arr[n - 1] = first_element
    print("After left_rotation")
    print(arr)

def right_rotation(arr,n):
    last_element = arr[n-1]
    i=n-1
    while(i>0):
        arr[i] = arr[i - 1]
        i=i-1
    arr[0] = last_element
    print("After right_rotation")
    print(arr)


def reverse_rotate(arr):
    n=0
    for i in arr:
        n+=1
    arr2 = [None] * len(arr);

    for i in range(0,n):
        arr2[i] = arr[n-1-i]
        print("After reverse array")
        print(arr2)


if __name__ == '__main__':
  print("Enter the array to perform rotation")
  arr = list(map(int, input().split(' ')))
  r = input("Enter l to perform left or r to perform right")
  d = int(input("By how many elements to perform right or left rotation"))
  Rotate(arr,r)
  reverse_rotate(arr)



