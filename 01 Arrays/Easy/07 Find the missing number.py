# Naive Approach(Brute-force approach): Approach 1

def missing_number(a, N):
    # Outer loop that runs from 1 to N:
    for i in range(1, N + 1):
        # flag variable to check if an element exists
        flag = 0

        # Search the element using linear search:
        for j in range(len(a)):
            if a[j] == i:
                # i is present in the array:
                flag = 1
                break

        # check if the element is missing (i.e., flag == 0):
        if flag == 0:
            return i

    # The following line will never execute.
    # It is just to avoid warnings.
    return -1

def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missing_number(a, N)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()


# Time Complexity: O(N2), where N = size of the array+1.
## Reason: In the worst case i.e. if the missing number is N itself, the outer loop will run for N times, and for every single number the inner loop will also run for approximately N times. So, the total time complexity will be O(N2).

# Space Complexity: O(1)  as we are not using any extra space.


#############################################################################

# Better Approach (using Hashing): Approach 2

def missingNumber(a, N):
    hash = [0] * (N + 1)  # hash array

    # storing the frequencies:
    for i in range(N - 1):
        hash[a[i]] += 1

    # checking the frequencies for numbers 1 to N:
    for i in range(1, N + 1):
        if hash[i] == 0:
            return i

    # The following line will never execute.
    # It is just to avoid warnings.
    return -1

def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missingNumber(a, N)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()



# Time Complexity: O(N) + O(N) ~ O(2*N),  where N = size of the array+1.
# Reason: For storing the frequencies in the hash array, the program takes O(N) time complexity and for checking the frequencies in the second step again O(N) is required. So, the total time complexity is O(N) + O(N).

# Space Complexity: O(N), where N = size of the array+1. Here we are using an extra hash array of size N+1.


###############################################################################

# Summation Approach: Approach 3



def missingNumber(a, N):
    # Summation of first N numbers:
    summation = (N * (N + 1)) // 2

    # Summation of all array elements:
    s2 = sum(a)

    missingNum = summation - s2
    return missingNum

def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missingNumber(a, N)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()


# Time Complexity: O(N), where N = size of array+1.
# Reason: Here, we need only 1 loop to get the sum of the array elements. The loop runs for approx. N times. So, the time complexity is O(N).

# Space Complexity: O(1) as we are not using any extra space.

#########################################################################

# XOR Approach: Approach 4



def missingNumber(a, N):
    xor1 = 0
    xor2 = 0

    for i in range(N - 1):
        xor2 = xor2 ^ a[i]  # XOR of array elements
        xor1 = xor1 ^ (i + 1)  # XOR up to [1...N-1]
    
    xor1 = xor1 ^ N  # XOR up to [1...N]

    return xor1 ^ xor2  # the missing number


def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missingNumber(a, N)
    print("The missing number is:", ans)


if __name__ == '__main__':
    main()


# Time Complexity: O(N), where N = size of array+1.
# Reason: Here, we need only 1 loop to calculate the XOR. The loop runs for approx. N times. So, the time complexity is O(N).

# Space Complexity: O(1) as we are not using any extra space.


