'''
todo:
Start with understanding the basics of data structures like lists, sets, dictionaries, tuples, and more.
Practice using dictionaries to store and retrieve key/value pairs.
Create programs that perform operations on dictionary data.
Tuples for Multi-Step Tasks:

Develop programs that involve multi-step tasks using tuples.
Explore sorting and looping with tuples.
Implement various data structures and perform operations on them (e.g., insertion, deletion, searching).'''

# =======================================
#      Sorting Algorithms Implementation
# =======================================

# Python Fundamentals for Data Engineering
# algorithms/sorting_algorithms.py: Implements fundamental algorithms for sorting, searching, and data manipulation.

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print("Sorted Numbers:", numbers)

# ----------------------------------------------
# Conclusion
# ----------------------------------------------

print("Sorting Algorithms - sorting_algorithms.py execution complete.")

# End of sorting_algorithms.py file
