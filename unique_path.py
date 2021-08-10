from math import factorial as fc

class Solution:
    def fac(self, k):
        return 1 if (k==1 or k==0) else k*self.fac(k-1)
    
    def uniquePaths(self, m: int, n: int) -> int:
