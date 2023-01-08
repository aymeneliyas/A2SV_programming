class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for num in nums:
            if num % 2 == 0:
                even_sum += num
        
        ans = []
        for query in queries:
            res =0 
            prev = nums[query[1]]
            nums[query[1]] = nums[query[1]] + query[0]
            
            if prev % 2 == 0:
                if nums[query[1]] % 2 == 0:
                    res = (even_sum - prev) + nums[query[1]]

                else:
                    res = even_sum - prev
            else:
                if nums[query[1]] % 2 == 0:
                    res = even_sum + nums[query[1]]

                else:
                    res = even_sum
            even_sum = res
            ans.append(res)           
        return ans
