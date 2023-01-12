class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        ans = []
        for index in range(len(boxes)):
            add = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    add += abs(index-j)
            ans.append(add)
        return ans
