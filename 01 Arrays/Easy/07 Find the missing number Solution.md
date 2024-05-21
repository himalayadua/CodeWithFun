# Naive Approach(Brute-force approach): Approach 1

Intuition: For each number between 1 to N, we will try to find it in the given array using linear search. And if we don't find any of them, we will return the number.

## Approach: 

The algorithm steps are as follows:

1.  We will run a loop(say i) from 1 to N.
2.  For each integer, i, we will try to find it in the given array using linear search.
    1.  For that, we will run another loop to iterate over the array and consider a flag variable to indicate if the element exists in the array. Flag = 1 means the element is present and flag = 0 means the element is missing.
    2.  Initially, the flag value will be set to 0. While iterating the array, if we find the element, we will set the flag to 1 and break out from the loop.\
        Now, for any number i, if we cannot find it, the flag will remain 0 even after iterating the whole array and we will return the number.

## Dry run:
Assume given array = {1, 3} and N = 3.

Note: *For each number, before starting the linear search, we set the flag to 0*.

For i = 1, flag = 0
We will try to find 1 in the array using linear search and in the first index, we can find it and the flag will be 1. So, it is not the missing number.

For i = 2, flag = 0
We will try to find 2 in the given array using linear search. But number 2 is not present and the flag will remain 0. So, we will return 2 as it is the missing number.



# Better Approach (using Hashing): Approach 2
## Intuition:
Using the hashing technique, we will store the frequency of each element of the given array. Now, the number( i.e. between 1 to N) for which the frequency will be 0, will be returned. Refer to the article link to know more about hashing.

## Approach:
The algorithm steps are as follows:

The range of the number is 1 to N. So, we need a hash array of size N+1 (as we want to store the frequency of N as well).
Now, for each element in the given array, we will store the frequency in the hash array.
After that, for each number between 1 to N, we will check the frequencies. And for any number, if the frequency is 0, we will return it.
Dry run:

Assume the given array = {1,3} and N = 3. We can clearly see that for index 2 the frequency is 0 and so 2 is our answer.


# Summation Approach: Approach 3

## Intuition:

We know that the summation of the first N numbers is (N*(N+1))/2. We can say this S1. Now, in the given array, every number between 1 to N except one number is present. So, if we add the numbers of the array (say S2), the difference between S1 and S2 will be the missing number. Because, while adding all the numbers of the array, we did not add that particular number that is missing.

Sum of first N numbers(S1) = (N*(N+1))/2
Sum of all array elements(S2) = i = 0n-2a[i]
The missing number = S1-S2

## Approach:

The steps are as follows:

1.  We will first calculate the summation of first N natural numbers(i.e. 1 to N) using the specified formula.
2.  Then we will add all the array elements using a loop.
3.  Finally, we will consider the difference between the summation of the first N natural numbers and the sum of the array elements.

## Dry run:

Assume the given array is: {1, 2, 4, 5} and N = 5.
Summation of 1 to 5 = (5*(5+1))/2 = 15
Summation of array elements = 12
So, the difference will be = 15 - 12 = 3.
And the missing number is also 3.



# XOR Approach: Approach 4
## Intuition:

Two important properties of XOR are the following:

XOR of two same numbers is always 0 i.e. a ^ a = 0. ←Property 1.\
XOR of a number with 0 will result in the number itself i.e. 0 ^ a = a.  ←Property 2

Now, let's XOR all the numbers between 1 to N.\
xor1 = 1^2^.......^N

Let's XOR all the numbers in the given array.\
xor2 = 1^2^......^N (contains all the numbers except the missing one).

Now, if we again perform XOR between xor1 and xor2, we will get:\
xor1 ^ xor2 = (1^1)^(2^2)^........^(missing Number)^.....^(N^N)

Here all the numbers except the missing number will form a pair and each pair will result in 0 according to the XOR property. The result will be = 0 ^ (missing number) = missing number (according to property 2).

*So, if we perform the XOR of the numbers 1 to N with the XOR of the array elements, we will be left with the missing number.*

## Approach:

The steps are as follows:

1.  We will first run a loop(say i) from 0 to N-2(as the length of the array = N-1).
2.  Inside the loop, xor2 variable will calculate the XOR of array elements\
    i.e. xor2 = xor2 ^ a[i].\
    And the xor1 variable will calculate the XOR of 1 to N-1 i.e. xor1 = xor1 ^ (i+1).
3.  After the loop ends we will XOR xor1 and N to get the total XOR of 1 to N.
4.  Finally, the answer will be the XOR of xor1 and xor2.

## Dry run:

Assume the given array is: {1, 2, 4, 5} and N = 5.
XOR of (1 to 5) i.e. xor1 = (1^2^3^4^5)
XOR of array elements i.e. xor2 = (1^2^4^5)
XOR of xor1 and xor2 = (1^2^3^4^5) ^ (1^2^4^5)
			= (1^1)^(2^2)^(3)^(4^4)^(5^5)
			= 0^0^3^0^0 = 0^3 = 3.
The missing number is 3.
