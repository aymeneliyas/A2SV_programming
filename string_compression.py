class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        index = 0
        i = 0
        while i < len(chars):
            j = i
            while j<len(chars) and chars[j] == chars[i]:
                j = j+1
            chars[index] = chars[i]
            index = index+1
            if j-i > 1:
                count = str(j-i)
                for x in count:
                    chars[index] = x
                    index = index+1
            i = j
