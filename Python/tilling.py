class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1000000007
        dpfull, dpet, dpeb = [0]*(n+1), [0]*(n+1), [0]*(n+1) # full at index i, empty top at index i, etc.
        
        dpfull[0] = 1
        dpfull[1] = 1
        
        for i in range(2, n+1):
            dpfull[i] = (dpfull[i-1] + dpfull[i-2] + dpeb[i-1] + dpet[i-1])%MOD
            dpet[i] = (dpfull[i-2] + dpeb[i-1])%MOD
            dpeb[i] = (dpfull[i-2] + dpet[i-1])%MOD
            
        return dpfull[n]