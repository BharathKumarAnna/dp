#Memoization method

class Solution:
    def perfectSum(self, arr, n, sum):
        dp={}
        arr.sort(reverse=True)
        mod = 10**9+7
        def solve(N,sm):
            if N==0:
                if sm==0:
                    return 1
                else:
                    return 0
            elif (N,sm) in dp:
                return dp[(N,sm)]
            else:
                item = arr[N-1]
                if item<=sm:
                    c1 = solve(N-1,sm-item)
                    c2 = solve(N-1,sm)
                    c = (c1+c2)%mod
                else:
                    if sm==0:
                        c = 1
                    else:
                        c = 0
                dp[(N,sm)] = c
                return c
        return solve(n,sum)

arr = [2,4,6,7,1,3]
sol = Solution() 
print(sol.perfectSum(arr,6,10))

'''

#Iteration method

class Solution:
	def perfectSum(self, arr, n, sum):
		# code here
		dp = [[0]*(sum+1) for _ in range(n)]
		mod = 10**9+7
		for i in range(n):
		    item = arr[i]
            for j in range(sum+1):
		        sm = j
		        if i==0:
		            if sm==0:
		                if item==0:
		                    dp[i][j] = 2
                        else:
		                    dp[i][j] = 1
		            else:
		                if item == sm:
		                    dp[i][j] = 1
		        else:
		            if item<=sm:
		                dp[i][j] = (dp[i-1][sm-item] + dp[i-1][sm])%mod
		            else:
		                dp[i][j] = dp[i-1][sm]
	    return dp[n-1][sum]

arr = [2,4,6,7,1,3]
sol = Solution() 
print(sol.perfectSum(arr,6,10))

'''