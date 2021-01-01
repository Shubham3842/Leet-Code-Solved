class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x1 = nums[:n]
        x2 = nums[n:]
        l=[]
        for i in range(n):
            c = 0
            if c==0:
                c+=1
                l.append(x1[i])
            if c==1:
                l.append(x2[i])
        return (l)    
