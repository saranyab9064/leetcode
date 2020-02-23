

# ============================================================================
# Name        : 28_Defanging_an_IP_Address.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".



Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"


Constraints:

The given address is a valid IPv4 address.
"""


class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        IP = ""
        for i in address:
            if i is ".":
                IP += "[.]"
            else:
                IP += i
        return(IP)

if __name__ == "__main__":
    test = Solution()
    address = "1.1.1.1"
    res = test.defangIPaddr(address)
    print(res)
