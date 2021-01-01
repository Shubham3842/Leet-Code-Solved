class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        l1 = list(jewels)
        l2 = list(stones)
        sm = 0
        for i in l1:
            sm +=l2.count(i)
        return sm    
            
