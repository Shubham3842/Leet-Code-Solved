class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h = heights.copy()
        print(h)
        heights.sort(reverse=False)
        c = 0
        for i,j in zip(heights,h):
            if i!=j:
                c+=1
        return c        
