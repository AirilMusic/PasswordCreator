# https://leetcode.com/problems/arranging-coins/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        tr = 0
        tr0 = 0
        t = 0
        n2 = n
        while n2 > 0:
            t += 1
            n2 -= t
            tr0 += 1
        print(t)
        if n  == (t * (t + 1))/2:
            return(tr0)
        else:        
            for i in range(t):
                n -= i+1
                if n > 0:
                    tr += 1
                else:
                    break
            return(tr)
