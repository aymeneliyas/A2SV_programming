class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        comm_len = len(command)
        ans = ""
        for i in range(comm_len):
            if command[i] == "G":
                ans += "G"
            elif command[i] == "(" and command[i+1] == ")":
                ans += "o"
            elif command[i] == "(" and command[i+1] == "a":
                ans += "al"
        return ans
