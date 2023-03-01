class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        output = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(prefix[i-1] * nums[i])

        for i in reversed(range(len(nums))):
            if i == len(nums)-1:
                postfix.append(nums[i])
            else:
                postfix.append(postfix[len(nums)-2-i] * nums[i])
        postfix.reverse()
        
        for i in range(len(nums)):
            if i == 0:
                output.append(postfix[i+1])
            elif i == len(nums)-1 :
                output.append(prefix[i-1])
            else:
                output.append(prefix[i-1] * postfix[i+1])
        return output