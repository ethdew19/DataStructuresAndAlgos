#Leetcode #1. Two Sum
#https://leetcode.com/problems/two-sum/

#Single pass through dictionary solution
#Time Complexity: O(n), dictionary operations are O(1) time and the for loop is O(n)
#Space Complexity: O(n), dictionary can have n max elements
#notes: Useful pattern of using dictionary to find past elements, and to avoid brute force solution
def twoSum(nums,target):
    myDict = {}
    for index,num in enumerate(nums):
        if (target - nums) in myDict:
            return [myDict[target - num], index]
        else:
            myDict[num] = index

#Leetcode #121. Best Time to Buy and Sell Stock
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

#Single pass through solution
#Time Complexity: O(n), goes through list single time
#Space Complexity: O(1), constant amount of variables are used
#Notes: The key to this one is that once you hit a new lowest point,  that is the only point you need to check for profits from until you hit a new low.  
def maxProfit(prices):
    minPrice = 999999
    maxProfit = 0
    for price in prices:
        if (price < minPrice):
            minPrice = price
        elif (price - minPrice > maxProfit):
            maxProfit = price - minPrice
    return maxProfit

#Leetcode #217. Contains Duplicate
#https://leetcode.com/problems/contains-duplicate/

#Dictionary approach
#Time Complexity: O(n), goes through list single time, dictionary operations are constant time
#Space Complexity: O(n), max of n elements placed into the dictionary
#Notes: useful pattern of dictionarys/hashmaps being used to determine if an element is unique
def containsDuplicate(nums):
    myDict = {}
    for i in nums:
        if i in myDict:
            return True
        else:
            myDict[i] = 1
    return False