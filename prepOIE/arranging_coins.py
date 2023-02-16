# https://leetcode.com/problems/arranging-coins/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        tr = 0
        t = 0
        n2 = n
        while n2 > 0:
            t += 1
            n2 -= t
        
        while t > 0 and n > 0:
            n -= t
            t -= 1
            tr += 1
        
        return(tr)
