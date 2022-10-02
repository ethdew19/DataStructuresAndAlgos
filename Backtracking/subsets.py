# Leetcode 78. 
# Given an integer array nums, return all possible subsets. Answer must not include duplicates.
#Solution credit : Neetcode 150


#Time complexity: O(2^n), the total amount of subsets that will exist
#At each element you have two options, either add the element to the subset or not
def subsets(nums):
    res = []

    subset = [] #Gives dfs global access to subset
    def dfs(i):
        if i >= len(nums):
            res.append(subset[:]) #Cheaper way of .copy ing a list
            return

        subset.append(nums[i])
        dfs(i + 1)

        subset.pop()
        dfs(i + 1)
        
    dfs(0)
    return res