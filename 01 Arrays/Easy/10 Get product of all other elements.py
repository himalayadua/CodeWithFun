# Solution 1
def product_except_self(nums):
    total_product = 1
    for num in nums:
        total_product *= num
    
    result = []
    for num in nums:
        result.append(total_product // num)
    
    return result

# Example usage
nums = [1, 2, 3, 4, 5]
print(product_except_self(nums))  # Output: [120, 60, 40, 30, 24]



# Solution 2
def product_except_self(nums):
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]
    
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]
    
    result = []
    for i in range(n):
        result.append(left_products[i] * right_products[i])
    
    return result

# Example usage
nums = [1, 2, 3, 4, 5]
print(product_except_self(nums))  # Output: [120, 60, 40, 30, 24]
