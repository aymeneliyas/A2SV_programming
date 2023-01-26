class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        maximum = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            cur = arr[i]
            arr[i] = maximum
            if cur>maximum:
                maximum = cur
        return arr
