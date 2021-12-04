#Binary Search
#Time Complexity: O(logn), the array shrinks in half each time it loops
#Space Complexity: O(1), the array is considered free space since it's given as a parameter. The only space used is the pointers
#Notes: This is a very important algorithm to learn. It also clearly showcases what something being logn time means.
def binarySearch(arr,target):
    low = 0
    high = len(arr)
    while low < high:
        mid = (high + low ) // 2
        if arr[mid] > target:
            high = mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1

#Binary Search Insert Position
#"Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order."
#Time Complexity: O(logn), same as normal binary search
#Space Complexity: O(1), same as normal binary search
#Notes: This shows a useful modification of binary search. If a question involves a sorted array, you should see if a modified binary search can work.
def modifiedBinarySearch(arr,target):
    low = 0
    high = len(arr)
    while low < high:
        mid = (high + low) // 2
        if arr[mid] > target:
            high = mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            return mid
    return low

