#Approach 1:
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

#Time complexity: O(n^2) 
#For each element, we try to find its complement by looping through the rest of the array which takes O(n)O(n)O(n) time. Therefore, the time complexity is O(n2).

#Space complexity: O(1).
#The space required does not depend on the size of the input array, so only constant space is used.                



#Approach 2:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hash table to store value and index
        number_map = {}

        #store each element and index in the hash table
        for i in range(len(nums)):
            number_map[nums[i]] = i

        #check if the complement of each element exists in the hash table
        for i in range(len(nums)):
            complement = target - nums[i]

            #if it does -> that's our answer
            if complement in number_map and number_map[complement] != i:
                return [i, number_map[complement]]

#Time complexity: O(n).
#We traverse the list containing nnn elements exactly twice. Since the hash table reduces the lookup time to O(1), the overall time complexity is O(n).

#Space complexity: O(n).
#The extra space required depends on the number of items stored in the hash table, which stores exactly n elements.


#Approach 3:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

#Time complexity: O(n).
#We traverse the list containing nnn elements only once. Each lookup in the table costs only O(1) time.

#Space complexity: O(n).
#The extra space required depends on the number of items stored in the hash table, which stores at most n elements.


