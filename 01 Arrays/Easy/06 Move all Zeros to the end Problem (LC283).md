# Move all Zeros to the end of the array
**Leetcode 283**
[LC283](https://leetcode.com/problems/move-zeroes/description/)


## Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.

### Example 1:
Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1

Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0

Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order

### Example 2:
Input: 1,2,0,1,0,4,0

Output: 1,2,1,4,0,0,0

Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order


# Leetcode
## 283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

### Example 1:
Input: nums = [0,1,0,3,12]

Output: [1,3,12,0,0]

### Example 2:
Input: nums = [0]

Output: [0]
 

### Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 