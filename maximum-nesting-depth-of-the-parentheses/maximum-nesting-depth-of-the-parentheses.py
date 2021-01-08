class Solution:
    def maxDepth(self, s: str) -> int:
        flag = 0
        l =[]
        if s.count('(') != s.count(')') or s.count('(')==0:
            return 0
        else:
            for i in s:
                if i == "(":
                    flag +=1
                    l.append(flag)
                elif i == ")":
                    flag-=1
                    l.append(flag)
        return (max(l))        
                
        
