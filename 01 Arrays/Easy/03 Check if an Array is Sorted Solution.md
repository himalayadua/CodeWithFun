### **Approach**: Brute Force

-   simple solution
-   start with the element at the **0th** **index**
    -   compare it with all of its future elements that are present in the array.
-   If the picked element is smaller than or equal to all of its future values then we will move to the next **Index/element** until the whole array is traversed.
    -   If any of the picked elements is greater than its future elements, Then simply we will return **False.**
    -   If the size of the array is Zero or One i.e **( N = 0 or N = 1 )** or the entire array is traversed successfully then we will simply return **True.**


### **Approach**: Efficient (Single traversal)

-   sorted array = previous of every element is smaller than or equal to its current element.
-   i.e. if the previous element is smaller than or equal to the current element 
    -   then we can say that the two elements are sorted. 
    -   If the condition is true for the entire array then the array is **sorted.**
-   We will check every element with its previous element if the previous element is smaller than or equal to the current element then we will move to the next index.
-   If the whole array is traversed successfully or the size of the given array is zero or one **(i.e N = 0 or N = 1).** Then we will return **True** else return **False.**

