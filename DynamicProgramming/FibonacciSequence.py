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
#O(n) Time Complexity: Second fib call for each recursive step will have already been solved, meaning that once the program works it's way to the bottom the first time, most of the work is already done
#O(n) Space Complexity: Same reasoning as for regular fib function(above), the dictionary does take up more space, but could never take up more than O(n) space so it doesn't affect the overall big O space.
def fibWithMemo (n, memo = {}):
    if (n in memo):
        return memo[n]
    if (n <= 2):
        return 1
    memo[n] = fibWithMemo(n-1,memo) + fibWithMemo(n-2,memo)
    return memo[n]






#Example calls
print(fib(5)) #Prints 5
print(fibWithMemo(10)) #Prints 55



