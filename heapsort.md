# **Heap Sort**


Heap Sort is an efficient comparison-based sorting algorithm that belongs to the family of selection sorts. In this section, we will dive deep into the inner workings of Heap Sort, exploring its implementation, performance, advantages, and disadvantages. By the end of this section, you will have a solid understanding of Heap Sort and be equipped to implement it in your projects.

## **Content Table**
- [**Heap Sort**](#heap-sort)
  - [**Content Table**](#content-table)
  - [**Chapter 1: Introduction to Heap Sort**](#chapter-1-introduction-to-heap-sort)
    - [**1. What is Heap Sort?**](#1-what-is-heap-sort)
    - [**2. How Does Heap Sort Work?**](#2-how-does-heap-sort-work)
    - [**3. Importance of Heap Sort**](#3-importance-of-heap-sort)
  - [**Chapter 2: Data Structures: Heaps**](#chapter-2-data-structures-heaps)
    - [**1. What is Heap?**](#1-what-is-heap)
    - [**2. Max-Heap and Min-Heap**](#2-max-heap-and-min-heap)
    - [**3. Maintaining Heap Property**](#3-maintaining-heap-property)
  - [**Chapter 3: Heap Sort**](#chapter-3-heap-sort)
    - [**1. Building the Heap**](#1-building-the-heap)
    - [**2. Extracting Elements**](#2-extracting-elements)
    - [**3. Iterative Heap Sort**](#3-iterative-heap-sort)
    - [**4. Recursive Heap Sort**](#4-recursive-heap-sort)
    - [**5. Psuedocode**](#5-psuedocode)
  - [**Chapter 4: Time Complexity Analysis**](#chapter-4-time-complexity-analysis)
    - [**1. Best-Case, Worst-Case, and Average-Case Time Complexity**](#1-best-case-worst-case-and-average-case-time-complexity)
    - [**2. Comparison with Other Sorting Algorithms**](#2-comparison-with-other-sorting-algorithms)
  - [**Chapter 5: Space Complexity Analysis**](#chapter-5-space-complexity-analysis)
    - [**1. In-Place Sorting**](#1-in-place-sorting)
    - [**2. Space Complexity**](#2-space-complexity)
    - [**3. Comparison with Other Sorting Algorithms**](#3-comparison-with-other-sorting-algorithms)
  - [**Chapter 6: Advantages, Disadvantages and Application**](#chapter-6-advantages-disadvantages-and-application)
    - [**1. Advantages of Heap Sort:**](#1-advantages-of-heap-sort)
    - [**2. Disadvantages of Heap Sort:**](#2-disadvantages-of-heap-sort)
    - [**3. Applications of Heap Sort:**](#3-applications-of-heap-sort)
  - [**Chapter 7: Implementation**](#chapter-7-implementation)
    - [**1. Python Implementation**](#1-python-implementation)
    - [**2. Java Implementation**](#2-java-implementation)
    - [**3. C++ Implementation**](#3-c-implementation)
  - [**Chapter 8: Summary**](#chapter-8-summary)
  - [**Chapter 9: Quiz**](#chapter-9-quiz)


## **Chapter 1: Introduction to Heap Sort**

### **1. What is Heap Sort?**

Heap Sort is an efficient, comparison-based sorting algorithm that uses the heap data structure to sort a given dataset. Invented by J.W.J. Williams in 1964, Heap Sort is a part of the selection sort family. It works by dividing the input into a sorted and an unsorted region and iteratively extracting the maximum or minimum element from the unsorted region and moving it to the sorted region.  

Heap Sort is an in-place sorting algorithm, meaning it does not require additional memory to be allocated for the sorted output. Instead, it rearranges the elements within the input dataset. Heap Sort is not a stable sort, which means that the relative order of equal elements may not be preserved.  

### **2. How Does Heap Sort Work?**

Heap Sort uses a binary heap data structure, which is a complete binary tree with either the max-heap or min-heap property. The max-heap property states that each parent node is greater than or equal to its children, while the min-heap property states that each parent node is less than or equal to its children.  

The algorithm can be divided into two main phases:

Building the Heap: The input dataset is transformed into a max-heap (or a min-heap, depending on the desired order of the output). This step is performed in linear time, taking O(n) time complexity.

Extracting Elements: The maximum (or minimum) element of the heap is repeatedly removed and placed at the end of the unsorted region. This step is performed for each element in the input dataset, taking O(n log n) time complexity.  

The combination of these two phases results in a sorted dataset in ascending (or descending) order. Throughout this section, we will delve deeper into the specifics of each phase and discuss the variations and optimizations of the Heap Sort algorithm.  

### **3. Importance of Heap Sort**

Heap Sort is an important sorting algorithm in computer science due to its efficiency and in-place nature. Although other algorithms like Quick Sort and Merge Sort may have better average-case performance, Heap Sort can be advantageous in specific scenarios, such as when limited memory is available or when a worst-case time complexity of O(n log n) is required.

Moreover, Heap Sort forms the foundation for other algorithms and data structures, such as priority queues, which are widely used in various applications like task scheduling, network packet scheduling, and graph algorithms.

In the following chapters, we will explore the heap data structure in detail, examine the Heap Sort algorithm step by step, and analyze its performance in terms of time and space complexity. By the end of this section, you will have a comprehensive understanding of Heap Sort and be able to implement it in your projects.

## **Chapter 2: Data Structures: Heaps**

### **1. What is Heap?**

A heap is a specialized tree-based data structure that satisfies the heap property. It is a complete binary tree, meaning that every level of the tree is fully filled except for the last level, which is filled from left to right. The heap property requires that each parent node is either greater than or equal to its children (max-heap) or less than or equal to its children (min-heap).

### **2. Max-Heap and Min-Heap**

There are two types of heaps: max-heaps and min-heaps. The main difference between them lies in the heap property they enforce.
- Max-Heap: In a max-heap, each parent node is greater than or equal to its children. The largest element in a max-heap is always at the root node. Max-heaps are commonly used to implement algorithms like Heap Sort in ascending order.
- Min-Heap: In a min-heap, each parent node is less than or equal to its children. The smallest element in a min-heap is always at the root node. Min-heaps are commonly used to implement algorithms like Heap Sort in descending order, as well as other algorithms like Dijkstra's shortest path algorithm.

### **3. Maintaining Heap Property**

To ensure that the heap property is maintained, we need to perform certain operations during insertions and deletions. These operations are known as "heapify" operations and involve swapping nodes to restore the heap property if it is violated.

- Heapify Up (also known as Bubble-Up or Sift-Up): Heapify up is used when inserting a new element into the heap or increasing the value of an existing element. Starting from the newly inserted or modified node, we compare it with its parent. If the heap property is violated, we swap the node with its parent and continue the process until the heap property is restored or the root node is reached.
- Heapify Down (also known as Bubble-Down or Sift-Down): Heapify down is used when deleting the root element or decreasing the value of an existing element. Starting from the modified node, we compare it with its children. If the heap property is violated, we swap the node with the child that maintains the heap property (the larger child for max-heap or the smaller child for min-heap) and continue the process until the heap property is restored or a leaf node is reached.

By performing these heapify operations, we can ensure that the heap property is maintained during insertions and deletions, allowing the heap to be efficiently used for various algorithms, including Heap Sort.

In the next chapter, we will discuss the Heap Sort algorithm in detail, explaining how it leverages the heap data structure to efficiently sort a given dataset.

## **Chapter 3: Heap Sort**

### **1. Building the Heap**

The first step in the Heap Sort algorithm is to convert the input dataset into a max-heap (for ascending sort) or a min-heap (for descending sort). This process takes $O(n)$ time complexity. The following steps outline the process of building a max-heap (a similar process can be followed for building a min-heap):

1. Treat the input dataset as an array representation of a complete binary tree.
2. Start from the last non-leaf node, which is the parent of the last element in the array (index `floor(n/2) - 1`, where `n` is the total number of elements).
3. Perform the heapify down operation on the current node.
4. Move to the previous node in the array and repeat steps 3 and 4 until the root node is reached.

After completing this process, the input dataset will have been transformed into a max-heap.

### **2. Extracting Elements**

Once the heap is built, we can begin extracting the maximum (or minimum) element and placing it at the end of the unsorted region. This process takes $O(n\log n)$ time complexity. The following steps outline the process for extracting elements from a max-heap (a similar process can be followed for a min-heap):

1. Swap the root node (maximum element) with the last element in the array.
2. Decrease the size of the unsorted region by one.
3. Perform the heapify down operation on the new root node.
4. Repeat steps 1 to 3 until the entire array is sorted.

At the end of this process, the input dataset will be sorted in ascending order.

### **3. Iterative Heap Sort**

Heap Sort can be implemented iteratively using loops. The iterative approach is easier to understand for beginners and is generally considered more efficient due to the lack of function call overhead. The following is a high-level outline of the iterative Heap Sort algorithm:

1. Build the max-heap (or min-heap) from the input dataset.
2. Iterate from the last element of the array to the first element, performing the following steps for each element:
   3. Swap the current element with the root node.
   4. Perform the heapify down operation on the root node, considering the unsorted region only.
3. The input dataset is now sorted.

### **4. Recursive Heap Sort**

Heap Sort can also be implemented recursively by defining recursive functions for the heapify up and heapify down operations. Recursive implementations are often more concise but can be less efficient due to function call overhead. The following is a high-level outline of the recursive Heap Sort algorithm:

1. Build the max-heap (or min-heap) from the input dataset using a recursive heapify down function.
2. Define a recursive sorting function that takes the current index and the size of the unsorted region as arguments:
   1. If the current index is zero, return (the entire dataset is sorted).
   2. Swap the element at the current index with the root node.
   3. Perform the heapify down operation on the root node, considering the unsorted region only.
   4. Call the sorting function recursively with the previous index and the reduced size of the unsorted region.
3. Call the sorting function with the last index and the size of the input dataset.
4. The input dataset is now sorted.
In the following chapters, we will analyze the time and space complexity of the Heap Sort algorithm, discuss its advantages and disadvantages, and provide sample implementations in various programming languages.

### **5. Psuedocode**
```
function heapSort(arr):
    n = length(arr)
    
    // Build the max-heap
    for i from floor(n/2) - 1 to 0 (inclusive) step -1:
        heapifyDown(arr, i, n)

    // Extract elements from the max-heap
    for i from n - 1 to 1 (inclusive) step -1:
        swap(arr[0], arr[i])
        heapifyDown(arr, 0, i)

    return arr

function heapifyDown(arr, i, heapSize):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    // Check if left child is larger than the current largest element
    if left < heapSize and arr[left] > arr[largest]:
        largest = left

    // Check if right child is larger than the current largest element
    if right < heapSize and arr[right] > arr[largest]:
        largest = right

    // Swap and continue heapifying if the largest element is not the current element
    if largest != i:
        swap(arr[i], arr[largest])
        heapifyDown(arr, largest, heapSize)
```

## **Chapter 4: Time Complexity Analysis**

### **1. Best-Case, Worst-Case, and Average-Case Time Complexity**

The time complexity of Heap Sort can be analyzed in three different scenarios: best-case, worst-case, and average-case. However, for Heap Sort, all these scenarios share the same time complexity.

*Best-Case*: The best-case scenario for Heap Sort occurs when the input dataset is already sorted or nearly sorted. Despite the sorted nature of the dataset, Heap Sort must still build the heap and extract elements, resulting in a time complexity of $O(n\log n)$.

*Worst-Case*: The worst-case scenario for Heap Sort occurs when the input dataset is sorted in the reverse order. Even in this case, the time complexity remains O(n log n) due to the nature of the heap-building and extraction processes.

*Average-Case*: The average-case time complexity of Heap Sort is also $O(n\log n)$ regardless of the distribution of the input dataset.

In all cases, Heap Sort exhibits a time complexity of O(n log n), which makes it an efficient sorting algorithm. However, it's important to note that Heap Sort is not a stable sort, which means that it may not maintain the relative order of equal elements.

### **2. Comparison with Other Sorting Algorithms**

Heap Sort, while efficient, is often outperformed by other sorting algorithms in practice, such as Quick Sort and Merge Sort. Let's compare Heap Sort's time complexity with other popular sorting algorithms:

*Quick Sort*: Quick Sort has an average-case and best-case time complexity of O(n log n), like Heap Sort. However, its worst-case time complexity is $O(n^2)$, which occurs when the input dataset is already sorted or nearly sorted. Despite this, Quick Sort is often faster in practice due to its smaller constant factors and better cache performance.

*Merge Sort*: Merge Sort also has a time complexity of $O(n\log n)$ in all cases. Unlike Heap Sort, Merge Sort is a stable sorting algorithm, which may be an advantage in certain applications. However, Merge Sort is not an in-place algorithm, requiring $O(n)$ additional space for the sorted output, whereas Heap Sort sorts the dataset in-place.

*Bubble Sort, Selection Sort, and Insertion Sort*: These elementary sorting algorithms have a worst-case and average-case time complexity of $O(n^2)$, making them less efficient than Heap Sort for large datasets. However, they may perform better on small or nearly sorted datasets and are generally easier to implement.

In conclusion, Heap Sort is an efficient sorting algorithm with a time complexity of $O(n\log n)$ in all cases. While other algorithms like Quick Sort and Merge Sort may outperform Heap Sort in practice, Heap Sort's in-place nature and guaranteed $O(n\log n)$ worst-case time complexity make it a valuable algorithm in specific scenarios where memory is limited or a guaranteed worst-case performance is required.

## **Chapter 5: Space Complexity Analysis**

### **1. In-Place Sorting**

Heap Sort is an in-place sorting algorithm, which means that it sorts the input dataset without requiring additional memory for a separate sorted output. Instead, the algorithm rearranges the elements within the input array itself, resulting in a low space complexity.

### **2. Space Complexity**

Heap Sort has a space complexity of $O(1)$, as it only requires a constant amount of additional memory to perform the heapify operations and store temporary variables. This constant amount of extra memory does not depend on the size of the input dataset.

The in-place nature of Heap Sort makes it an attractive option for sorting large datasets when memory is limited. However, it's essential to consider that Heap Sort is not a stable sorting algorithm, meaning that it may not maintain the relative order of equal elements during the sorting process.

### **3. Comparison with Other Sorting Algorithms**

When compared to other popular sorting algorithms, Heap Sort stands out as a low-space complexity algorithm:

*Quick Sort*: Quick Sort is an in-place sorting algorithm like Heap Sort, although its space complexity is slightly higher at $O(\log n)$ due to the recursive nature of the algorithm, which requires additional memory for the function call stack. In practice, Quick Sort may have better cache performance than Heap Sort, which can result in faster execution times.

*Merge Sort*: Merge Sort is not an in-place sorting algorithm and has a space complexity of $O(n)$, as it requires additional memory to store the sorted output. Although Merge Sort is a stable sorting algorithm with a time complexity of $O(n\log n)$, the increased space complexity can be a drawback when memory is limited.

*Bubble Sort, Selection Sort, and Insertion Sort*: These elementary sorting algorithms are also in-place, like Heap Sort, with a space complexity of $O(1)$. However, their time complexity is $O(n^2)$, making them less efficient than Heap Sort for large datasets.

In conclusion, Heap Sort is an efficient in-place sorting algorithm with low space complexity, making it suitable for scenarios with limited memory or when minimizing memory usage is a priority. However, its lack of stability should be considered when the relative order of equal elements must be preserved.

## **Chapter 6: Advantages, Disadvantages and Application**

In this chapter, we will discuss the advantages and disadvantages of Heap Sort, considering its efficiency, stability, and adaptability compared to other sorting algorithms. We will also explore some common applications of Heap Sort in various domains.

### **1. Advantages of Heap Sort:**

1. In-place sorting: Heap Sort is an in-place sorting algorithm, which means it doesn't require any additional memory for sorting other than the input array. This makes Heap Sort memory-efficient compared to other algorithms like Merge Sort.
2. Time complexity: Heap Sort has a time complexity of $O(n\log n)$ in the best, worst, and average cases, making it a reliable choice for sorting large datasets.
3. No recursion: Heap Sort doesn't use recursion, which can reduce the risk of stack overflow errors, especially when working with large datasets.

### **2. Disadvantages of Heap Sort:**

1. Not stable: Heap Sort is not a stable sorting algorithm. This means that equal elements may not maintain their original order in the sorted array, which can be a problem when sorting data with additional attributes that need to be preserved.
2. Less efficient for small datasets: Heap Sort might not be the most efficient choice for small datasets, as other algorithms, such as Insertion Sort or Quick Sort, can perform better in such cases.
3. Slower in practice: While Heap Sort has a favorable time complexity, it can be slower in practice compared to Quick Sort due to its larger constant factors and poor cache performance.

### **3. Applications of Heap Sort:**

1. Priority queues: Heap Sort is a suitable choice for implementing priority queues, which are used in scheduling algorithms, task management systems, and other applications where elements need to be sorted based on their priority.
2. Graph algorithms: Heap Sort can be used in graph algorithms like Dijkstra's shortest path algorithm and Prim's minimum spanning tree algorithm, where the priority queue is a key component.
3. K-th largest element: Heap Sort can be used to find the k-th largest element in an array efficiently, without having to sort the entire array.
4. External sorting: Heap Sort is a good candidate for external sorting, where the dataset is too large to fit in memory, and sorting must be performed using external storage devices like disks.

By understanding the advantages, disadvantages, and applications of Heap Sort, we can make informed decisions about when to use this algorithm and when to consider other sorting techniques.

## **Chapter 7: Implementation**

In this chapter, we will provide sample implementations of Heap Sort in popular programming languages such as Python, Java, and C++. Each implementation includes detailed explanations and comments to ensure understanding.

### **1. Python Implementation**
```python
def heapify(arr, n, i):
    largest = i  # Initialize largest as the root
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the largest element found so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest element is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build the max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the max-heap and maintain the heap property
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap

# Example usage
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array is", arr)
```

### **2. Java Implementation**
```java
public class HeapSort {
    public void sort(int arr[]) {
        int n = arr.length;

        // Build the max-heap
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i);

        // Extract elements from the max-heap and maintain the heap property
        for (int i = n - 1; i > 0; i--) {
            // Swap the root with the last element
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            // Heapify the reduced heap
            heapify(arr, i, 0);
        }
    }

    void heapify(int arr[], int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        // Check if left child exists and is greater than the root
        if (left < n && arr[left] > arr[largest])
            largest = left;

        // Check if right child exists and is greater than the largest element found so far
        if (right < n && arr[right] > arr[largest])
            largest = right;

        // If the largest element is not the root, swap and continue heapifying
        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;

            heapify(arr, n, largest);
        }
    }

    // Example usage
    public static void main(String args[]) {
        int arr[] = {12, 11, 13, 5, 6, 7};
        int n = arr.length;

        HeapSort ob = new HeapSort();
        ob.sort(arr);

        System.out.println("Sorted array is");
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }
}
```

### **3. C++ Implementation**
```cpp
#include <iostream>
using namespace std;

void heapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    // Check if left child exists and is greater than the root
    if (left < n && arr[left] > arr[largest])
        largest = left;

    // Check if right child exists and is greater than the largest element found so far
    if (right < n && arr[right] > arr[largest])
        largest = right;

    // If the largest element is not the root, swap and continue heapifying
    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heap_sort(int arr[], int n) {
    // Build the max-heap
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // Extract elements from the max-heap and maintain the heap property
    for (int i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i]);  // Swap the root with the last element
        heapify(arr, i, 0);  // Heapify the reduced heap
    }
}

// Example usage
int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    heap_sort(arr, n);

    cout << "Sorted array is: ";
    for (int i = 0; i < n; ++i)
        cout << arr[i] << " ";
    cout << endl;

    return 0;
}
```

These implementations demonstrate how Heap Sort can be implemented in Python, Java, and C++. Each code snippet includes detailed explanations and comments to ensure understanding. By studying these implementations, you can gain a deeper understanding of the Heap Sort algorithm and how to apply it in different programming languages.

## **Chapter 8: Summary**

Throughout this section, we have delved into the intricacies of the Heap Sort algorithm. We've explored the underlying data structure – heaps – and discussed the properties of max-heaps and min-heaps. We've analyzed the time and space complexity of Heap Sort, compared its performance to other sorting algorithms, and discussed its advantages and disadvantages.

Additionally, we provided sample implementations of Heap Sort in popular programming languages, such as Python, Java, and C++, to help you understand how the algorithm can be applied in real-world scenarios. We've also discussed common use cases and applications where Heap Sort is the preferred sorting algorithm.

As we conclude our journey, we encourage you to further study and experiment with Heap Sort. Understanding this powerful and efficient algorithm will be beneficial in your journey as a programmer or computer scientist. Practice implementing Heap Sort in your preferred programming language, analyze its performance, and compare it to other sorting algorithms. As you gain a deeper understanding of Heap Sort, you will be better equipped to choose the right sorting algorithm for your specific problem or use case. Remember that becoming proficient in any skill requires practice and dedication, and learning about sorting algorithms is no exception.

We hope this section has provided you with a solid foundation for understanding Heap Sort and has sparked your interest in exploring other sorting algorithms and data structures.

## **Chapter 9: Quiz**

1. What is a heap data structure, and what are its two main types?
2. In the context of the Heap Sort algorithm, what is the heap property?
3. What are the best-case, worst-case, and average-case time complexities of Heap Sort?
4. Is Heap Sort a stable sorting algorithm? Explain your answer.
5. What makes Heap Sort an in-place sorting algorithm?
6. (Coding) Implement the Heap Sort algorithm in your preferred programming language. Use the given array as input: `[9, 5, 8, 1, 3, 7]`. Print the sorted array as output.
7. (Coding) Modify the Heap Sort algorithm to work with a min-heap instead of a max-heap. Implement the modified algorithm in your preferred programming language, and use the following array as input: `[5, 8, 1, 3, 7, 9]`. Print the sorted array as output.
8. List two advantages and two disadvantages of using Heap Sort over other sorting algorithms.
9. (Coding) Given an array of integers, write a function that returns the kth largest element using a max-heap. Implement the function in your preferred programming language, and test it with the following input array and value of k: `[3, 2, 1, 5, 6, 4]` and `k = 2`. The expected output is `5`. Print the output as a result of your function call.
10. (Coding) Implement a priority queue using a max-heap data structure in your preferred programming language. The priority queue should support the following operations: insert, delete, and extract maximum. Test your implementation with a series of insert, delete, and extract maximum operations, and print the results after each operation. Use the following array as input: `[5, 3, 17, 10, 84, 19, 6, 22, 9]`.
11. [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

    Given an unsorted array of integers `nums`, find the length of the longest consecutive elements sequence.

    You must write an algorithm that runs in $O(n)$ time complexity.

    Write a function `int longestConsecutive(vector<int>& nums)` that returns the length of the longest consecutive elements sequence.

    **Example 1:**

    Input: `nums = [100, 4, 200, 1, 3, 2]`  
    Output: `4`

    Explanation: The longest consecutive elements sequence is `[1, 2, 3, 4]`. Therefore, its length is 4.

    **Example 2:**

    Input: `nums` = `[0, 3, 7, 2, 5, 8, 4, 6, 0]`  
    Output: `5`

    Explanation: The longest consecutive elements sequence is `[3, 4, 5, 6, 7]`. Therefore, its length is 5.

    **Constraints:**

    - $0\leq$ `nums.length` $\leq 10^5$
    - $-10^9\leq$ `nums[i]` $\leq 10^9$

12. [Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/)  
    You are given an integer array `nums` and two integers `k` and `t`. Return `true` if there are two distinct indices `i` and `j` in the array such that `abs(nums[i] - nums[j]) <= t` and `abs(i - j) <= k`.

    Write a function `bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t)` that returns `true` if the conditions are met, and `false` otherwise.

    **Example 1:**

    Input: `nums = [1, 2, 3, 1], k = 3, t = 0`  
    Output: `true`

    **Example 2:**

    Input: `nums = [1, 0, 1, 1], k = 1, t = 2`  
    Output: `true`

    **Example 3:**

    Input: `nums = [1, 5, 9, 1, 5, 9], k = 2, t = 3`  
    Output: `false`

    **Constraints:**

    $0 \leq$ `nums.length` $\leq 2\times 10^4$  
    $-2^{31}\leq$ `nums[i]` $\leq 2^{31} - 1$  
    $0\leq$ `k` $\leq 10^4$  
    $0\leq$ `t` $\leq 2^{31} - 1$  
    Hint: You can use a sliding window approach and maintain a data structure like a max-heap or min-heap within the window to efficiently check the conditions for nearby almost duplicate elements.
