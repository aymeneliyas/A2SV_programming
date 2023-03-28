class Solution:
    def __init__(self):
        self.count = 0
    def merge(self,list1,list2):
        p1 = 0
        p2 = 0
        while p1 < len(list1):
            while p2 < len(list2):
                if list1[p1] - self.diff <= list2[p2] :
                    break
                p2 += 1
            self.count += len(list2) - p2 
            p1 += 1 
        arr = []
        l = 0
        r = 0
        while l < len(list1) and r < len(list2):
            if list1[l] < list2[r]:
                arr.append(list1[l])
                l += 1
            else:
                arr.append(list2[r])
                r += 1
        
        arr.extend(list2[r:])
        arr.extend(list1[l:])
        return arr    
    def merge_sort(self,arr):
        if len(arr) == 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left,right)  
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = []
        self.diff = diff
        for i in range(len(nums1)):
            arr.append(nums1[i] - nums2[i])
        
        val = self.merge_sort(arr)
        
        return self.count