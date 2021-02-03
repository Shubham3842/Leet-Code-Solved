class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        l = []
        for i in A:
            i.reverse()
            l.append(list(map(lambda x: 1 if x==0 else 0,i)))
        return l    