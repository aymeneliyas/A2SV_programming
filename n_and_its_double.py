class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for key,elm in enumerate(arr):
            for j in range(len(arr)):
                if elm == 2*arr[j] and key != j:
                    print(elm , arr[j])
                    return True
                

        return False
