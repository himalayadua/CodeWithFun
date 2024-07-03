import heapq
from typing import List

#Approach 1
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        return 0 if len(nums)<=4 else nums.sort() or min(nums[len(nums)-4+i]-nums[i] for i in range(4))
        


#Approach 2
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums_size = len(nums)
        if nums_size <= 4:
            return 0

        # Find the four smallest elements
        smallest_four = sorted(heapq.nsmallest(4, nums))

        # Find the four largest elements
        largest_four = sorted(heapq.nlargest(4, nums))

        min_diff = float("inf")
        # Four scenarios to compute the minimum difference
        for i in range(4):
            min_diff = min(min_diff, largest_four[i] - smallest_four[i])

        return min_diff