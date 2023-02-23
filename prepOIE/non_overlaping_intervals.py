# https://leetcode.com/problems/non-overlapping-intervals/submissions/903441350/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        c = 0
        t = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < t[1]:
                c += 1
                t[1] = min(t[1], intervals[i][1])
            else:
                t = intervals[i]
        return(c)
