# Solution:

## Approach 1:  
We maintain a variable count that keeps a track of the number of consecutive 1's while traversing the array. The other variable max_count maintains the maximum number of 1's, in other words, it maintains the answer.

We start traversing from the beginning of the array. Since we can encounter either a 1 or 0 there can be two situations:-

1.  If  the value at the current index is equal to 1 we increase the value of count by one. After updating  the count variable if it becomes more than the max_count  update the max_count.
2.  If the value at the current index is equal to zero we make the variable count as 0 since there are no more consecutive ones.


## Approach 2:
### Sliding window with max window size

Make window big as possible. When window has zeros just move left window pointer. At the end of processing in the window can be some zeros, but we don't care, because need return just window size `r - l + 1`\
Example for:`111001`\
`[1]11001 => l = 0, r = 0`\
`[11]1001 => l = 0, r = 1`\
`[111]001 => l = 0, r = 2 => max result 2 - 0 + 1 = 3`\
`1[110]01 => l = 1, r = 3 => keep max window size, but move left pointer`\
`11[100]1 => l = 2, r = 4 => move left pointer again`\
`111[001] => l = 3, r = 5 => move left pointer again, window size is the answer => 5 - 3 + 1 = 3`


## Approach 3:
### Greedy

Calculate count in a row. When meet zero update max result. There is one edge case for cases when the last element is `1`: like `0111[1]` or `1111[1]`, so we didn't update result in the loop. To solve just update max result at the end `res = max(res, windowSize)`.

