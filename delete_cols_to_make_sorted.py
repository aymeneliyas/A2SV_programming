class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        row_len = len(strs[0])
        col_len = len(strs)
        ans = 0
        for row in range(row_len):
            char = ord("a")
            print(char)
            for col in range(col_len):
                if ord(strs[col][row]) >= char:
                    char = ord(strs[col][row])
                else:
                    ans += 1
                    break
        return ans
