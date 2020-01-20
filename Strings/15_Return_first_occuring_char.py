# ============================================================================
# Name        : 15_Return_first_occurring_char.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================


def first_recurring_char(string):
  count = {}
  for char in string:
      if char in count:
          return char
      else:
          count[char] = 1
  return None


if __name__ == '__main__':
    string = 'ABCDABCD'
    res = first_recurring_char(string)
    print(res)