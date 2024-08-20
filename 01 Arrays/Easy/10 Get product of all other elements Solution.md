# Solution 1
Division
- calculate the product of all elements in the array.
- for each element in the array
    - divide the total product by the element at that index to get the product of all other elements.

# Solution 2
What if you can't use division
1.  Create two arrays, `left_products` and `right_products`.
2.  `left_products[i]` will contain the product of all elements to the left of `i`.
3.  `right_products[i]` will contain the product of all elements to the right of `i`.
4.  The result at index `i` will be the product of `left_products[i]` and `right_products[i]`.

## Example:
Input: [1, 2, 3, 4, 5]

Left Products: [1, 1, 2, 6, 24]

Right Products: [120, 60, 20, 5, 1]

Output: [1 * 120, 1 * 60, 2 * 20, 6 * 5, 24 * 1] = [120, 60, 40, 30, 24]

## Step by step
Let's run through the code step-by-step with an example input to see the output at each print statement.

### Example Input
```python
nums = [1, 2, 3, 4, 5]
```

### Code Execution and Output

1. **Initialization:**
   ```python
   n = 5
   left_products = [1, 1, 1, 1, 1]
   right_products = [1, 1, 1, 1, 1]
   ```

2. **First Loop (Calculating `left_products`):**
   - **Iteration 1 (i=1):**
     ```python
     left_products[1] = left_products[0] * nums[0] = 1 * 1 = 1
     print(left_products)  # Output: [1, 1, 1, 1, 1]
     ```
   - **Iteration 2 (i=2):**
     ```python
     left_products[2] = left_products[1] * nums[1] = 1 * 2 = 2
     print(left_products)  # Output: [1, 1, 2, 1, 1]
     ```
   - **Iteration 3 (i=3):**
     ```python
     left_products[3] = left_products[2] * nums[2] = 2 * 3 = 6
     print(left_products)  # Output: [1, 1, 2, 6, 1]
     ```
   - **Iteration 4 (i=4):**
     ```python
     left_products[4] = left_products[3] * nums[3] = 6 * 4 = 24
     print(left_products)  # Output: [1, 1, 2, 6, 24]
     ```

3. **Second Loop (Calculating `right_products`):**
   - **Iteration 1 (i=3):**
     ```python
     right_products[3] = right_products[4] * nums[4] = 1 * 5 = 5
     print(left_products)  # Output: [1, 1, 2, 6, 24]
     ```
   - **Iteration 2 (i=2):**
     ```python
     right_products[2] = right_products[3] * nums[3] = 5 * 4 = 20
     print(left_products)  # Output: [1, 1, 2, 6, 24]
     ```
   - **Iteration 3 (i=1):**
     ```python
     right_products[1] = right_products[2] * nums[2] = 20 * 3 = 60
     print(left_products)  # Output: [1, 1, 2, 6, 24]
     ```
   - **Iteration 4 (i=0):**
     ```python
     right_products[0] = right_products[1] * nums[1] = 60 * 2 = 120
     print(left_products)  # Output: [1, 1, 2, 6, 24]
     ```

4. **Third Loop (Calculating `result`):**
   - **Iteration 1 (i=0):**
     ```python
     result.append(left_products[0] * right_products[0]) = 1 * 120 = 120
     print(result)  # Output: [120]
     ```
   - **Iteration 2 (i=1):**
     ```python
     result.append(left_products[1] * right_products[1]) = 1 * 60 = 60
     print(result)  # Output: [120, 60]
     ```
   - **Iteration 3 (i=2):**
     ```python
     result.append(left_products[2] * right_products[2]) = 2 * 20 = 40
     print(result)  # Output: [120, 60, 40]
     ```
   - **Iteration 4 (i=3):**
     ```python
     result.append(left_products[3] * right_products[3]) = 6 * 5 = 30
     print(result)  # Output: [120, 60, 40, 30]
     ```
   - **Iteration 5 (i=4):**
     ```python
     result.append(left_products[4] * right_products[4]) = 24 * 1 = 24
     print(result)  # Output: [120, 60, 40, 30, 24]
     ```

### Final Output
```python
[120, 60, 40, 30, 24]
```
