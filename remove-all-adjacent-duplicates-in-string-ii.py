class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        arr = []
        for chr in s:
            if arr and arr[-1][0] == chr:
                arr[-1][1] += 1
                if arr[-1][1] == k:
                    arr.pop()
            else:
                arr.append([chr,1])

        res = ""
        for ch, count in arr:
            res += ch * count

        return res