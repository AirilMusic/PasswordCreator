# https://leetcode.com/problems/largest-number/submissions/903449308/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=lambda x: x*9, reverse=True)
        return ''.join(nums).lstrip('0') or '0'
