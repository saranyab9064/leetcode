# ============================================================================
# Name        : 12_inverted_right_angle_tri_pattern.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
string = input("enter the string:")
for i in range(len(string)+1):
        print(string[0:i]*(i*1))
