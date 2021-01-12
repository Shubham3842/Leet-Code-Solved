class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l = []
        l.append(0)
        for i in nums:
            l.append(l[-1]+i)
        return(l[1:])    
            
