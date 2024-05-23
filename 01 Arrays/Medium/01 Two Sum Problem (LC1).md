# Two Sum : Check if a pair with given sum exists in Array
**Leetcode 1**
[LC1](https://leetcode.com/problems/two-sum/description/)

## Problem Statement: 
Given an array of integers arr[] and an integer target.

1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

> Note: You are not allowed to use the same element twice. Example: If the target is equal to 6 and num[1] = 3, then nums[1] + nums[1] = target is not a solution.


### Example 1:
Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 14

Result: YES (for 1st variant)
       [1, 3] (for 2nd variant)

Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for the first variant and [1, 3] for 2nd variant.

### Example 2:
Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 15

Result: NO (for 1st variant)
	[-1, -1] (for 2nd variant)

Explanation: There exist no such two numbers whose sum is equal to the target.



# Leetcode
## 1. Two Sum

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have *exactly* one solution, and you may not use the *same* element twice.

You can return the answer in any order.


### Example 1:
Input: nums = [2,7,11,15], target = 9

Output: [0,1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

### Example 2:
Input: nums = [3,2,4], target = 6

Output: [1,2]

### Example 3:
Input: nums = [3,3], target = 6

Output: [0,1]

### Constraints:

-   `2 <= nums.length <= 104`
-   `-109 <= nums[i] <= 109`
-   `-109 <= target <= 109`
-   Only one valid answer exists.