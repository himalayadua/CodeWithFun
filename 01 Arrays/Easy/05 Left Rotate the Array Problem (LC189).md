# Left Rotate the Array by One
**Leetcode 189**
[LC189](https://leetcode.com/problems/rotate-array/description/)

## Problem Statement: Given an array of N integers, left rotate the array by one place.

### Example 1:
Input: N = 5, array[] = {1,2,3,4,5}

Output: 2,3,4,5,1

Explanation:
Since all the elements in array will be shifted
toward left by one so '2' will now become the
first index and and '1' which was present at
first index will be shifted at last.

### Example 2:
Input: N = 1, array[] = {3}

Output: 3

Explanation: Here only element is present and so
the element at first index will be shifted to
last index which is also by the way the first index.


# Leetcode
## 189. Rotate Array
Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

### Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3

Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

### Example 2:
Input: nums = [-1,-100,3,99], k = 2

Output: [3,99,-1,-100]

Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:

-   `1 <= nums.length <= 105`
-   `-231 <= nums[i] <= 231 - 1`
-   `0 <= k <= 105`
