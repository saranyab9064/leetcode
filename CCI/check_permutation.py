class Solution(object):
    def check_permutation(self, s1,s2):
        """
        :type s1, s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        else:
            s1 = sorted(s1)
            s2 = sorted(s2)
            if s1 == s2:
                return True
            else:
                return False
    def check_permutation1(self,s1,s2):
        #max chars is 256
        no_of_chars = 256
        if len(s1) != len(s2):
            return False
        # initialise count1 and count 2 with max chars of array
        count1 = [0]*no_of_chars
        count2 = [0]*no_of_chars
        # run the loop for s1 and incr the value for the respective ascii value - chars
        for i in s1:
            count1[ord(i)] += 1
        print(count1)
        for i in s2:
            count2[ord(i)] += 1

        print(count2)
        # iterate each value in count 1 and 2 , compare and return respective value
        for i in range(0,no_of_chars):
            if count1[i] != count2[i]:
                return False
        return True
            
                    
 
    
        

if __name__ == "__main__":
    
    in1 = "godd"
    in2 = "dogi"
    test = Solution()
    out1 = test.check_permutation(in1,in2)
    out2 = test.check_permutation1(in1,in2)
    print(out1,out2)