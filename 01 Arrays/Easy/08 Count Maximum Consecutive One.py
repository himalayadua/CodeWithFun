# Approach 1

from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt = 0
            maxi = max(maxi, cnt)
        return maxi




if __name__ == "__main__":
    nums = [1, 1, 0, 1, 1, 1]
    obj = Solution()
    ans = obj.findMaxConsecutiveOnes(nums)
    print("The maximum  consecutive 1's are", ans)


# Output: The maximum consecutive 1’s are 3.
# Time Complexity: O(N) since the solution involves only a single pass.
# Space Complexity: O(1) because no extra space is used.



# Approach 2
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, zeros = 0, 0
        for r, n in enumerate(nums):
            zeros += n == 0
            if zeros > 0:
                zeros -= nums[l] == 0
                l += 1
        
        return r - l + 1
    

# Approach 3

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, windowSize = 0, 0
        for n in nums:
            if n == 1:
                windowSize += 1
            else:
                res = max(res, windowSize)
                windowSize = 0
        res = max(res, windowSize)

        return res  