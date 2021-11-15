#Problem: Say that you are a traveler on a 2d grid. You begin in the top left corner and your goal is to travel to the bottom-right corner
#You may only move down or right
#In how many ways can you travel to the goal on a grid with dimensions m * n?

#Standard brute force recursive implementation
#Time Complexity: O(2^(n + m)) ,  Since tree moves by one for each step, the height is n + m. Since it doubles at every branch, we get the 2 and raisee it to the power of the height.
#Space Complexity: O(n + m) , space complexity is just height of tree, closes nodes after hitting the return statement. 
def gridTraveler(m,n):
    if (m==1 and n ==1):
        return 1
    if m == 0 or n == 0:
        return 0
    return gridTraveler(m - 1 ,n) + gridTraveler(m,n-1)

#Approach using memoization, stores previous function results in a dictionary
#Initial call should leave the memo parament empty, so that it defaults to an empty dictionary
#One interesting note about this function is that gridTravelerWithMemo(1,2) == gridTravelerWithMemo(2,1), this means that memoization allows us to return values for functions we haven't even calculated yet
#Time Complexity: O(n * m) , there are a total of n * m distinct nodes in any situation. In other words, for each node in n, there are m distinct nodes you can make with that.  All other nodes are memoized from these. 
#Space Complexity: O(n + m), heigh of tree, same reasoning for non memoized version. 
def gridTravelerWithMemo(m,n,memo = {}):
    if ((m,n) in memo):
        return memo[(m,n)]
    if (m==1 and n ==1):
        return 1
    if m == 0 or n == 0:
        return 0
    memo[(n,m)] = memo[(m,n)] = gridTravelerWithMemo(m - 1 ,n,memo) + gridTravelerWithMemo(m,n-1,memo)
    return memo[(m,n)]


#Example calls
print(gridTraveler(5,5)) #prints 70
print(gridTravelerWithMemo(20,20)) #prints 35345263800



