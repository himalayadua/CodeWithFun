# Approach 1:
## Intuition
=========

As sorting is not allowed, we will count individual elements count.\
Then we will replace the `nums` according to the available counts, we counted earlier.

## Approach
========

1.  As there are only three values in `nums`, use a list `counts` of size 3
2.  Count total occurences for each value and store it in `counts`
3.  Replace the `nums` starting from count of 0 in `counts`, then 1 and then 2.
4.  Return `nums`

## Complexity
==========

-   Time complexity: O(N)

    -   Building `counts` takes O(N) time
    -   Replacing `nums` takes O(N) time
-   Space complexity: O(1)

    -   `counts` takes O(3) ~ O(1)



# Approach 2: Better Approach
## Algorithm / Intuition
Keeping count of values

Intuition: Since in this case there are only 3 distinct values in the array so it's easy to maintain the count of all, Like the count of 0, 1, and 2. This can be followed by overwriting the array based on the frequency(count) of the values.

Approach: 

1.  Take 3 variables to maintain the count of 0, 1 and 2.
2.  Travel the array once and increment the corresponding counting variables

( let's consider count_0 = a, count_1 = b, count_2 = c )

1.  In 2nd traversal of array, we will now over write the first 'a' indices / positions in array with '0', the next 'b' with '1' and the remaining 'c' with '2'.



# Approach 3:
## This problem is a variation of the popular **Dutch National flag algorithm**.

This algorithm contains 3 pointers i.e. low, mid, and high, and 3 main rules.  The rules are the following:

-   arr[0....low-1] contains 0. [Extreme left part]
-   arr[low....mid-1] contains 1.
-   arr[high+1....n-1] contains 2. [Extreme right part], n = size of the array

The middle part i.e. arr[mid....high] is the unsorted segment. So, hypothetically the array with different markers will look like the following:

![](https://static.takeuforward.org/wp/uploads/2023/03/Screenshot-2023-03-18-171206.png)

In our case, we can assume that the entire given array is unsorted and so we will place the pointers accordingly. For example, if the given array is: [2,0,2,1,1,0], the array with the 3 pointers will look like the following:

![](https://static.takeuforward.org/wp/uploads/2023/03/Screenshot-2023-03-18-171326.png)

Here, as the entire array is unsorted, we have placed the mid pointer in the first index and the high pointer in the last index. The low is also pointing to the first index as we have no other index before 0. Here, we are mostly interested in placing the 'mid' pointer and the 'high' pointer as they represent the unsorted part in the hypothetical array.

Now, let's understand how the pointers will work to make the array sorted.

Approach:

Note: *Here in this tutorial we will work based on the value of the mid pointer.*

The steps will be the following:

1.  First, we will run a loop that will continue until mid <= high.
2.  There can be three different values of mid pointer i.e. arr[mid]
    1.  If arr[mid] == 0, we will swap arr[low] and arr[mid] and will increment both low and mid. Now the subarray from index 0 to (low-1) only contains 0.
    2.  If arr[mid] == 1, we will just increment the mid pointer and then the index (mid-1) will point to 1 as it should according to the rules.
    3.  If arr[mid] == 2, we will swap arr[mid] and arr[high] and will decrement high. Now the subarray from index high+1 to (n-1) only contains 2.\
        In this step, we will do nothing to the mid-pointer as even after swapping, the subarray from mid to high(*after decrementing high*) might be unsorted. So, we will check the value of mid again in the next iteration.
3.  Finally, our array should be sorted.

Dry Run:

Assume the given array is [2,0,2,1,1,0]. The algorithm will be the following:

![](https://static.takeuforward.org/wp/uploads/2023/03/Screenshot-2023-03-18-171428.png)

![](https://static.takeuforward.org/wp/uploads/2023/03/Screenshot-2023-03-18-173242.png)

![](https://static.takeuforward.org/wp/uploads/2023/03/Screenshot-2023-03-18-173322.png)

In each iteration, if we check, the rules are always valid. This is how the algorithm works.
