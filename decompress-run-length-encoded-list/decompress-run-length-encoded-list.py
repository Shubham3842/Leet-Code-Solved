class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l =[]
        for i in range(len(nums)//2):
            l.extend([nums[2*i+1]]*nums[2*i])
        return l
