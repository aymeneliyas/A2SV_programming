class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        for idx,val in enumerate(arr):
            if idx == 0:
                arr[idx] = 1
                continue
            if val > arr[idx-1]:
                arr[idx] = arr[idx-1] + 1
        
        return max(arr)