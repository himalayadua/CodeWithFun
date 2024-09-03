# How to approach any Leetcode Problem - Part2
Here's a step-by-step approach that you can follow to solve any LeetCode problem:

1. Understand the problem: Read and understand the problem statement thoroughly. Identify the input and output requirements, constraints, and any specific edge cases mentioned.
2. Clarify doubts and ask questions: If any part of the problem statement is unclear, don't hesitate to ask questions in the LeetCode discussion forum or seek clarification from the interviewer (if you're solving the problem in an interview setting).
3. Define the problem's inputs and outputs: Clearly define the function signature or method you need to implement. Identify the input parameters and return type.
4. Formulate examples: Come up with a set of example inputs and expected outputs. Identify various scenarios, including edge cases, to ensure you have a comprehensive understanding of the problem requirements.
5. Break down the problem: Analyze the problem and break it down into smaller subproblems or steps. Identify any patterns, data structures, or algorithms that might be useful in solving the problem.
6. Design an algorithm: Based on the subproblems you identified, design a high-level algorithm or plan to solve the problem. Consider using pseudocode or simple diagrams to outline your thought process.
7. Choose appropriate data structures: Determine which data structures are suitable for the problem. This might involve using arrays, linked lists, stacks, queues, trees, graphs, hash tables, etc., depending on the problem's requirements.
8. Implement the algorithm: Start implementing the algorithm in your preferred programming language. Follow best practices, use meaningful variable names, and ensure your code is readable.
9. Test your solution: Test your code with the example inputs and expected outputs you formulated earlier. Verify that your solution produces the correct results. Consider edge cases, boundary conditions, and large inputs to validate the correctness and efficiency of your solution.
10. Analyze the time and space complexity: Analyze the time and space complexity of your solution. Consider the Big O notation to understand the efficiency of your algorithm. Optimize your solution if necessary.


## Let's consider the following problem as an example:
**Problem:** Given an array of integers, find two numbers such that they add up to a specific target value. Return the indices of the two numbers as an array.

**Example:**
```json
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: The sum of nums[0] = 2 and nums[1] = 7 is 9, so the indices [0, 1] are returned.
```

Now, let's walk through the step-by-step approach to solve this problem:

1. **Understand the problem:** We need to find two numbers in an array that add up to a specific target value. We should return the indices of these two numbers.

2. **Clarify doubts and ask questions:** No specific doubts or questions arise from the problem statement.

3. **Define the problem's inputs and outputs:** We need to implement a function with the following signature: `int[] twoSum(int[] nums, int target)`. It takes an integer array `nums` and an integer `target` as input and returns an integer array representing the indices of the two numbers.

4. **Formulate examples:** We have already provided an example in the problem statement. Let's consider a few more examples:
   - Example 1:
     ```json
     Input: nums = [3, 2, 4], target = 6
     Output: [1, 2]
     Explanation: The sum of nums[1] = 2 and nums[2] = 4 is 6, so the indices [1, 2] are returned.
     ```
   - Example 2:
     ```json
     Input: nums = [3, 3], target = 6
     Output: [0, 1]
     Explanation: The sum of nums[0] = 3 and nums[1] = 3 is 6, so the indices [0, 1] are returned.
     ```

5. **Break down the problem:** To solve this problem, we can use a hash table (also known as a dictionary in some programming languages) to store the complement of each number as we traverse the array. We iterate through the array, and for each number, we check if its complement (target minus the current number) exists in the hash table. If it does, we have found the two numbers that add up to the target. If not, we add the current number and its index to the hash table.

6. **Design an algorithm:** Here's an algorithmic plan to solve the problem:
   - Initialize an empty hash table to store the complement of each number.
   - Iterate through the array using a for loop:
     - Calculate the complement by subtracting the current number from the target.
     - Check if the complement exists in the hash table:
       - If it does, return the indices of the current number and its complement.
       - If not, add the current number and its index to the hash table.
   - If no solution is found, return an empty array.

7. **Choose appropriate data structures:** We'll use a hash table to store the complements for efficient lookup.

8. **Implement the algorithm:** Here's an implementation of the algorithm in Python:

```python
def twoSum(nums, target):
    complement_map = {}  # Hash table to store complements

    for i, num in enumerate(nums):
        complement = target - num
        if complement in complement_map:
            return [complement_map[complement], i]
        complement_map[num] = i

    return []  # No solution found
```

9. **Test your solution:** Let's test the function with the example inputs we formulated earlier:
```python
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(twoSum([3, 3], 6))          # Output: [0, 1]
```

10. **Analyze the time and space complexity:** The time complexity of this solution is O(n) since we iterate through the array once. The space complexity is also O(n) because, in the worst case, we may store all the elements in the hash table.

