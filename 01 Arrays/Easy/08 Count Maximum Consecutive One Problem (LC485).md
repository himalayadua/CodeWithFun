# Count Maximum Consecutive One's in the array
**Leetcode 485**
[LC485](https://leetcode.com/problems/max-consecutive-ones/description/)

## Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

### Example 1:
Input: prices = {1, 1, 0, 1, 1, 1}

Output: 3

Explanation: There are two consecutive 1’s and three consecutive 1’s in the array out of which maximum is 3.

Input: prices = {1, 0, 1, 1, 0, 1} 

Output: 2

### Explanation: There are two consecutive 1's in the array. 


# Leetcode
## 485. Max Consecutive Ones

Given a binary array `nums`, return *the maximum number of consecutive *`1`*'s in the array*.

### Example 1:
Input: nums = [1,1,0,1,1,1]

Output: 3

Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

### Example 2:
Input: nums = [1,0,1,1,0,1]

Output: 2

### Constraints:

-   `1 <= nums.length <= 105`
-   `nums[i]` is either `0` or `1`.