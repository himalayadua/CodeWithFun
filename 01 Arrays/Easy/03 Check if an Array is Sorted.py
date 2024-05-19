### **Approach**: Brute Force
from typing import List


def isSorted(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return False

    return True

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    ans = isSorted(arr, n)
    if ans:
        print("True")
    else:
        print("False")


#Output: True

#Time Complexity: O(N^2)
#Space Complexity: O(1)


#####################################################
### **Approach**: Efficient (Single traversal)

def isSorted(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = 5
    print("True" if isSorted(arr, n) else "False")


#Output: True

#Time Complexity: O(N)
#Space Complexity: O(1)


######################################################
# Leetcode 1752. Check if Array Is Sorted and Rotated

# Additional Condition: 
# An array A rotated by x positions results in an array B of the same length 
# such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

# Example 1:

#Input: nums = [3,4,5,1,2]
#Output: true
#Explanation: [1,2,3,4,5] is the original sorted array.
#You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].



class Solution:
    def check(self, nums: List[int]) -> bool:
        op = 0
        l = len(nums)
        for i in range(l):
            if nums[(i+1)%l] >= nums[i]: 
                pass
            else:
                op += 1
                if op > 1:
                    return False
        else:
            return True
            
        

# Faster Approach
class Solution:
    def check(self, nums: List[int]) -> bool:

        l = sorted(nums) 

        for i in range(len(nums)) :

            x = nums[0] 

            nums.remove(x) 
            nums.append(x) 

            if nums == l :
                return True 

        return False 
        
