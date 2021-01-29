class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        diff = 0
        mx = 0 
        for i in gain:
            diff+=i
            if mx < diff:
                mx = diff    
        if mx < 0 :
            return 0
        else:
            return mx