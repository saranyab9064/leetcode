"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false

"""
class Solution(object):
    def one_insert(self,s1,s2):
        index1 = 0
        index2 = 0
        for i in range(0,len(s1))
            print(index1,index2)
            if s1[index1] == s2[index2]:
                print(s1[index1])
                if index1 == index2:
                    flag = True
                index2 = index2+1
            else:
                    index1 = index1 +1
                    index2 = index2 +1
        if not flag:
            return False 
    def one_edit(self,s1,s2):
        count = 0
        for i in range(0,len(s1)):
            if s1[i] != s2[i]:
                count = count + 1
        return count <= 1
    def one_way(self, s1,s2):
        """
        :type s1,s2: str
        :rtype: str
        """
        if len(s1) == len(s2):
            res = self.one_edit(s1,s2)
        elif len(s1)-1 == len(s2):
            res = self.one_insert(s1,s2)
        return res






if __name__ == "__main__":
    
    in1 = "pales"
    in2 = "pale"
    test = Solution()
    out1 = test.one_way(in1,in2)
    print(out1)
