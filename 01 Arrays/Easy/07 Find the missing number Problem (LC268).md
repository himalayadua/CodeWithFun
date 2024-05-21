# Find the missing number in an array
**Leetcode 268**
[LC268](https://leetcode.com/problems/missing-number/description/)

## Problem Statement: 
Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array.

### Example 1:
Input Format: N = 5, array[] = {1,2,4,5}

Result: 3

Explanation: In the given array, number 3 is missing. So, 3 is the answer.

### Example 2:
Input Format: N = 3, array[] = {1,3}

Result: 2

Explanation: In the given array, number 2 is missing. So, 2 is the answer.


# Leetcode
## 268. Missing Number

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return *the only number in the range that is missing from the array.*

### Example 1:
Input: nums = [3,0,1]

Output: 2

Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

### Example 2:
Input: nums = [0,1]

Output: 2

Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.


### Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

### Constraints:

-   `n == nums.length`
-   `1 <= n <= 104`
-   `0 <= nums[i] <= n`
-   All the numbers of `nums` are unique.