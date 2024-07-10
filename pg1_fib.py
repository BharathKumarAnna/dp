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

# Top Down approach with DP.
# Memorization
# recursion