class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = []
        opens = ["[","{","("]
        closes = ["}",")","]"]
        openClose = {
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }
        
        for el in s:
          if el in opens:
            arr.append(el)
          elif len(arr) > 0:
            lastOpen = arr.pop();
            if openClose[lastOpen] != el:
                return False;
          else:
            return False;
        return len(arr) == 0;