class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
       
        ans = [] 
        string = "" 
        blocked = False
        for code in source:
            index = 0
            while index < len(code):
                if code[index] == '/' and index + 1 < len(code) and code[index+1] == "/" and not blocked:
                    index = len(code)
                elif code[index] == "/" and index + 1 < len(code) and code[index+1] == "*" and not blocked:
                    blocked = True
                    index += 2
                elif code[index] == "*" and index + 1 < len(code) and code[index+1] == "/" and blocked:
                    blocked = False
                    index += 2
                elif blocked:
                    index += 1
                else:
                    string += code[index]
                    index  += 1
            if not blocked and string:
                ans.append(string)
                string = ""
        return ans
