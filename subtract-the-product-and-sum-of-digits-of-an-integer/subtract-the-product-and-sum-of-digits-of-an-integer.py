class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(map(int,list(str(n))))
        sm = 0
        pd = 1
        for i in n:
            sm+=i
            pd*=i
        return (pd-sm)    
