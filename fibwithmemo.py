from typing import Optional


#Typical recursive fibonacci function
#Returns n-th number in fibonacci sequence
#O(2^n) Time Complexity: Tree doubles at each node
#O(n) Space Complexity: Will only ever have n functions called at once before hitting a return value 
def fib(n):
    if (n <= 2):
        return 1
    return fib(n-1) + fib(n-2)
#Recursive fibonacci function utilizing memoization
#Memoization = Stores results of function calls in dictionary to stop repeated calls
#Initial call should ignore the memo parameter, and it will default to a blank dictionary
def fibWithMemo (n,memo = {}):
    if ( n in memo):
        return memo[n]
    if(n<=2): return 1
    memo[n] = fib(n-1,memo) + fib(n-2,memo)
    return memo[n]



print(fib(10))