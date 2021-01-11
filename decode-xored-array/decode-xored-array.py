class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        l = []
        l.append(first)
        for i in encoded:
            l.append(i^l[-1])
        return(l)    
