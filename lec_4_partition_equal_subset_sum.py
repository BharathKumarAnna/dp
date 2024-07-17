class Solution:
    def equalPartition(self, N, arr):
        # code here
        sm = sum(arr)
        memo = {}
        
        if sm % 2 != 0:
            return False
            
        else:
            target = sm //2
            arr.sort(reverse=True)
            
        def solve(n, tot):
            if tot == 0:
                return True
            elif n == 0:
                return False
                
            elif (n,tot) in memo:
                return memo[(n,tot)]
                
            else:
                cur_itm = arr[n-1]
                
                if cur_itm <= tot:
                    c1 = solve(n-1, tot-cur_itm)
                    if c1 == True:
                        memo[(n,tot)] = True
                        return True
                    else:
                        c2 = solve(n-1, tot)
                        # c = c1 or c2
                        
                    memo[(n,tot)] = c2
                    return c2
                else:
                    memo[(n,tot)]=0
                    return memo[(n,tot)]
                    
        return solve(N, target)