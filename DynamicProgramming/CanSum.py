#Problem: Write a function CanSum(targetsum,numbers) that takes in a targetsum and an array of numbers as arguments
#The function should return a boolean indicating whether or not it is possible to generate the targetSum using numbers from the array.
#You may use an element of the array as many times as needed, and all input numbers are non-negative

#Brute force recursive implementation
#Time Complexity: O(n^m), where m is target sum and n is array length
#Space Complexity: O(m), since height of tree is a multiple of m
def canSum(target, nums):
    if target == 0:
        return True
    if target < 0:
        return False
    for i in nums:
        remainder = target - i
        if canSum(remainder,nums):
            return True
        
    return False
#Memoized recursive implementation
#Time Complexity: O(m * n), basically height times length of new tree after we memoize
#Space Complexity: O(m), still height of the tree
def canSumMemo(target,nums,memo = None):
    if memo == None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    for i in nums:
        remainder = target - i
        if canSumMemo(remainder,nums,memo):
            memo[target] = True
            return True
    memo[target] = False
    return False

#Example calls
print(canSum(8,[2,3,5])) #True
print(canSum(7,[2,4])) #False
print(canSumMemo(8,[2,3,5])) #True
print(canSumMemo(300,[7,14])) #False