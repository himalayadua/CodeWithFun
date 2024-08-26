# Sort an array of 0s, 1s and 2s
**Leetcode 75**
[LC75](https://leetcode.com/problems/sort-colors/description/)

## Problem Statement: 
Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)

### Examples
Input:
 nums = [2,0,2,1,1,0]
 
Output
: [0,0,1,1,2,2]

Input:
 nums = [2,0,1]

Output:
 [0,1,2]

Input:
 nums = [0]

Output:
 [0]


 # Leetcode
 ## 75. Sort Colors

 Given an array `nums` with `n` objects colored red, white, or blue, sort them [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

### Example 1:
Input: nums = [2,0,2,1,1,0]

Output: [0,0,1,1,2,2]

### Example 2:
Input: nums = [2,0,1]

Output: [0,1,2]

### Constraints:

-   `n == nums.length`
-   `1 <= n <= 300`
-   `nums[i]` is either `0`, `1`, or `2`.