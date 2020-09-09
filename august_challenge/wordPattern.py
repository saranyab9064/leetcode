class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # declare two hash map
        hash_pattern = {}
        hash_str = {}

        split_word = str.split(' ')
        # if length of pattern is not equal to split_word return false
        if len(pattern) != len(split_word):
            return False

        # iterate the loop and store the value in hash map
        for pattern_i,str_j in zip(pattern,split_word):
            if pattern_i not in hash_pattern:
                if str_j in hash_str:
                    return False
                else:
                    hash_pattern[pattern_i] = str_j
                    hash_str[str_j] = pattern_i
            else:
                if hash_pattern[pattern_i] != str_j:
                    return False

        return True


        
