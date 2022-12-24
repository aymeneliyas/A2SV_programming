class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        stack = []
        
        first = 0
        string = str(x)
        rev_string = string[::-1]
        if string == rev_string:
            return True
        return False
