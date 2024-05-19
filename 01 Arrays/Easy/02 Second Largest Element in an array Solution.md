### **Solution 1: (Brute Force)**
--------------------------------
### **Intuition:**
[this approach only works if there are no duplicates]
What do we do to find the largest or the smallest element present in an array? We ideally sort them and the first element would be the smallest of all while the last element would be the largest. Can we find the second-smallest and second-largest using a similar approach?

### **Approach:**

-   Sort the array in ascending order
-   The element present at the second index is the second smallest element
-   The element present at the second index from the end is the second largest element




### **Solution 2(Better Solution)**
-------------------------------

### **Intuition:**

Even though we want to have just the second smallest and largest elements, we are still sorting the entire array for that and thus increasing the time complexity. Can we somehow try to not sort the array and still get our answer?

### **Approach:**

-   Find the smallest and largest element in the array in a single traversal
-   After this, we once again traverse the array and find an element that is just greater than the smallest element we just found.
-   Similarly, we would find the largest element which is just smaller than the largest element we just found
-   Indeed, this is our second smallest and second largest element.


### **Solution 3(Best Solution)**
-------------------------------

### **Intuition:**

In the previous solution, even though we were able to bring down the time complexity to O(N), we still needed to do two traversals to find our answer. Can we do this in a single traversal by using smart comparisons on the go?

#### **Approach:**

We would require four variables: small,second_small, large, and second_large. Variable small and second_small are initialized to INT_MAX while large and second_large are initialized to INT_MIN.

**Second Smallest Algo:**

-   If the current element is smaller than 'small', then we update second_small and small variables
-   Else if the current element is smaller than 'second_small' then we update the variable 'second_small'
-   Once we traverse the entire array, we would find the second smallest element in the variable second_small.
-   Here's a quick demonstration of the same.

**Second Largest Algo:**

-   If the current element is larger than 'large' then update second_large and large variables
-   Else if the current element is larger than 'second_large' then we update the variable second_large.
-   Once we traverse the entire array, we would find the second largest element in the variable second_large.
-   Here's a quick demonstration of the same.