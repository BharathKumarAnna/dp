# Recursive approach:
class Solution:
    def isSubsetSum (self, N, arr, sum):
        def solve(n,sm):
            if sm == 0:
                return 1
            elif n==0:
                return 0
            else:
                item = arr[n-1]
                if item <= sm:
                    c1 = solve(n-1,sm-item)
                    c2 = solve(n-1,sm)
                    return c1 or c2
                else:
                    return solve(n-1,sm)
                
        return solve(N,sum)

# Dp (memoization)
class Solution:
    def isSubsetSum (self, N, arr, sum):
        dp = {}
        def solve(n,sm):
            if sm == 0:
                return 1
            elif n==0:
                return 0
            elif (n,sm) in dp:
                return dp[(n,sm)]
            else:
                item = arr[n-1]
                if item <= sm:
                    c1 = solve(n-1,sm-item)
                    c2 = solve(n-1,sm)
                    c = c1 or c2
                else:
                    c = solve(n-1,sm)
                dp[(n,sm)] = c
                return c
                
        return solve(N,sum)
    
