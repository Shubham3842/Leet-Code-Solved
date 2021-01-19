class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = dict(paths)
        l = []
        for k,v in d.items():
            l.append(k)
            l.append(v)
        print(d)    
        for i in l:
            for k,v in d.items():
                if l.count(i)==1 and i==v:
                    return i
                    break 
                
