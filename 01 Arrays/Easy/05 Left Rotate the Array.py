# Solution 1: Brute force Approach

from typing import List


def solve(arr, n):
    temp = [0] * n
    for i in range(1, n):
        temp[i - 1] = arr[i]
    temp[n - 1] = arr[0]
    for i in range(n):
        print(temp[i], end=" ")
    print()

n = 5
arr = [1, 2, 3, 4, 5]
solve(arr, n)

# Time Complexity: O(n), as we iterate through the array only once.
# Space Complexity: O(n) as we are using another array of size, same as the given array.


# Solution 2:

def solve(arr, n):
    temp = arr[0]  # storing the first element of the array in a variable
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp  # assign the value of the variable at the last index
    for i in range(n):
        print(arr[i], end=" ")

n = 5
arr = [1, 2, 3, 4, 5]
solve(arr, n)

# Time Complexity: O(n), as we iterate through the array only once.
# Space Complexity: O(1) as no extra space is used



# Solution 3:

class Solution:
    def reverse(self, nums: List[int], i: int, j: int) -> None:
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        #self.reverse(nums, n - k, n - 1)
        #self.reverse(nums, 0, n - k - 1)
        #self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, n - 1)    # Reverse the entire array
        self.reverse(nums, 0, k - 1)    # Reverse the first k elements
        self.reverse(nums, k, n - 1)    # Reverse the remaining elements
