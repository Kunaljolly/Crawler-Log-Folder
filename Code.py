class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c = 0
        for x in logs:
            print(c)
            
            if x == "../" and c != 0:
                c -= 1
            elif x == "./":
                continue
            elif x != "./" and x != "../":
                c += 1
        return c
        
