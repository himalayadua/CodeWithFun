# Solution 1:

### Brute Force Approach: 

The extremely naive solution, we can think of, involves the use of an extra array. The algorithm is as follows.

### Algorithm:

-   Suppose, there are N-X zeros and X non-zero elements in the array. We will first copy those X non-zero elements from the original array to a temporary array. 
-   Then, we will copy the elements from the temporary array one by one and fill the first X places of the original array. 
-   The last N-X places of the original array will be then filled with zero. Now, our task is completed.



# Optimal Approach(Using 2 pointers): 

We can optimize the approach using 2 pointers i.e. i and j. The pointer j will point to the first 0 in the array and i will point to the next index.

Assume, the given array is {1, 0, 2, 3, 2, 0, 0, 4, 5, 1}. Now, initially, we will place the 2-pointers.

The algorithm will be the following.

### Algorithm:

1.  First, using a loop, we will place the pointer j. If we don't find any 0, we will not perform the following steps.
2.  After that, we will point i to index j+1 and start moving the pointer using a loop.
3.  While moving the pointer i, we will do the following:
    1.  If a[i] != 0 i.e. a[i] is a non-zero element: We will swap a[i] and a[j]. Now, the current j is pointing to the non-zero element a[i]. So, we will shift the pointer j by 1 so that it can again point to the first zero.
4.  Finally, our array will be set in the right manner.
