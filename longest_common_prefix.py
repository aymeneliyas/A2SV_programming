class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for i in range(1,len(strs)):
            ans = ""
            for j in range(0,len(prefix)):
                if j < len(strs[i]) and prefix[j] == strs[i][j]:
                    ans += strs[i][j]
                else:
                    break
            prefix = ans  
                # if prefix[j] == strs[i][j]:
                #     ans += strs[i][j]
                # prefix = ans
        return prefix
