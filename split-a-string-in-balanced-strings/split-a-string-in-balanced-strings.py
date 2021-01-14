class Solution:
​
    def balancedStringSplit(self, s: str) -> int:
        c,r,l=0,0,0
        for i in s:
            if i=='R':
                r+=1
            elif i=='L':
                l+=1
            if r==l:
                c+=1
                r,l=0,0
        return(c)       
        
