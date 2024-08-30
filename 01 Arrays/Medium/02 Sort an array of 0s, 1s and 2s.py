#Approach 1:
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [nums.count(num) for num in range(3)]
        index = 0
        for num, count in enumerate(counts):
            while count:
                nums[index] = num
                count -= 1
                index += 1
        return nums
    
# Time complexity: O(N)
#  Building `counts` takes O(N) time
#  Replacing `nums` takes O(N) time
#   Space complexity: O(1)
#  `counts` takes O(3) ~ O(1)


#Approach 2:

def sortArray(arr):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0

    for num in arr:
        if num == 0:
            cnt0 += 1
        elif num == 1:
            cnt1 += 1
        else:
            cnt2 += 1

    for i in range(cnt0):
        arr[i] = 0

    for i in range(cnt0, cnt0 + cnt1):
        arr[i] = 1

    for i in range(cnt0 + cnt1, len(arr)):
        arr[i] = 2

n = 6
arr = [0, 2, 1, 2, 0, 1]
sortArray(arr)
print("After sorting:")
for num in arr:
    print(num, end=" ")
print()

#Time Complexity: O(N) + O(N), where N = size of the array. 
#First O(N) for counting the number of 0’s, 1’s, 2’s, and 
#second O(N) for placing them correctly in the original array.

#Space Complexity: O(1) as we are not using any extra space.

########################################################

#Approach 3:
def sortArray(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

n = 6
arr = [0, 2, 1, 2, 0, 1]
sortArray(arr)
print("After sorting:")
for num in arr:
    print(num, end=" ")
print()


#Time Complexity: O(N), where N = size of the given array.
#Reason: We are using a single loop that can run at most N times.

#Space Complexity: O(1) as we are not using any extra space.

