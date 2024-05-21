# Solution 1:

def moveZeros(n: int,  a: [int]) -> [int]:
    # Temporary array
    temp = []
    
    # Copy non-zero elements from original to temp array
    for i in range(n):
        if a[i] != 0:
            temp.append(a[i])
    
    # Number of non-zero elements
    nz = len(temp)
    
    # Copy elements from temp to fill first nz fields of original array
    for i in range(nz):
        a[i] = temp[i]
    
    # Fill the rest of the cells with 0
    for i in range(nz, n):
        a[i] = 0
    
    return a

arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n = 10
ans = moveZeros(n, arr)
for it in ans:
    print(it, end=" ")
print()


# Time Complexity: O(N) + O(X) + O(N-X) ~ O(2*N), where N = total no. of elements,
# X = no. of non-zero elements, and N-X = total no. of zeros.
# Reason: O(N) for copying non-zero elements from the original to the temporary array. O(X) for again copying it back from the temporary to the original array. O(N-X) for filling zeros in the original array. So, the total time complexity will be O(2*N).

# Space Complexity: O(N), as we are using a temporary array to solve this problem and the maximum size of the array can be N in the worst case.
# Reason: The temporary array stores the non-zero elements. In the worst case, all the given array elements will be non-zero.


# Solution 2:




def moveZeros(n: int,  a: [int]) -> [int]:
    j = -1
    # Place the pointer j
    for i in range(n):
        if a[i] == 0:
            j = i
            break
    
    # No non-zero elements
    if j == -1:
        return a
    
    # Move the pointers i and j and swap accordingly
    for i in range(j + 1, n):
        if a[i] != 0:
            a[i], a[j] = a[j], a[i]
            j += 1
    
    return a


arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n = 10
ans = moveZeros(n, arr)
for it in ans:
    print(it, end=' ')
print()



# Output: 1 2 3 2 4 5 1 0 0 0

# Time Complexity: O(N), N = size of the array.
# Reason: We have used 2 loops and using those loops, we are basically traversing the array once.

# Space Complexity: O(1) as we are not using any extra space to solve this problem.


