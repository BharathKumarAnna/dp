# Top Down approach with DP.
# Memoisation
# recursion
'''
def fib(n,dp):
    if n==0:
        return 0
    elif n == 1:
        return 1
    elif dp[n]!=-1:
        return dp[n]
    else:
        return fib(n-1,dp)+fib(n-2,dp)

n = int(input("Enter the nth value: "))       
dp = [-1 for _ in range(n+1)]        
print(fib(n,dp))
'''


# Bottom Up approach with DP.
# Tabulation
# Iteration

dp = [0]*(101)
dp[1] = 1
for i in range(2,101):
    dp[i] = dp[i-1]+dp[i-2]
    
print(dp[7])

