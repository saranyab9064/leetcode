"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
permutation is a rearrangement of letters. The palindrome does not need to be limited to just
dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat'; "atc o eta·; etc.)

"""
class Solution(object):
    def palindrome_permutation(self, s):
        """
        :type s: str
        :rtype: str
        """
        # declare hash table
        h = {}
        # check the no of character
        # all character should be in even count and one character can be in odd count
        s = s.replace(' ','')
        s =s.lower()
        print(s)
        for i in range(0,len(s)):
            if s[i] not in h:
                h[s[i]] = 1
            else:
                h[s[i]] += 1
        # check for char which has odd count
        odd_char_count = [i for i in h if h[i]%2 == 1]
        return  len(odd_char_count) < 2





if __name__ == "__main__":
    
    in1 = "Tact Coa"
    test = Solution()
    out1 = test.palindrome_permutation(in1)
    print(out1)
