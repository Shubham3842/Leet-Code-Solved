class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        cnt = 0
        string=""
        while True:
            for i,j in zip(s,indices):
                if j == cnt:
                    string+=i
                    cnt+=1
            if cnt == max(indices)+1 :
                break
        return string    
            
            
                
        
        
