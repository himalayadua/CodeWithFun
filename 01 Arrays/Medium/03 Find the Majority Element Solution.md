Approach 1: Sorting
===================

Intuition:
==========

The intuition behind this approach is that if an element occurs more than n/2 times in the array (where n is the size of the array), it will always occupy the middle position when the array is sorted. Therefore, we can sort the array and return the element at index n/2.

Explanation:
============

1.  The code begins by sorting the array `nums` in non-decreasing order using the `sort` function from the C++ Standard Library. This rearranges the elements such that identical elements are grouped together.
2.  Once the array is sorted, the majority element will always be present at index `n/2`, where `n` is the size of the array.
    -   This is because the majority element occurs more than n/2 times, and when the array is sorted, it will occupy the middle position.
3.  The code returns the element at index `n/2` as the majority element.

The time complexity of this approach is O(n log n) since sorting an array of size n takes O(n log n) time.





Approach 2: Hash Map
====================

Intuition:
==========

The intuition behind using a hash map is to count the occurrences of each element in the array and then identify the element that occurs more than n/2 times. By storing the counts in a hash map, we can efficiently keep track of the occurrences of each element.

Explanation:

1.  The code begins by initializing a hash map `m` to store the count of occurrences of each element.
2.  It then iterates through the array `nums` using a for loop.
3.  For each element `nums[i]`, it increments its count in the hash map `m` by using the line `m[nums[i]]++;`.
    -   If `nums[i]` is encountered for the first time, it will be added to the hash map with a count of 1.
    -   If `nums[i]` has been encountered before, its count in the hash map will be incremented by 1.
4.  After counting the occurrences of each element, the code updates `n` to be `n/2`, where `n` is the size of the array. This is done to check if an element occurs more than n/2 times, which is the criteria for being the majority element.
5.  The code then iterates through the key-value pairs in the hash map using a range-based for loop.
    -   For each key-value pair `(x.first, x.second)`, it checks if the count `x.second` is greater than `n`.
    -   If the count is greater than `n`, it means that `x.first` occurs more than n/2 times, so it returns `x.first` as the majority element.
6.  If no majority element is found in the hash map, the code returns 0 as the default value.
    -   Note that this will only occur if the input array `nums` is empty or does not have a majority element.

The time complexity of this approach is O(n) because it iterates through the array once to count the occurrences and then iterates through the hash map, which has a maximum size of the number of distinct elements in the array.

