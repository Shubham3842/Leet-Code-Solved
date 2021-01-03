class Solution:
    def numberOfSteps (self, num: int) -> int:
        cnt = 0
        while True:
            if num == 0:
                cnt = 0
            elif num%2==0:
                cnt+=1
                num/=2
            else:
                cnt+=1
                num-=1
            if num==0:
                break
        return cnt        
            
        
