class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sm =0
        for i in range(len(arr)):
            for j in range(len(arr)+1):
                if len(arr[i:j])%2 !=0 and len(arr)!=0:
                    sm +=sum(arr[i:j]) 
        return(sm)            
