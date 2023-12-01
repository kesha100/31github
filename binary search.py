"""
Task: Binary Search in a Sorted Array

You are given a sorted array of integers. Write a function in a programming language of your choice to implement binary
search to find the index of a given target element in the array. If the target
is not present in the array, the function should return -1.
"""

# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         guess = arr[mid]
#         if guess == target:
#             return mid
#         elif guess > target:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return -1
#
# print(binary_search([1, 2, 3 ,4 , 5], 3))


# def binary_search_rotated(arr, target):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         mid_value = arr[mid]
#         if mid_value == target:
#             return mid
#         if arr[low] <= mid_value:
#             if arr[low] <= target < mid_value:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         else:
#             if mid_value < target <=arr[high]:
#                 low = mid + 1
#             else:
#                 high = mid -1
#     return -17
# print(binary_search_rotated([4, 5, 6, 7, 0, 1, 2], 7))


"""
day3 Selection Sort algorithm
"""

# arr = [64, 25, 12, 22, 11]
#
#
# def selection_sort(arr):
#     for i in range(len(arr)):
#         smallest_ind = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[smallest_ind]:
#                 smallest_ind = j
#         arr[i], arr[smallest_ind] = arr[smallest_ind], arr[i]
#     return arr
#
# print(selection_sort(arr))

"""
day 4 
leetcode problem
Problem Explaination:
roman numbers to numbers
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0

        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i + 1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]

        return ans
solution = Solution()
print(solution.romanToInt('LXI'))

