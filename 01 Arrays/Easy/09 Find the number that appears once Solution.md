# Approach 1 (Brute-force approach): 

## Intuition:

For every element present in the array, we will do a linear search and count the occurrence. If for any element, the occurrence is 1, we will return it.

## Approach:

The steps are as follows:

1.  First, we will run a loop(say i) to select the elements of the array one by one.
2.  For every element arr[i], we will perform a linear search using another loop and count its occurrence.
3.  If for any element the occurrence is 1, we will return it.




# Approach 2 - Better Approach(Using Hashing): 

## Intuition:

In the previous approach, we were finding the occurrence of an element using linear search. We can optimize this using hashing technique. We can simply hash the elements along with their occurrences in the form of (key, value) pair. Thus, we can reduce the cost of finding the occurrence and hence the time complexity.

Now, hashing can be done in two different ways and they are the following:

-   Array hashing(not applicable if the array contains negatives or very large numbers)
-   Hashing using the map data structure

## Array hashing:

In order to hash using an array, we need to first find the maximum element(say maxElement) to get the range of the hash array. The index of the hash array will represent the elements of the given array and the value stored in that index will be the number of occurrences. Now, the size of the array must be maxElement+1 as we need to hash the maxElement itself.

### Approach:

The steps are as follows:

1.  First, we will find the maximum element(say maxElement) to know the size of the hash array.
2.  Then we will declare a hash array of size maxElement+1.
3.  Now, using another loop we will store the elements of the array along with their frequency in the hash array. (i.e. hash[arr[i]]++)
4.  After that, using another loop we will iterate over the hash array, and try to find the element for which the frequency is 1, and finally, we will return that particular element.

Note: While searching for the answer finally, we can either use a loop from 0 to n(i.e. Size of the array) or use a loop from 0 to maxElement. So, the time complexity will change accordingly.

Now, using array hashing it is difficult to hash the elements of the array if it contains negative numbers or a very large number. So to avoid these problems, we will be using the map data structure to hash the array elements.



# Approach 3 - Hashing using the map data structure: 

## Intuition:

The intuition will be the same as the array hashing. The only difference here is we will use the map data structure for hashing instead of using another array for hashing.

## Approach:

The steps are as follows:

1.  First, we will declare a map.
2.  Now, using a loop we will store the elements of the array along with their frequency in the map data structure.
3.  Using another loop we will iterate over the map, and try to find the element for which the frequency is 1, and finally, we will return that particular element.



# Approach 4 - Optimal Approach(Using XOR): 

## Intuition:

Two important properties of XOR are the following:

XOR of two same numbers is always 0 i.e. a ^ a = 0. ←Property 1.\
XOR of a number with 0 will result in the number itself i.e. 0 ^ a = a.  ←Property 2

Here all the numbers except the single number appear twice and so will form a pair. Now, if we perform XOR of all elements of the array, the XOR of each pair will result in 0 according to the XOR property 1. The result will be = 0 ^ (single number) = single number (according to property 2).

*So, if we perform the XOR of all the numbers of the array elements, we will be left with a single number.*

## Approach:

-   We will just perform the XOR of all elements of the array using a loop and the final XOR will be the answer.

Dry run:

Assume the given array is: [4,1,2,1,2]\
XOR of all elements = 4^1^2^1^2\
      = 4 ^ (1^1) ^ (2^2)\
      = 4 ^ 0 ^ 0 = 4^0 = 4\
Hence, 4 is the single element in the array.