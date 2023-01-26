class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        for i in range(size):
            ch = str(nums[i])
            j = len(ch)-1
            tmp = ""
            while ch[j] == "0":
                    j = j-1
            
            while j >= 0:
                tmp += ch[j]
                j -= 1
            
            nums.append(int(tmp))
        ans = set(nums)
        
        return len(ans)
