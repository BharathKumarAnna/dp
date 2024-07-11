# 0/1 knapsack iterative method

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        dp = [[0]*(W+1) for _ in range(n)]
        for i in range(n):
            for j in range(W+1):
                
                cap = j
                cwt = wt[i]
                cv = val[i]
                if i == 0:
                    if cwt <= cap:
                        dp[i][j] = cv
                    else:
                        dp[i][j] = 0
                else:
                    if cwt <= cap:
                        c1 = cv + dp[i-1][cap-cwt]
                        c2 = 0 + dp[i-1][cap]
                        c = max(c1,c2)
                        dp[i][j] = c
                    else:
                        dp[i][j] = dp[i-1][cap]
        return dp[n-1][W]
