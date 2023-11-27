"""
Task: Binary Search in a Sorted Array

You are given a sorted array of integers. Write a function in a programming language of your choice to implement binary
search to find the index of a given target element in the array. If the target
is not present in the array, the function should return -1.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(binary_search([1, 2, 3 ,4 , 5], 3))