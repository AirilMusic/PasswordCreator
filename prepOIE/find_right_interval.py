# https://leetcode.com/problems/find-right-interval/description/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        pos = [-1] * n
        
        start_index = {}
        for i in range(n):
            start_index[intervals[i][0]] = i
        
        sorted_starts = sorted(start_index.keys())
        
        for i in range(n):
            end = intervals[i][1]
            index = bisect_left(sorted_starts, end)
            if index != len(sorted_starts):
                pos[i] = start_index[sorted_starts[index]]
        
        return pos
