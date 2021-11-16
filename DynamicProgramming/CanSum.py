#Problem: Write a function CanSum(targetsum,numbers) that takes in a targetsum and an array of numbers as arguments
#The function should return a boolean indicating whether or not it is possible to generate the targetSum using numbers from the array.
#You may use an element of the array as many times as needed, and all input numbers are non-negative

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


print(canSum(8,[2,3,5]))
print(canSum(7,[2,4]))