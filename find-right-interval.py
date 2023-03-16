class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        s = {}
        for key,interval in enumerate(intervals):
            s[key] = interval[0]
        
        arr , ans = [] , []
        for key,i in enumerate(intervals):
            arr.append([i[0], key])
        
        arr.sort()
        for interval in intervals:
            left = 0
            right = len(arr)-1

            start , end = interval
            while left < right:
                middle = left + (right - left) // 2

                if arr[middle][0] < end:
                    left = middle + 1
                else:
                    right = middle

            if end > arr[len(arr)-1][0]:
                ans.append(-1)
            else:
                ans.append(arr[right][1])
        return ans