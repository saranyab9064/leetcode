# ============================================================================
# Name        : 05_fibonacci.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(0, n):
            c = a + b
            a = b
            b = c
        return b

    # Driver Program


print(fibonacci(0))


def printFibonacciNumbers(n):
    first_element = 0
    second_element = 1
    if (n < 1):
        return
    for x in range(0, n):
        print(second_element, end=" ")
        next = first_element + second_element
        first_element = second_element
        second_element = next


# Driven code
printFibonacciNumbers(3)
