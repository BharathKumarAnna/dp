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