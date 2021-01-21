class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result =[]
        for i in range(left,right+1):
            l = list(str(i))
            c = 0
            if '0' not in l:
                for k in l:
                    if k == 0:
                        break    
                    if i%int(k)==0:
                        c+=1
                if c == len(l):
                    result.append(i)
        return result            
