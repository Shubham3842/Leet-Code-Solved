class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx = 0
        for i in accounts:
            tot = 0
            for j in i:
                tot+=j
            if mx<tot:
                mx=tot
        return mx        
