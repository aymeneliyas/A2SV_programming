class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP == "":
            return "Neither"
        if "." in queryIP:
            arr = queryIP.split(".")
            if len(arr) != 4:
                return "Neither"
            
            for i in queryIP:
                if not i.isdigit() and i != ".":
                    return "Neither"
            for i in arr:
                
                if i == "" or int(i) < 0 or int(i) > 255:
                    return "Neither"
                if len(i) > 1 and i[0] == "0":
                    return "Neither"
                
            return "IPv4"
        if ":" in queryIP:
            arr = queryIP.split(":")
            if len(arr) != 8:
                return "Neither"
            for i in arr:
                if len(i) > 4 or i == "":
                    return "Neither"
            for i in queryIP:
                if not i.isdigit() and i != ":":
                    if (i not in "abcdef" and i not in "ABCDEF"):
                        return "Neither"
            return "IPv6"