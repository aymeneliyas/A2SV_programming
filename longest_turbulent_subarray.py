class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        window = 1
        left = 0
        right = 1
        while right < len(arr):
            cond = True
            val = cmp(arr[right-1],arr[right])
            greater = True
            if val == -1:
                greater = True
            elif val == 1:
                greater = False
            if val == 0:
                left = right
            while cond and right < len(arr):
                right += 1
                if right < len(arr):    
                    if greater:
                        q = cmp(arr[right-1],arr[right])
                        if q < 1:
                            cond = False
                        greater = False
                    else:
                        q = cmp(arr[right-1],arr[right])
                        if q > -1:
                            cond = False
                        greater = True
                
            window = max(window,right-left)
            left = right - 1
        
                    
        return window
