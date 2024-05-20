# Solution 1: Brute force Approach

### Intuition:

The rotated array has just a difference that its first element is present at the last index of the array. So if we can just store the element at the first index and then shift all the elements towards the left and at last put the stored element at the last index. We will get th rotated array.

### Approach:

We can take another dummy array of the same length and then shift all elements in the array toward the left and then at the last element store the index of 0th index of the array and print it.

# Solution 2:

### Approach: 

Here, in the given array :

```python
n = 5,
arr[] = {1,2,3,4,5}
```

At first, we have to shift the array towards the left so, we store the value of the first index in a variable (let it be x).

Then we iterate the array from the 0th index to the `n-1th` index(why `n-1` i will explain it below)

And then store the value present in the next index to the current index like this :

```python
arr[i] = arr[i+1]
```

And to prevent its segmentation fault we will iterate it till `n-1`.

At last, put the value of variable x in the last index of the array.



# Solution 3:

### Intuition

When I first encountered the problem of rotating an array, my initial thought was to create a new array to store the rotated elements. This seemed like a straightforward approach, where I could directly place each element into its new position. I thought of using an extra array (`output`) where the elements of the original array (`nums`) could be repositioned based on the rotation count `k`. The idea was to calculate the new index for each element and then copy them back to `nums`.

### Approach

My initial approach involved using a new array to temporarily hold the rotated values. I calculated the new index for each element in `nums`, taking into account the rotation count `k`. After populating the `output` array with the rotated elements, I copied these values back into the original `nums` array. However, this approach didn't modify `nums` in-place as required. I then learned about a more efficient technique, which involved reversing parts of the array. This approach begins by reversing the entire array, then reversing the first `k` elements, and finally reversing the remaining elements. This method cleverly utilizes the properties of reversal to achieve the rotation without needing any extra space.

### Complexity

-   Time complexity:\
    The time complexity is `O(n)`, as each element is accessed a constant number of times during the reversal process.

-   Space complexity:\
    The space complexity is `O(1)`, as the rotation is done in-place without using any additional storage proportional to the input size.

