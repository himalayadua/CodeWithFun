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